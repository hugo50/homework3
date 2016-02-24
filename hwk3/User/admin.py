from django.contrib import admin

# Register your models here.
from User.models import *

admin.site.register(Message)
admin.site.register(Secret_Message)
