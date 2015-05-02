from django.db import models


class WebsiteSettings(models.Model):
    site_title = models.TextField(blank=True, default="")
    site_description = models.TextField(blank = True, default = "")


