import random

from django.db import models
from django.utils import timezone

from accounts.models import User


class Incident(models.Model):
    INCIDENT_STATUS_CHOICES = (
        ("Open", "Open"),
        ("In Progress", "In Progress"),
        ("Closed", "Closed"),
    )

    PRIORITY_CHOICES = (
        ("High", "High"),
        ("Medium", "Medium"),
        ("Low", "Low"),
    )

    incident_id = models.CharField(
        primary_key=True, max_length=20, editable=False, unique=True
    )
    reporter = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="incidents"
    )
    incident_details = models.TextField()
    reported_date = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    status = models.CharField(
        max_length=20, choices=INCIDENT_STATUS_CHOICES, default="Open"
    )

    def save(self, *args, **kwargs):
        if not self.incident_id:
            # This will ensure that the id that is being generated is unique
            # If not it would regenerate another id.
            while True:
                random_number = str(random.randint(10000, 99999))
                current_year = timezone.now().year
                incident_id = f"RMG{random_number}{current_year}"
                if not Incident.objects.filter(incident_id=incident_id).exists():
                    self.incident_id = incident_id
                    break
        super().save(*args, **kwargs)

    def __str__(self):
        return self.pk
