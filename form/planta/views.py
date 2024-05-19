from django.shortcuts import render
# views.py
from rest_framework import generics
from .models import Title, Description
from .serializers import TitleSerializer, DescriptionSerializer
from .models import User, Owner, Property, Booking
from .serializers import BookingSerializer, OwnerSerializer, PropertySerializer, UserSerializer




class TitleListCreateAPIView(generics.ListCreateAPIView):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer

class TitleRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer

class DescriptionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Description.objects.all()
    serializer_class = DescriptionSerializer

class DescriptionRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Description.objects.all()
    serializer_class = DescriptionSerializer
# Create your views here.




class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class OwnerListView(generics.ListCreateAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class OwnerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class PropertyListView(generics.ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class PropertyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class BookingListView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
