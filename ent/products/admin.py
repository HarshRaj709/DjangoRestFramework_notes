from django.contrib import admin
from .models import Products

# Register your models here.
@admin.register(Products)
class AdminProducts(admin.ModelAdmin):
    list_display = [field.name for field in Products._meta.fields]
    ordering = ['title']        #to show in a definit order