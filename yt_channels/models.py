from django.db import models


# Create your models here.
class Channel(models.Model):
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_created=True, auto_now_add=True)

    channel_id = models.CharField(max_length=25, null=False, blank=False)
    etag = models.CharField(max_length=30, blank=True, null=True)
    title = models.CharField(max_length=1024, blank=True, null=True)
    localized_title = models.CharField(max_length=1024, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    published_at = models.DateTimeField(null=True, blank=True)
    thumbnail = models.URLField(blank=True, null=True)
    related_playlists = models.CharField(max_length=25, blank=True, null=True)


class ChannelStatistics(models.Model):
    channel = models.OneToOneField(Channel, on_delete=models.CASCADE, primary_key=True)
    created = models.DateTimeField(auto_created=True, auto_now_add=True)
    view_count = models.BigIntegerField()
    subscriber_count = models.BigIntegerField()
    hidden_subscriber_count = models.BooleanField(default=False)
    video_count = models.BigIntegerField()


class TopicCategories(models.Model):
    channel_statistics = models.ManyToOneRel(ChannelStatistics,
                                             on_delete=models.DO_NOTHING,
                                             field_name='channel_statistics',
                                             to=ChannelStatistics)
    url = models.URLField()


class ScrapeResult(models.Model):
    created_at = models.DateTimeField(auto_created=True, auto_now_add=True)
    channel_id = models.CharField(max_length=30)
    raw_json = models.TextField()
