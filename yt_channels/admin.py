from django.contrib import admin
from .models import Channel, ChannelStatistics, TopicCategories, ScrapeResult


# Register your models here.
class ChannelAdmin(admin.ModelAdmin):
    list_display = ('channel_id','title', 'etag', 'localized_title', 'description', 'published_at', 'created', 'updated')


class ChannelStatisticsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ChannelStatistics._meta.get_fields()]


class TopicCategoriesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in TopicCategories._meta.get_fields()]


class ScrapeResultAdmin(admin.ModelAdmin):
    list_display = ('channel_id', 'created_at',)


admin.site.register(Channel, ChannelAdmin)
admin.site.register(ChannelStatistics, ChannelStatisticsAdmin)
admin.site.register(TopicCategories, TopicCategoriesAdmin)
admin.site.register(ScrapeResult, ScrapeResultAdmin)
