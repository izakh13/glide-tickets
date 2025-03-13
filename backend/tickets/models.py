from django.db import models
from helpers.enums import TicketTypes

_ticket_type = (
    ('choose_value', '--Choose a right value--'),
    ('adult', 'Adult'),
    ('children', 'Children')
)

_means_of_transport = (
    ('choose_value', '--Choose a right value--'),
    ('airplane', 'Airplane'),
    ('coach', 'Coach'),
    ('train', 'Train')
)

class Ticket(models.Model):
    ticket_type = models.CharField(choices=TicketTypes.get_all(), default=TicketTypes.CHOOSE_VALUE.value, max_length=100)
    means_of_transport = models.CharField(choices=_means_of_transport, default='choose_value', max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    where_from = models.CharField(max_length=100)
    where_to = models.CharField(max_length=100)
    price = models.FloatField(max_length=10)
