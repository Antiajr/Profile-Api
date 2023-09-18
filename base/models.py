from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    age = models.IntegerField(max_length=2, null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name