from django.conf import settings
from pyyoutube import Client
from django.core.management.base import BaseCommand, CommandError
from yt_channels.models import Channel, ChannelStatistics, TopicCategories, ScrapeResult


class Command(BaseCommand):

    def handle(self, *args, **options):
        youtube = Client(api_key=settings.YT_API_KEY)

        channel_list = Channel.objects.all()

        for c in channel_list:
            channel = youtube.channels.list(channel_id=c.channel_id, return_json=True)

            sr = ScrapeResult()
            sr.channel_id = c.channel_id
            sr.raw_json = channel
            sr.save()
