from django.contrib import admin
from .models import Creator, CreatorMeta, CreatorUsername


# Register your models here.
@admin.register(Creator)
class CreatorAdmin(admin.ModelAdmin):
    list_display = ('name', 'yt_scrape')
    list_filter = ('yt_scrape', )


@admin.register(CreatorUsername)
class CreatorUsernameAdmin(admin.ModelAdmin):
    list_display = ('username', 'creator')
    search_fields = ('username', 'creator')


@admin.register(CreatorMeta)
class CreatorMetaAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CreatorMeta._meta.get_fields()]
