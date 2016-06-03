"""Test model."""

from django.db import models


class CharModel(models.Model):
    """Test model."""

    field = models.CharField(max_length=10)
