from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Ticket
from .serializers import TicketSerializer

class TicketListAPIView(APIView):
    def get(self, request):
        tickets = Ticket.objects.all()
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TicketSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)