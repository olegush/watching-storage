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
        username = self.passcard.owner_name
        if self.leaved_at:
            return f'{username} entered at {self.entered_at} {self.leaved_at}'
        return f'{username} entered at {self.entered_at} not leaved'

    def duration(self):
        if self.leaved_at:
            return self.leaved_at - self.entered_at
        else:
            return timezone.now().replace(microsecond=0) - self.entered_at

    def is_strange_visit(self):
        if self.leaved_at:
            return (self.leaved_at - self.entered_at).seconds > LONG_VISIT
        else:
            return (timezone.now().replace(microsecond=0) - self.entered_at).seconds > LONG_VISIT
