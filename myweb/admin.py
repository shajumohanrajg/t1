from django.contrib import admin
from import_export import resources
from .models import Registration
from import_export.admin import ImportExportModelAdmin
from django.utils.html import format_html



class RegistrationResource(resources.ModelResource):
    class Meta:
        model = Registration


class AdminRegistration(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = RegistrationResource
    # fields = [field.name for field in Registration._meta.get_fields()]

    fields = ['user_id','gender','date_of_birth','time_of_birth','place_of_birth',
              'mother_tongue','marital_status','father_name','father_occupation',
              'mother_name','mother_occupation','no_of_brothers','no_of_married_brothers',
              'no_of_sisters','no_of_married_sisters','height','weight','physical_status',
              'body_type','complexion','diet','educational_qualification',
              'job','place_of_job','income_per_month','religious','caste',
              'gothra','lagnam','raasi','star','raasi_chart','navamsam_chart',
              'contact_name','mobileNumber','whatsapp','country','state','district',
              'city','photo1','photo2','photo3','photo4','preference_religion','preference_caste',
              'preference_marital_status','preference_diet','preference_educational_qualification',
              'preference_job','preference_income_per_month','preference_location'
              ]
    list_display = ['user_id','gender']
    # fields = ['__all__']
    # search_fields = ['name','email','phone']
    # list_filter = ['date_joined']
    # ordering = ["-id"]

    def thumbnail(self,obj):
        if obj.raasi_chart:
            return format_html('<img src="{}" width="50" height="50" />',obj.raasi_chart.url)
        return ''
    thumbnail.short_description = "Profile Picture"


admin.site.register(Registration,AdminRegistration)
