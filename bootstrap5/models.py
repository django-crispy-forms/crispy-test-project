from django.db import models

# Create your models here.
class WithFileField(models.Model):
    my_file = models.FileField(null=True, blank=True, help_text="help")
    my_char = models.CharField(null=True, blank=True, help_text="help", max_length=32)
