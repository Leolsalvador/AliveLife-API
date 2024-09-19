from django.db import models
from django.contrib.auth.models import User


class Diagnosis(models.Model):
    diagnosis = models.TextField()
    Medical = models.ForeignKey(User, related_name='medical', on_delete=models.CASCADE)
    patient = models.ForeignKey(User, related_name='patient', on_delete=models.CASCADE)
    pdf = models.ForeignKey('pdf.PDF', on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.diagnosis
