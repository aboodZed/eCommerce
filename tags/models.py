from django.db import models

# Create your models here.
class Tag(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, unique=True, editable=False)
    name = models.CharField(max_length=100)

class ProductTag(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, unique=True, editable=False)
    product = models.ForeignKey('store.Product', on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
