from django.contrib import admin

from guild_bank.models import Bank, Character, Item, Scan, ScanItem


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    pass


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