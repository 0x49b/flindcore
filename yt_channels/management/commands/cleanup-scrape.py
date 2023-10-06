from django.core.management import BaseCommand

from yt_channels.models import ScrapeResult
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **options):
        answer = str(input("Do you really like to delete all ScrapeResults (y/n)?"))

        if answer == "y":
            srs = ScrapeResult.objects.all()
            for s in srs:
                print(f'removed {s.id}')
                s.delete()
        else:
            print(f'Ok I stop')
