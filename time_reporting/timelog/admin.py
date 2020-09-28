from django.contrib import admin
from .models import Hours
# Register your models here.


class HoursAdmin(admin.ModelAdmin):
    status = 'Completed'
admin.site.register(Hours, HoursAdmin)
