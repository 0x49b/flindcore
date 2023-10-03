from django.db import models


# Create your models here.
class Proxy(models.Model):
    class Meta:
        verbose_name = 'Proxy'
        verbose_name_plural = 'Proxies'

    ip_address = models.GenericIPAddressField(unique=True, verbose_name='IP Address')
    port = models.IntegerField()
    code = models.CharField(max_length=3)
    country = models.CharField(max_length=256)
    anonimity = models.CharField(max_length=256)
    google = models.BooleanField(default=False)
    https = models.BooleanField(default=False, verbose_name='HTTPS')
    last_checked = models.DateTimeField()
