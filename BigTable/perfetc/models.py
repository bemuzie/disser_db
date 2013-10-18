from django.db import models
from perfetc import circulation_models
from exams import models as exams_model
# Create your models here.
class Body(models.Model):
	injection_duration = models.IntegerField()
	examination=models.IntegerField(default=0)
	experimental_time_axis = models.CharField(max_length=100)
	def calculate_tac(self,time_duration,time_resolution):
		tmp_model={}
		for node in compartment_set.all():
			newnode=circulation_models.Compartment(node.name)
			newnode.time=np.arange(0,time_duration,time_resolution)
			newnode.set_attrs(node.mean,node.sigma,node.parametr3)
			if node.injection:
				newnode.make_delta()
			tmp_model[node.name]=newnode
		for node in compartment_set.all():
			[tmp_model[node.name].add_successor(tmp_model[n.name],n.weight) for n in node.successors]
		tmp_model['Injection'].successors[0]()
		return dict([(n.name,n.concentration) for n in tmp_model.values()])
	def get_timeaxis_as_list(self):
		return map(int,self.timeaxis.split(','))
			



class Compartment(models.Model):
	body = models.ForeignKey('Body')
	successors = models.ManyToManyField('self', through = 'Edge', symmetrical = False)
	name = models.CharField(max_length=10) 
	pdf = models.CharField(max_length=10)
	mean = models.FloatField()
	sigma = models.FloatField()
	parametr3 = models.FloatField()
	injection = models.BooleanField()
	experimental_concentration = models.CharField(max_length=100)


	def __unicode__(self):
		return self.name
	def add_edge(self, compartment, weight = 1):
		if weight > 1 or weight < 0:
			raise ValueError('weight should be in range from 0 to 1')
		edge, created = Edge.objects.get_or_create(
			from_compartment = self,
			to_compartment = compartment, 
			weight = weight)
		return edge
	def get_experimental_conc_as_list(self):
		return map(int,self.experimental_concentration.split(','))






class Edge(models.Model):
	from_compartment = models.ForeignKey(Compartment,related_name='from_compartment')
	to_compartment = models.ForeignKey(Compartment, related_name='to_compartment')
	weight = models.FloatField()