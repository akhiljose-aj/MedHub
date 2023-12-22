from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(user)
admin.site.register(admin_log)
admin.site.register(user_log)
admin.site.register(doctor_form)
admin.site.register(appoint_booking)