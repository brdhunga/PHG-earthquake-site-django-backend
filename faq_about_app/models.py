from django.db import models


class FAQApp(models.Model):
    '''
    This model is for the FAQ on the front page
    '''
    question = models.CharField(max_length=400, blank=True, default='')
    answer = models.TextField(blank=True, default = '')


class AboutUs(models.Model):
    '''
    The about us on the front page 
    '''
    about_us = models.TextField(blank = True, default='')





