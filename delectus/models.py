from django.db import models

class Tape(models.Model):
    AUDIO_CHOICES = (
    	('silent', 'Silent'),
        ('mono', 'Mono'),
        ('stereo', 'Stereo'),
        ('surround', 'Surround')
    )
    COLOR_CHOICES = (
        ('color', 'Color'),
        ('bw', 'B/W')
    )
    title = models.CharField(max_length=200)
    alertnate_title = models.CharField(max_length=200, blank=True)
    date = models.CharField(max_length=200, blank=True)
    hours = models.IntegerField(blank=True)
    minutes = models.IntegerField(blank=True)
    seconds = models.IntegerField(blank=True)
    country = models.CharField(max_length=200, blank=True)
    format = models.CharField(max_length=200, blank=True)
    color = models.CharField(max_length=50, blank=True, choices=COLOR_CHOICES)
    audio = models.CharField(max_length=50, blank=True, choices=AUDIO_CHOICES)
    keywords = models.TextField(blank=True)