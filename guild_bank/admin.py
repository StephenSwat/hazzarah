from django.contrib import admin

from guild_bank.models import Character, Item, Scan, ScanItem

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    pass


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(Scan)
class ScanAdmin(admin.ModelAdmin):
    pass


@admin.register(ScanItem)
class ScanItemAdmin(admin.ModelAdmin):
    pass