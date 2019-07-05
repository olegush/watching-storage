from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.filter(passcode=passcode)[0]
    visits = Visit.objects.filter(passcard=passcard).order_by('-entered_at')
    visits_formatted = [{
        'entered_at': visit.entered_at,
        'duration': visit.get_duration(),
        'is_strange': visit.get_duration().seconds > visit.LONG_VISIT
    } for visit in visits]
    context = {
        'passcard': passcard,
        'this_passcard_visits': visits_formatted
    }
    return render(request, 'passcard_info.html', context)
