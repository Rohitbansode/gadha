# serializers.py
from rest_framework import serializers
from .models import Title, Description

class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Description
        fields = ['id', 'title', 'description_text']

class TitleSerializer(serializers.ModelSerializer):
    descriptions = DescriptionSerializer(many=True, read_only=True)

    class Meta:
        model = Title
        fields = ['id', 'title', 'descriptions']



from .models import User, Owner, Property, Booking

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ['id', 'user', 'phone']

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['id', 'owner', 'title', 'description', 'address', 'price', 'bedrooms', 'bathrooms', 'sqft', 'amenities']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'user', 'property', 'start_date', 'end_date', 'total_price', 'status']


