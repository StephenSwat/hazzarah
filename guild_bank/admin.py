from django.contrib import admin

from guild_bank.models import Bank, Character, Item, Scan, ScanItem, ItemCategory


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ("name", "bank")


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


class ScanItemInline(admin.TabularInline):
    raw_id_fields = ("item",)
    model = ScanItem


@admin.register(Scan)
class ScanAdmin(admin.ModelAdmin):
    list_display = ("id", "character", "created")

    inlines = [ScanItemInline]


@admin.register(ItemCategory)
class ItemCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)

