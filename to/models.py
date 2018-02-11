from django.db import models
from unittest.util import _MAX_LENGTH

# Create your models here.


class List(models.Model):
    text = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
    

