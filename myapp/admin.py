from django.contrib import admin 
from .models import *

# Register your models here.

@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    
    
@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('id', 'district_name', 'get_division')
    list_filter = ('division',)
    search_fields = ('district_name',)
    
    def get_division(self, obj):
        return obj.division.name
    
    get_division.short_description = 'Division'


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'division', 'district')
    list_filter = ('division', 'district')
    search_fields = ('name', 'email')
    