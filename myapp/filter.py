from .models import snippet
import django_filters
from django import forms
from django.contrib.auth.models import User, Group

class snippetFilter(django_filters.FilterSet):
    CHOICE = (('ascending','Ascending'),
    ('descending','Descending')
    )

    ordering = django_filters.ChoiceFilter(label='Ordering',choices=CHOICE, method='filter_by_order')
    class Meta:
        model = snippet
        fields = ('title', 'body',
                  #'created'
                  )
    def filter_by_order(self, queryset, name, value):
        expression = 'created' if value =='ascending' else '-created'
        return queryset.order_by(expression)

class UserFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    year_joined = django_filters.NumberFilter(field_name='date_joined', lookup_expr='year')
    year_joined__gt = django_filters.NumberFilter(field_name='date_joined', lookup_expr='year__gt')
    year_joined__lt = django_filters.NumberFilter(field_name='date_joined', lookup_expr='year__lt')
    groups = django_filters.ModelMultipleChoiceFilter(queryset=Group.objects.all(),widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'groups']

        """
        fields = {  #Another option is to define the fields as a dictionary:
            'username': ['exact', ],
            'first_name': ['icontains', ],
            'last_name': ['exact', ],
            'date_joined': ['year', 'year__gt', 'year__lt', ],
                     'groups',
        }
        """
