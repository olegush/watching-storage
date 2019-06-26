from django.db import models
from django.utils import timezone

LONG_VISIT = 60 * 60

class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved= 'leaved at ' + str(self.leaved_at) if self.leaved_at else 'not leaved'
        )

    def duration(self):
        if self.leaved_at is not None:
            return self.leaved_at - self.entered_at
        else:
            return timezone.now().replace(microsecond=0) - self.entered_at

    def is_strange_visit(self):
        if self.leaved_at is not None:
            return (self.leaved_at - self.entered_at).seconds > LONG_VISIT
        else:
            return (timezone.now().replace(microsecond=0) - self.entered_at).seconds > LONG_VISIT
