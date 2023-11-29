from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .models import Department, Person
from .serializers import DepartmentSerializer, PersonSerializer
from .filter import PersonFilter
# Create your views here.


class DepartmentViewSet(ModelViewSet):
    model = Department
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class PersonViewSet(ModelViewSet):
    model = Person
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = PersonFilter
