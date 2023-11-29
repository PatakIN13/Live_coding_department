from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from .models import Department, Person


class PersonSerializer(serializers.ModelSerializer):
    depatrment = serializers.StringRelatedField()

    class Meta:
        model = Person
        fields = "__all__"

    def create(self, validated_data):
        return Person.objects.create(**validated_data)

    def delete(self, validated_data):
        return Person.objects.delete(**validated_data)


class DepartmentSerializer(serializers.ModelSerializer):
    manager = PersonSerializer()

    class Meta:
        model = Department
        fields = ['id', 'name', 'manager']