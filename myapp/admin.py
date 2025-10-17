from django import forms
from django.contrib import admin
from django.urls import path
from django.http import JsonResponse
from .models import Division, District, Person

# Custom form for Person
class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

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
    form = PersonForm
    list_display = ('id', 'name', 'email', 'division', 'district')
    list_filter = ('division', 'district')
    search_fields = ('name', 'email')

    class Media:
        js = ('js/filter_districts.js',)  # make sure this path is correct

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('get_districts/', self.admin_site.admin_view(self.get_districts))
        ]
        return custom_urls + urls

    def get_districts(self, request):
        division_id = request.GET.get('division')
        districts = District.objects.filter(division_id=division_id).values('id', 'district_name')
        return JsonResponse(list(districts), safe=False)
