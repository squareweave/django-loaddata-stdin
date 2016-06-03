from django.db import models


class CharModel(models.Model):
    field = models.CharField(max_length=10)
