from django.contrib import admin

# Register your models here.
from .models import Person

class PersonAdmin(admin.ModelAdmin):
    list_display = ['name']
    fields = ['name', 'description', 'image']

admin.site.register(Person, PersonAdmin)