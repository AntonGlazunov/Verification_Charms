from django.contrib import admin

from charm.models import Fluke, Charm, Muster


@admin.register(Fluke)
class FlukeAdmin(admin.ModelAdmin):
    list_display = ('serial_number', 'IP')

@admin.register(Charm)
class CharmAdmin(admin.ModelAdmin):
    serial_number = ('id', 'username')

@admin.register(Muster)
class MusterAdmin(admin.ModelAdmin):
    list_display = ('fluke', 'charm')