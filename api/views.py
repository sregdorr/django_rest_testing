from django.shortcuts import render
from rest_framework import viewsets

from api import models
from api import serializers


class PersonViewSet(viewsets.ModelViewSet):
    queryset = models.Person.objects.all().order_by('last_name')
    serializer_class = serializers.PersonSerializer