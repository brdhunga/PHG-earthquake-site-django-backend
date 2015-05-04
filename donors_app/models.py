from django.db import models

from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Donors(models.Model):
    '''
    List of all donors 
    '''
    name = models.CharField(max_length=300, blank=True, default='')
    contribution = models.DecimalField(max_digits=7, decimal_places=2, blank=True, default=0.00)

    def __str__(self):
        return self.name 




