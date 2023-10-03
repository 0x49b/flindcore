import logging

from django.conf import settings
from pyyoutube import Client

from flind_core.celery import app
from yt_channels.models import Channel, ScrapeResult

logger = logging.getLogger(__name__)


@app.task
def collect_youtube_stats():
    youtube = Client(api_key=settings.YT_API_KEY)

    channel_list = Channel.objects.all()

    for c in channel_list:
        channel = youtube.channels.list(channel_id=c.channel_id, return_json=True)

        sr = ScrapeResult()
        sr.channel_id = c.channel_id
        sr.raw_json = channel
        sr.save()
