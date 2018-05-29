from django.contrib import admin

from .models import SayingPost, Subject

# Register your models here.

admin.site.register(Subject)
admin.site.register(SayingPost)