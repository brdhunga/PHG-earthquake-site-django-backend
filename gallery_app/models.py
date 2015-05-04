from django.db import models
from django.utils.encoding import python_2_unicode_comptible


@python_2_unicode_comptible
class Image(models.Model):
    '''
    A single Image
    '''
    url = models.URLField(blank=True, default='')
    caption = models.CharField(max_length=500, blank=True, default='')

    def __str__(self):
        return self.caption




