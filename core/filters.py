import django_filters
from .models import Vacancy


class VacancyFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    salary__gt = django_filters.NumberFilter(field_name='salary', lookup_expr='gt')
    salary__lt = django_filters.NumberFilter(field_name='salary', lookup_expr='lt')

    class Meta:
        model = Vacancy
        fields = ['title']

class VacancyExperience(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    required_work_experience__gt = django_filters.NumberFilter(field_name='required_work_experience', lookup_expr='gt')
    required_work_experience__lt = django_filters.NumberFilter(field_name='required_work_experience', lookup_expr='lt')

    class Meta:
        model = Vacancy
        fields = ['title']
