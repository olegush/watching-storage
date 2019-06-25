from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone


LONG_VISIT = 60 * 60


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.filter(passcode=passcode)[0]
    visits = Visit.objects.filter(passcard=passcard)
    visits_formatted = [{
        'entered_at': visit.entered_at,
        'duration': visit.leaved_at - visit.entered_at,
        "is_strange": (visit.leaved_at - visit.entered_at).seconds > LONG_VISIT
    } for visit in visits if visit.leaved_at]
    context = {
        "passcard": passcard,
        "this_passcard_visits": visits_formatted
    }
    return render(request, 'passcard_info.html', context)
