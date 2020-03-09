from django.db import models

# Create your models here.
class WithFileField(models.Model):
    my_file = models.FileField(null=True, blank=True)
