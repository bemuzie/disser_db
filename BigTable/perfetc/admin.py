from django.contrib import admin
from perfetc.models import *


class EdgeInline(admin.StackedInline):
    model = Edge
    fk_name = 'from_compartment'

class CompartmentAdmin(admin.ModelAdmin):
    inlines = [EdgeInline]

admin.site.register(Compartment, CompartmentAdmin)

admin.site.register(Body)

