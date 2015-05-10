from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from django.template.defaultfilters import slugify


@python_2_unicode_compatible
class EventName(models.Model):
    name = models.CharField(max_length=500, blank=True, default='', unique=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Image(models.Model):
    '''
    A single Image
    '''
    url = models.URLField(blank=True, default='')
    caption = models.CharField(max_length=500, blank=True, default='')
    created_at = models.DateTimeField(editable=False, default=timezone.now())
    event = models.ManyToManyField(EventName, related_name="event_name")

    def __str__(self):        
        if self.caption:
            return self.url.split('/')[-1] +': ' + self.caption 
        return self.url

    def save(self, *args, **kwargs):
        '''
        update timestamps on save.
        '''
        if not self.pk:
            self.created_at = timezone.now()
        return super(Image, self).save(*args, **kwargs)


@python_2_unicode_compatible
class Event(models.Model):
    name = models.OneToOneField(EventName, related_name="main_event")
    images = models.ManyToManyField(Image, related_name='event_gallery')
    cover_image = models.URLField(blank=True, default='')
    created_at = models.DateTimeField(editable=False, default=timezone.now())
    description = models.TextField(blank=True, default='')
    slug = models.SlugField(blank=True, default='')
    
    def __str__(self):
        return self.name.name

    def save(self, *args, **kwargs):
        if not self.pk or self.slug == '':
            self.slug = slugify(self.name)
        return super(Event, self).save(*args, **kwargs)










