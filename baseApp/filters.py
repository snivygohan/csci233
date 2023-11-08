import django_filters
from .models import Games

genre_choices = (('Action'))

class GenreFilter(django_filters.FilterSet):

    genre = django_filters.MultipleChoiceFilter(choices=genre_choices, conjoined = True)

    class Meta:
        model = Games
        fields = ['genres']