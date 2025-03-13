from django.urls import path
from .views import TicketListAPIView

urlpatterns = [
    path('tickets/', view=TicketListAPIView.as_view(), name='ticket_list')
]