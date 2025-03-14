from django.db import models
from helpers.enums import TicketTypes, MeansOfTransport


class Ticket(models.Model):
    ticket_type = models.CharField(
        choices=TicketTypes.get_all(),
        default=TicketTypes.CHOOSE_VALUE.value,
        max_length=100,
    )
    means_of_transport = models.CharField(
        choices=MeansOfTransport.get_all(),
        default=MeansOfTransport.CHOOSE_VALUE.value,
        max_length=100,
    )
    created_at = models.DateTimeField(auto_now=True)
    where_from = models.CharField(max_length=100)
    where_to = models.CharField(max_length=100)
    price = models.FloatField(max_length=10)
