from django.contrib import admin
from .models import StudentInfo

# Register your models here.
@admin.register(StudentInfo)
class AdminStudent(admin.ModelAdmin):
    list_display = [field.name for field in StudentInfo._meta.fields]