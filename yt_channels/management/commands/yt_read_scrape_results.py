import logging

from django.core.management import BaseCommand

from yt_channels import tasks

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **options):
        tasks.read_scrape_result()
