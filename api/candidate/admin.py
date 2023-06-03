from django.contrib import admin
from .models import StudentModel
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','age','city','course','mobile']

admin.site.register(StudentModel,StudentAdmin)