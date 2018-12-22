from django.contrib.auth.models import User
from rest_framework import serializers as sz


class UserSerializer(sz.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')