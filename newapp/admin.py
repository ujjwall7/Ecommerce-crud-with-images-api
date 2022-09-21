from atexit import register
from django.contrib import admin
from .models import Ecommerce


class ecommercedisplay(admin.ModelAdmin):
    list_display = ['Name','Price','Description','Image']



admin.site.register(Ecommerce,ecommercedisplay)