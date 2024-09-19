from django.db import models
from django.contrib.auth.models import User


class Files(models.Model):
    file = models.FileField(upload_to='files/')
    name = models.CharField(max_length=100, default='')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='uploaded_files', on_delete=models.CASCADE)
    patient = models.ForeignKey(User, related_name='patient_files', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class PDF(models.Model):
    text = models.TextField()   
    file = models.ForeignKey(Files, related_name='read_pdf', on_delete=models.CASCADE)

    def __str__(self):
        return self.file.name
