from django.db import models
class IOT(models.Model):
    nom=models.CharField(max_length=20, blank=True)
    postion=models.CharField(max_length=70, blank=True)
    status=models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.nom + ' ' +self.postion

# Create your models here.


