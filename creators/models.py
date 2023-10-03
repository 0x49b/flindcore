from django.db import models


# Create your models here
class Creator(models.Model):
    name = models.CharField(max_length=1024, blank=False, null=False)
    yt_url = models.URLField(blank=False, null=False)
    yt_scrape = models.BooleanField(default=True)


class CreatorMeta(models.Model):
    subscriber_count = models.IntegerField()
