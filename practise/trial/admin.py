from django.contrib import admin
from .models import Students

# Register your models here.
@admin.register(Students)
class AdminRegister(admin.ModelAdmin):
    list_display = [field.name for field in Students._meta.fields]