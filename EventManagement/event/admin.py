from django.contrib import admin
from . import models

admin.site.register(models.Event)
admin.site.register(models.TicketSale)
admin.site.register(models.ManageAttendees)
admin.site.register(models.ManagersPlanner)
