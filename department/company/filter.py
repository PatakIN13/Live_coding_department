from django_filters import rest_framework as filters
from .models import Department, Person


class DepartmentFilter(filters.FilterSet):
    class Meta:
        model = Department
        fields = {
            'id': ['exact'],
            'name': ['exact'],
        }


class PersonFilter(filters.FilterSet):

    class Meta:
        model = Person
        fields = ('last_name', 'depatrment',)
