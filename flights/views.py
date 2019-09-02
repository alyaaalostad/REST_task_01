from rest_framework.generics import ListAPIView
from .models import Flight, Booking
from django.utils import timezone
from .serializers import FlightSerializer, BookingSerializer

class Flights_view(ListAPIView):
	queryset= Flight.objects.all()
	serializer_class= FlightSerializer

class Booking_view(ListAPIView):
	queryset= Booking.objects.filter(date__gte=timezone.now())
	serializer_class= BookingSerializer