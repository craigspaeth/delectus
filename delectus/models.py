from django.db import models

class Tape(models.Model):
    title = models.CharField(max_length=200)