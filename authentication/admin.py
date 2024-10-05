from django.contrib import admin
from .models import User
from import_export.admin import ImportExportModelAdmin


class AdminUser(ImportExportModelAdmin, admin.ModelAdmin):
    pass
    # fields = ("email", "username", "password", 'is_active', 'is_verified', 'is_staff')
    list_display = ['id','email', 'username', 'password']


admin.site.register(User, AdminUser)
