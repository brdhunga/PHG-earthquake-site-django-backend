from django.db import models


class WhyUs(models.Model):
    '''
    Why us reasons on the front page 
    '''
    why_us = models.TextField(default='', blank=True)


