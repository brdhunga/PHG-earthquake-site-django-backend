import datetime

from django.db import models
from django.template.defaultfilters import slugify
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Progress(models.Model):
    '''
    Progress report.    
    '''
    title = models.CharField(max_length=400, blank=True, default='')
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()
    summary = models.TextField(blank=True, default='')
    content = models.TextField(blank=True, default='')
    slug = models.CharField(max_length=60, blank=True, default='', unique=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        '''
        update timestamps on save.
        auto_now and auto_now_add are bad. implementing in save method
        '''
        if not self.pk or self.slug=='':
            self.created_at = datetime.datetime.today()
            self.slug = slugify(self.title)
        self.updated_at = datetime.datetime.today() 
        return super(Progress, self).save(*args, **kwargs)






