from datetime import datetime

from django.shortcuts import render
from django.utils import timezone

from datacenter.models import Passcard
from datacenter.models import Visit


def storage_information_view(request):
    non_closed_visits = Visit.objects.filter(leaved_at=None).order_by('-entered_at')
    non_closed_visits_formatted = [{
        'who_entered':visit.passcard.owner_name,
        'passcode':visit.passcard.passcode,
        'entered_at': timezone.localtime(visit.entered_at),
        'duration': visit.duration(),
        'is_strange': visit.is_strange_visit()
        } for visit in non_closed_visits]
    context = {
        'non_closed_visits': non_closed_visits_formatted,
    }
    return render(request, 'storage_information.html', context)
