from django.contrib import admin

from .models import Person,Message

admin.site.register(Person)
admin.site.register(Message)