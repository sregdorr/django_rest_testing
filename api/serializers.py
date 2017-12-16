from rest_framework import serializers

from api import models


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields = (
            'id',
            'url',
            'first_name',
            'last_name',
            'age',
        )

