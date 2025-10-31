from django.contrib import admin
from .models import Tag, ProductTag
# Register your models here.
admin.site.register([Tag, ProductTag])