from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.filter(passcode=passcode)[0]
    visits = Visit.objects.filter(passcard=passcard).order_by('-entered_at')
    visits_formatted = [{
        'entered_at': visit.entered_at,
        'duration': Visit.duration(visit),
        'is_strange': Visit.is_strange_visit(visit)
    } for visit in visits]
    context = {
        'passcard': passcard,
        'this_passcard_visits': visits_formatted
    }
    return render(request, 'passcard_info.html', context)
