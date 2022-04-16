from django_filters import FilterSet, DateFilter
from .models import *
from django.forms import DateInput


class PostFilter(FilterSet):
    dateCreation = DateFilter(
        lookup_expr='gt',
        widget=DateInput(
            attrs={
                'type': 'date'
            }
        )
    )

    class Meta:
        model = Post
        fields = ('dateCreation', 'author', 'categoryType')
