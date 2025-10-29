from django.db import models

# Create your models here.
class Tag(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, unique=True, editable=False)
    name = models.CharField(max_length=100)