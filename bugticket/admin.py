from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from bugticket.models import CustomUser, Ticket

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Ticket)
