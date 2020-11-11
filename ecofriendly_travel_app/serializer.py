from rest_framework import serializers
from .models import User, Trip


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'firstName','lastName','phone','carbon_footprint', 'total_eco_points']


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ['user', 'source', 'destination', 'distance']