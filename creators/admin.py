from django.contrib import admin
from .models import Creator, CreatorMeta


# Register your models here.
@admin.register(Creator)
class CreatorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Creator._meta.get_fields()]


@admin.register(CreatorMeta)
class CreatorMetaAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CreatorMeta._meta.get_fields()]
