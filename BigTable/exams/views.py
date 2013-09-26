# Create your views here.
# -*- coding: utf-8 -*-
from django.conf import settings
from django.utils import simplejson
from django.http import HttpResponse, HttpResponseRedirect, Http404,HttpResponseBadRequest
from django.template import RequestContext, loader, Context
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib import messages
from django.utils.encoding import smart_str
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.core.servers.basehttp import FileWrapper
from datetime import date
import os
import cStringIO as StringIO
from reportlab.pdfgen import canvas
from exams.models import *
from exams.forms import *
from exams import decorators


def index(request):
    reminder=Reminder.objects.filter(done=False).order_by('remind_date')
    template = loader.get_template('reports/index.html')
    today=date.today()
    reminder_expired=[r for r in reminder if r.remind_date<today]
    reminder_uptodate=[r for r in reminder if r.remind_date>=today]
    context = RequestContext(request,{'reminder_expired':reminder_expired,
                                        'reminder_uptodate':reminder_uptodate})
    return HttpResponse(template.render(context))

def patient_list(request):
    search_field = request.GET.get('search') or ''
    latest_patients_list = Patient.objects.filter(fio__regex=r'(%s|%s)'%(search_field,search_field.capitalize())).order_by('-fio')
    exams_num_list = [len(i.examination_set.all()) for i in latest_patients_list]
    latest_patients_list = zip(latest_patients_list,exams_num_list)
    template = loader.get_template('reports/patient_list.html')
    context = RequestContext(request, {'latest_patients_list':latest_patients_list})
    return HttpResponse(template.render(context))

def detail(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    patient_form = PatientForm_lite(instance=patient)
    examinations = patient.examination_set.all()
    docs_form = DocsForm()
    reminder_formset = ReminderFormSet(queryset=Reminder.objects.filter(patient=patient),
        initial=[{'patient':patient}])
    
    if request.POST.get('patient_submit'):
        
        patient_form = PatientForm_lite(request.POST or None,instance=patient)
        if patient_form.is_valid():
            patient_form.save()

            patient_form = PatientForm_lite(instance=patient)
            return HttpResponseRedirect(reverse('exams.views.detail', args=(patient.id,)))
    elif request.POST.get('docs_submit'):
        
        docs_form = DocsForm(request.POST or None,request.FILES or None)
        if docs_form.is_valid():
            docs_form.save(commit=False)
            docs_form.patient=patient
            
            patient.docs_set.add(docs_form.instance)
            docs_form = DocsForm()
            return HttpResponseRedirect(reverse('exams.views.detail', args=(patient.id,)))
    
    return render(request,'reports/detail.html',{'patient':patient,
                                                'examinations' : examinations, 
                                                'docs_form':docs_form,
                                                "patient_form":patient_form,
                                                'reminder_formset':reminder_formset

                                                })

def add_patient(request):
    
    patient_form = PatientForm(request.POST or None)
    if patient_form.is_valid():
        patient_form.save()
        return HttpResponseRedirect(reverse('exams.views.detail', args=(patient_form.instance.id,)))
    return render (request,'reports/add_patient.html',
        {'patient_form':patient_form,})
def new_examination(request, patient_id, examination_id=None):
    patient = get_object_or_404(Patient, pk=patient_id)
    if examination_id:
        examination_form = ExaminationForm(request.POST or None, 
                                        instance = patient.examination_set.get(pk=examination_id))
    else:
        examination_form = ExaminationForm(request.POST or None)
        
    if examination_form.is_valid():
        examination_form.save(commit=False)
        examination_form.patient=patient
        patient.examination_set.add(examination_form.instance)
        return HttpResponseRedirect(reverse('exams.views.detail', args=(patient.id,)))
    return render(request, 'reports/add_examination.html', {'patient':patient,
                                                            'examination_form':examination_form})

def modify_examination(request, patient_id, examination_id):
    
    if request.POST.get('delete'):
        patient = get_object_or_404(Patient, pk=patient_id)
        patient.examination_set.get(pk=examination_id).delete()
        return HttpResponseRedirect(reverse('exams.views.detail', args=(patient.id,)))
    elif request.POST.get('modify'):
        return HttpResponseRedirect(reverse('exams.views.new_examination', args=(patient_id,examination_id)))
    elif request.POST.get('download'):
        response = HttpResponse(mimetype='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=somefilename.pdf'

        buffer = StringIO.StringIO()

        # Create the PDF object, using the StringIO object as its "file."
        p = canvas.Canvas(buffer)

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        p.drawString(100, 100, "Hello world.")

        # Close the PDF object cleanly.
        p.showPage()
        p.save()

        # Get the value of the StringIO buffer and write it to the response.
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response
    else:
        raise Http404
@decorators.example
def modify_reminder(request, patient_id):
    
    patient = get_object_or_404(Patient, pk=patient_id)
    reminder_form = ReminderForm(request.POST or None)
    if request.POST.get("new_reminder"):
        reminder_formset = ReminderFormSet(request.POST)
        print 'before'
        if reminder_formset.is_valid():
            print 'after'
            reminder_formset.save(commit=False)
            for f in reminder_formset:
                f.patient=patient
                try:
                    pi=patient.reminder_set.get(pk=f.instance.id)
                    pi=f.instance


                except:
                    patient.reminder_set.add(f.instance)
            
            reminder_formset = ReminderFormSet(queryset=Reminder.objects.filter(patient=patient),
                initial=[{'patient':patient}])
            return HttpResponseRedirect(reverse('exams.views.detail', args=(patient.id,)))
    

    if request.POST.get("change_reminder"):
        reminder = patient.reminder_set.get(pk=request.POST.get("change_reminder"))
        print 1
        reminder.done = not reminder.done
        reminder.save()
        
        return HttpResponse(status=204)
    if request.POST.get("delete_reminder"):
        
        patient.reminder_set.get(pk=request.POST.get("delete_reminder")).delete()
        return HttpResponseRedirect(reverse('exams.views.detail', args=(patient.id,)))
    return detail(request, patient_id)
        

def delete_patient (request, patient_id):
    if request.POST:
        patient = get_object_or_404(Patient, pk=patient_id)
        patient.delete()
        return HttpResponseRedirect(reverse('exams.views.patient_list'))
    else:
        raise Http404
def statistis(request):
    patients_num = len(Patient.objects.all())
    examinations_num = len(Examinations.objects.all().filter(modality='P'))
    

def upload(request):
    """
    
    ## View for file uploads ##

    It does the following actions:
        - displays a template if no action have been specified
        - upload a file into unique temporary directory
                unique directory for an upload session
                    meaning when user opens up an upload page, all upload actions
                    while being on that page will be uploaded to unique directory.
                    as soon as user will reload, files will be uploaded to a different
                    unique directory
        - delete an uploaded file

    ## How Single View Multi-functions ##

    If the user just goes to a the upload url (e.g. '/upload/'), the request.method will be "GET"
        Or you can think of it as request.method will NOT be "POST"
    Therefore the view will always return the upload template

    If on the other side the method is POST, that means some sort of upload action
    has to be done. That could be either uploading a file or deleting a file

    For deleting files, there is the same url (e.g. '/upload/'), except it has an
    extra query parameter. Meaning the url will have '?' in it.
    In this implementation the query will simply be '?f=filename_of_the_file_to_be_removed'

    If the request has no query parameters, file is being uploaded.

    """

    # used to generate random unique id
    import uuid

    # settings for the file upload
    #   you can define other parameters here
    #   and check validity late in the code
    options = {
        # the maximum file size (must be in bytes)
        "maxfilesize": 2 * 2 ** 20, # 2 Mb
        # the minimum file size (must be in bytes)
        "minfilesize": 1 * 2 ** 10, # 1 Kb
        # the file types which are going to be allowed for upload
        #   must be a mimetype
        "acceptedformats": (
            "image/jpeg",
            "image/png",
            )
    }


    # POST request
    #   meaning user has triggered an upload action
    if request.method == 'POST':
        # figure out the path where files will be uploaded to
        # PROJECT_ROOT is from the settings file
        temp_path = os.path.join(settings.PROJECT_PATH, "tmp")

        # if 'f' query parameter is not specified
        # file is being uploaded
        if not ("f" in request.GET.keys()): # upload file

            # make sure some files have been uploaded
            if not request.FILES:
                return HttpResponseBadRequest('Must upload a file')

            # make sure unique id is specified - VERY IMPORTANT
            # this is necessary because of the following:
            #       we want users to upload to a unique directory
            #       however the uploader will make independent requests to the server
            #       to upload each file, so there has to be a method for all these files
            #       to be recognized as a single batch of files
            #       a unique id for each session will do the job
            if not request.POST[u"uid"]:
                return HttpResponseBadRequest("UID not specified.")
                # if here, uid has been specified, so record it
            uid = request.POST[u"uid"]

            # update the temporary path by creating a sub-folder within
            # the upload folder with the uid name
            temp_path = os.path.join(temp_path, uid)

            # get the uploaded file
            file = request.FILES[u'files[]']

            # initialize the error
            # If error occurs, this will have the string error message so
            # uploader can display the appropriate message
            error = False

            # check against options for errors

            # file size
            if file.size > options["maxfilesize"]:
                error = "maxFileSize"
            if file.size < options["minfilesize"]:
                error = "minFileSize"
                # allowed file type
            if file.content_type not in options["acceptedformats"]:
                error = "acceptFileTypes"


            # the response data which will be returned to the uploader as json
            response_data = {
                "name": file.name,
                "size": file.size,
                "type": file.content_type
            }

            # if there was an error, add error message to response_data and return
            if error:
                # append error message
                response_data["error"] = error
                # generate json
                response_data = simplejson.dumps([response_data])
                # return response to uploader with error
                # so it can display error message
                return HttpResponse(response_data, mimetype='application/json')


            # make temporary dir if not exists already
            if not os.path.exists(temp_path):
                os.makedirs(temp_path)

            # get the absolute path of where the uploaded file will be saved
            # all add some random data to the filename in order to avoid conflicts
            # when user tries to upload two files with same filename
            filename = os.path.join(temp_path, str(uuid.uuid4()) + file.name)
            # open the file handler with write binary mode
            destination = open(filename, "wb+")
            # save file data into the disk
            # use the chunk method in case the file is too big
            # in order not to clutter the system memory
            for chunk in file.chunks():
                destination.write(chunk)
                # close the file
            destination.close()

            # here you can add the file to a database,
            #                           move it around,
            #                           do anything,
            #                           or do nothing and enjoy the demo
            # just make sure if you do move the file around,
            # then make sure to update the delete_url which will be send to the server
            # or not include that information at all in the response...

            # allows to generate properly formatted and escaped url queries
            import urllib

            # url for deleting the file in case user decides to delete it
            response_data["delete_url"] = request.path + "?" + urllib.urlencode(
                    {"f": uid + "/" + os.path.split(filename)[1]})
            # specify the delete type - must be POST for csrf
            response_data["delete_type"] = "POST"

            # generate the json data
            response_data = simplejson.dumps([response_data])
            # response type
            response_type = "application/json"

            # QUIRK HERE
            # in jQuey uploader, when it falls back to uploading using iFrames
            # the response content type has to be text/html
            # if json will be send, error will occur
            # if iframe is sending the request, it's headers are a little different compared
            # to the jQuery ajax request
            # they have different set of HTTP_ACCEPT values
            # so if the text/html is present, file was uploaded using jFrame because
            # that value is not in the set when uploaded by XHR
            if "text/html" in request.META["HTTP_ACCEPT"]:
                response_type = "text/html"

            # return the data to the uploading plugin
            return HttpResponse(response_data, mimetype=response_type)

        else: # file has to be deleted

            # get the file path by getting it from the query (e.g. '?f=filename.here')
            filepath = os.path.join(temp_path, request.GET["f"])

            # make sure file exists
            # if not return error
            if not os.path.isfile(filepath):
                return HttpResponseBadRequest("File does not exist")

            # delete the file
            # this step might not be a secure method so extra
            # security precautions might have to be taken
            os.remove(filepath)

            # generate true json result
            # in this case is it a json True value
            # if true is not returned, the file will not be removed from the upload queue
            response_data = simplejson.dumps(True)

            # return the result data
            # here it always has to be json
            return HttpResponse(response_data, mimetype="application/json")

    else: #GET
        # load the template
        t = loader.get_template("upload.html")
        c = Context({
            # the unique id which will be used to get the folder path
            "uid": uuid.uuid4(),
            # these two are necessary to generate the jQuery templates
            # they have to be included here since they conflict with django template system
            "open_tv": u'{{',
            "close_tv": u'}}',
            # some of the parameters to be checked by javascript
            "maxfilesize": options["maxfilesize"],
            "minfilesize": options["minfilesize"],
            })
        # add csrf token value to the dictionary
        c.update(csrf(request))
        # return
        return HttpResponse(t.render(c))

