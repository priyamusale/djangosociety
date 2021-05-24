from django.contrib import admin
from .models import Group, Event, People
# Register your models here.

admin.site.register(Group)
admin.site.register(Event)
admin.site.register(People)
