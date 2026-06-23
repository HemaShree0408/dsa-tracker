from django.contrib import admin

# Register your models here.
from .models import Topic, Problem

admin.site.register(Topic)
admin.site.register(Problem)