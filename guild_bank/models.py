from django.db import models


class Bank(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class ItemCategory(models.Model):
    name = models.CharField(max_length=60)

    class Meta:
        verbose_name_plural = "item categories"


class Item(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    category = models.ForeignKey(ItemCategory, models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=30, unique=True)
    bank = models.ForeignKey(Bank, models.CASCADE)

    def last_update(self):
        return self.scan_set.latest('created').created

    def __str__(self):
        return self.name


class Scan(models.Model):
    character = models.ForeignKey(Character, models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


class ScanItem(models.Model):
    scan = models.ForeignKey(Scan, models.CASCADE)
    item = models.ForeignKey(Item, models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        unique_together = ('scan', 'item',)