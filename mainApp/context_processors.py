from .models import *

def davlatlar(request):
    davlatlar_chap = Davlat.objects.all()[:6]
    davlatlar_ong = Davlat.objects.all()[6:11]
    other_clubs = Club.objects.filter(id__in=Davlat.objects.filter(id__gt=11)).values_list('id', flat=True)
    context = {
        'davlatlar_chap':davlatlar_chap,
        'davlatlar_ong':davlatlar_ong,
        'other_clubs': other_clubs,
    }
    return context