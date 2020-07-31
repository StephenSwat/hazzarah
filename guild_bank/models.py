from django.db import models


class Item(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)


class Character(models.Model):
    name = models.CharField(max_length=30, unique=True)


class Scan(models.Model):
    character = models.ForeignKey(Character, models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)


class ScanItem(models.Model):
    scan = models.ForeignKey(Scan, models.CASCADE)
    item = models.ForeignKey(Item, models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        unique_together = ('scan', 'item',)