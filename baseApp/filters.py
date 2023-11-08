import django_filters
from .models import Games
from django import forms

genre_choices = (
    (0, 'Action'),
    (1, 'Adventure'),
    (2, 'Simulation')
)

class GenreFilter(django_filters.FilterSet):

    genres = django_filters.MultipleChoiceFilter(
        label = 'Genre filter',
        choices = genre_choices,
        conjoined = True,
        widget=forms.CheckboxSelectMultiple
    )