from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Person, Command


class CommandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Command
        fields = ['id', 'name']

    def create(self, validated_data):
        if Command.objects.filter(**validated_data).exists():
            raise ValidationError('Command with this name already exists.')
        return Command.objects.create(**validated_data)


class PersonSerializer(serializers.ModelSerializer):
    name = serializers.RegexField(regex=r'^[A-Za-z\s\'-]+$',
                                  error_messages={
                                      'invalid': 'Name can only contain letters, spaces, hyphens, and apostrophes'})
    surname = serializers.RegexField(regex=r'^[A-Za-z\s\'-]+$',
                                     error_messages={
                                         'invalid': 'Surname can only contain letters, spaces, hyphens, and apostrophes'})

    class Meta:
        model = Person
        fields = ['id', 'name', 'surname', 'mail', 'command']

    def create(self, validated_data):
        if Person.objects.filter(**validated_data).exists():
            raise ValidationError('User already exists.')
        if validated_data['name'] == validated_data['surname']:
            raise serializers.ValidationError('Name and Surname should not be same.')
        return Person.objects.create(**validated_data)
