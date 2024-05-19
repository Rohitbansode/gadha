# urls.py
from django.urls import path
from .views import (
    TitleListCreateAPIView,
    TitleRetrieveUpdateDestroyAPIView,
    DescriptionListCreateAPIView,
    DescriptionRetrieveUpdateDestroyAPIView,
)

from .views import (UserListView, UserDetailView, OwnerListView,
OwnerDetailView, PropertyListView,
PropertyDetailView, BookingListView, BookingDetailView
)


urlpatterns = [
    path('titles/', TitleListCreateAPIView.as_view(), name='title-list-create'),
    path('titles/<int:pk>/', TitleRetrieveUpdateDestroyAPIView.as_view(), name='title-detail'),
    path('descriptions/', DescriptionListCreateAPIView.as_view(), name='description-list-create'),
    path('descriptions/<int:pk>/', DescriptionRetrieveUpdateDestroyAPIView.as_view(), name='description-detail'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('owners/', OwnerListView.as_view(), name='owner-list'),
    path('owners/<int:pk>/', OwnerDetailView.as_view(), name='owner-detail'),
    path('properties/', PropertyListView.as_view(), name='property-list'),
    path('properties/<int:pk>/', PropertyDetailView.as_view(), name='property-detail'),
    path('bookings/', BookingListView.as_view(), name='booking-list'),
    path('bookings/<int:pk>/', BookingDetailView.as_view(), name='booking-detail'),

]
