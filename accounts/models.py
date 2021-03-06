# from django.db import models as db
from django.contrib.auth.models import User
from rest_framework import serializers as sz


class UserSerializer(sz.HyperlinkedModelSerializer):
    class Meta:
        models = User
        fields = ('url', 'username', 'email', 'groups')