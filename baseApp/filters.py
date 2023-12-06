import django_filters
from .models import Games
from django import forms


def getDistinctList():
    genreset = set([])
    genrelist = []
    genrefield = ' '.join([str(x) for x in Games.objects.values_list('genres')])
    
    removechar = ['(', '"', ')', '[', ']', ',']
    for char in removechar:
        genrefield = genrefield.replace(char, '')

    genreclean = genrefield.split("'")[1::2]
    for x in genreclean:
        genreset.add(x)
        if "" in genreset:
            genreset.remove("")
    for x in (genreset):
        if x not in genrelist:
            genrelist.append((x, x))
    genrelist.sort()
    return genrelist
    
class GenreFilter(django_filters.FilterSet):
    genres = django_filters.MultipleChoiceFilter(
        label = 'Genre filter',
        lookup_expr = 'icontains',
        choices = getDistinctList(),
        conjoined = True,
        widget = forms.CheckboxSelectMultiple
    )
    class Meta:
        widgets = {
            
        }

# genre_list = [
#             ('Adventure', 'Adventure'),
#             ('Arcade', 'Aracade'),
#             ('Brawler', 'Brawler'),
#             ('Card & Board Game', 'Card & Board Game'),
#             ('Fighting', 'Fighting'),
#             ('Indie', 'Indie'),
#             ('MOBA', 'MOBA'),
#             ('Music', 'Music'),
#             ('Platform', 'Platform'),
#             ('Point-and-Click', 'Point-and-Click'),
#             ('Puzzle', 'Puzzle'),
#             ('Pinball', 'Pinball'),
#             ('Racing', 'Racing'),
#             ('Real Time Strategy', 'Real Time Strategy'),
#             ('RPG', 'RPG'),
#             ('Shooter', 'Shooter'),
#             ('Simulator', 'Simulator'),
#             ('Sport', 'Sport'),
#             ('Strategy', 'Strategy'),
#             ('Tactical', 'Tactical'),
#             ('Turn Based Strategy', 'Turn Based Strategy'),
#             ('Quiz/Trivia', 'Quiz/Trivia'),
#             ('Visual Novel', 'Visual Novel')
# ]
