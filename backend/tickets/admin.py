from django.contrib import admin
from .models import Ticket

class TicketAdmin(admin.ModelAdmin):
    list_display = ('ticket_type', 'means_of_transport', 'created_at', 'where_from', 'where_to', 'price')

admin.site.register(Ticket, TicketAdmin)