from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone


LONG_VISIT = 60 * 60


def duration(leaved_at, entered_at):
    if leaved_at is not None:
        return leaved_at - entered_at
    else:
        return timezone.now().replace(microsecond=0) - entered_at


def is_strange_visit(leaved_at, entered_at):
    if leaved_at is not None:
        return (leaved_at - entered_at).seconds > LONG_VISIT
    else:
        return (timezone.now().replace(microsecond=0) - entered_at).seconds > LONG_VISIT


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.filter(passcode=passcode)[0]
    visits = Visit.objects.filter(passcard=passcard).order_by('-entered_at')
    visits_formatted = [{
        'entered_at': visit.entered_at,
        'duration': duration(visit.leaved_at, visit.entered_at),
        'is_strange': is_strange_visit(visit.leaved_at, visit.entered_at)
    } for visit in visits]
    context = {
        'passcard': passcard,
        'this_passcard_visits': visits_formatted
    }
    return render(request, 'passcard_info.html', context)
