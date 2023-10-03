from celery import shared_task
from flind_core.celery import app
from bs4 import BeautifulSoup

from infrastructure.models import Proxy
from datetime import datetime, timedelta
import requests
import logging

logger = logging.getLogger(__name__)


@app.task
def scrape_proxies():
    url = "https://www.sslproxies.org"

    page = requests.get(url)
    soup = BeautifulSoup(page.content, features="html.parser")

    table = soup.find('table')
    tbody = table.find('tbody')

    tabledata = table_data_text(tbody)

    for d in tabledata:
        try:
            proxy_check = Proxy.objects.get(ip_address=d[0])
            proxy_check.last_checked = transform_last_seen(d[7])
            proxy_check.save()
            logger.info(f'Updated proxy {proxy_check.ip_address}')
        except Proxy.DoesNotExist:
            proxy = Proxy()
            proxy.ip_address = d[0]
            proxy.port = d[1]
            proxy.code = d[2]
            proxy.country = d[3]
            proxy.anonimity = d[4]
            proxy.google = True if d[5] == 'yes' else False
            proxy.https = True if d[6] == 'yes' else False
            proxy.last_checked = transform_last_seen(d[7])
            proxy.save()
            logger.info(f'saved new proxy {proxy.ip_address}')


def transform_last_seen(datestring):
    ds = datestring.split()[:-1]
    current_datetime = datetime.now()
    duration = timedelta()

    if len(ds) == 4:
        val1 = ds[0]
        val2 = ds[2]
        duration = timedelta(hours=int(val1), minutes=int(val2))

    if len(ds) == 2:
        val = ds[0]
        key = ds[1]

        if key == 'hours' or key == 'hour':
            duration = timedelta(hours=int(val))
        elif key == 'mins':
            duration = timedelta(minutes=int(val))
        elif key == 'secs':
            duration = timedelta(seconds=int(val))
        else:
            raise KeyError

    return current_datetime - duration


def table_data_text(table):
    """Parses a html segment started with tag <table> followed
    by multiple <tr> (table rows) and inner <td> (table data) tags.
    It returns a list of rows with inner columns.
    Accepts only one <th> (table header/data) in the first row.
    """

    def rowgetDataText(tr, coltag='td'):  # td (data) or th (header)
        return [td.get_text(strip=True) for td in tr.find_all(coltag)]

    rows = []
    trs = table.find_all('tr')
    headerow = rowgetDataText(trs[0], 'th')
    if headerow:  # if there is a header row include first
        rows.append(headerow)
        trs = trs[1:]
    for tr in trs:  # for every table row
        rows.append(rowgetDataText(tr, 'td'))  # data row
    return rows
