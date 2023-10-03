from django.db import models


# Create your models here
class Creator(models.Model):
    name = models.CharField(max_length=1024, blank=False, null=False)
    yt_url = models.URLField(blank=False, null=False)
    yt_scrape = models.BooleanField(default=True)


class CreatorUsername(models.Model):
    creator = models.ManyToOneRel(Creator, field_name='creator', to=Creator, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=1024)


class CreatorMeta(models.Model):
    subscriber_count = models.IntegerField()
