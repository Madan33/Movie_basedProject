from rest_framework import serializers
from .models import Movieinfo


class MovieinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movieinfo
        fields = '__all__'

