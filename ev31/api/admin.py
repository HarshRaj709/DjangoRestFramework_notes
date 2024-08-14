from django.contrib import admin
from .models import Singer,Songs

# Register your models here.
@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Singer._meta.fields]


@admin.register(Songs)
class SingerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Songs._meta.fields]