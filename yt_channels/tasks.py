import json
import logging

from django.conf import settings
from pyyoutube import Client

from flind_core.celery import app
from yt_channels.models import Channel, ScrapeResult
from django.db import close_old_connections

logger = logging.getLogger(__name__)


@app.task
def collect_youtube_stats():
    youtube = Client(api_key=settings.YT_API_KEY)

    channel_list = Channel.objects.all()

    for c in channel_list:
        logger.info(f'Now reading {c.channel_id}')
        channel = youtube.channels.list(channel_id=c.channel_id, return_json=True)

        sr = ScrapeResult()
        sr.channel_id = c.channel_id
        sr.raw_json = json.dumps(channel)
        sr.save()
        close_old_connections()


@app.task(name='yt-scrape-result-transformer')
def read_scrape_result():
    logger.info("Running Youutbe Scrape Data transformer")
    close_old_connections()
    scrapeResult = ScrapeResult.objects.all().order_by('created_at')

    for sc in scrapeResult:
        logger.info(f'{sc.channel_id} -> {sc.created_at} parsing')
        cjson = json.loads(sc.raw_json)

        try:
            channel = Channel.objects.get(channel_id=cjson['items'][0]['id'])
            channel.title = cjson['items'][0]['snippet']['title']
            channel.etag = cjson['items'][0]['etag']
            channel.localized_title = cjson['items'][0]['snippet']['localized']['title']
            channel.description = cjson['items'][0]['snippet']['description']
            channel.save()

            logger.info("CHANNEL EXISTS  DO SOME STUFF!!")
        except Channel.DoesNotExist:
            logger.error("CHANNEL DOES NOT EXIST")
