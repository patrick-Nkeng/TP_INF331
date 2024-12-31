from django.contrib import admin
from .models import Problem, Intervention
from django.contrib.auth.models import Group

admin.site.site_header = 'TechAssist'

class ProblemAdmin(admin.ModelAdmin):
    list_display = ('NomProblem','statut', 'type')

# Register your models here.
admin.site.register(Problem, ProblemAdmin)
admin.site.register(Intervention)
# admin.site.unregister(Group)