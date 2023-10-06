from django.db import models


# Create your models here.
class Channel(models.Model):
    class Meta:
        verbose_name = 'Channel'
        verbose_name_plural = 'Channels'

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

    def __str__(self):
        return f'{self.title if self.title != None else ""} {self.channel_id}'


class ChannelStatistics(models.Model):
    class Meta:
        verbose_name = "Channel Statistic"
        verbose_name_plural = "Channel Statistics"

    channel = models.OneToOneField(Channel, on_delete=models.CASCADE, primary_key=True)
    created = models.DateTimeField(auto_created=True, auto_now_add=True)
    view_count = models.BigIntegerField()
    subscriber_count = models.BigIntegerField()
    hidden_subscriber_count = models.BooleanField(default=False)
    video_count = models.BigIntegerField()


class TopicCategories(models.Model):
    class Meta:
        verbose_name = "Topic Category"
        verbose_name_plural = "Topic Categories"

    channel_statistics = models.ManyToOneRel(ChannelStatistics,
                                             on_delete=models.DO_NOTHING,
                                             field_name='channel_statistics',
                                             to=ChannelStatistics)
    url = models.URLField()


class ScrapeResult(models.Model):
    class Meta:
        verbose_name = "Scrape Result"
        verbose_name_plural = "Scrape Results"

    created_at = models.DateTimeField(auto_created=True, auto_now_add=True)
    channel_id = models.CharField(max_length=30)
    raw_json = models.TextField()

    def __str__(self):
        return self.channel_id
