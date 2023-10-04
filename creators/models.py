from django.db import models


class CreatorMeta(models.Model):
    subscriber_count = models.IntegerField()


class Creator(models.Model):
    name = models.CharField(max_length=1024, blank=False, null=False)
    yt_url = models.URLField(blank=False, null=False)
    yt_scrape = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class CreatorUsername(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE, related_name='usernames')
    username = models.CharField(max_length=1024)

    def __str__(self):
        return self.username
