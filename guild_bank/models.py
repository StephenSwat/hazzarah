from django.db import models


class Bank(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=30, unique=True)
    bank = models.ForeignKey(Bank, models.CASCADE)

    def __str__(self):
        return self.name


class Scan(models.Model):
    character = models.ForeignKey(Character, models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)


class ScanItem(models.Model):
    scan = models.ForeignKey(Scan, models.CASCADE)
    item = models.ForeignKey(Item, models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        unique_together = ('scan', 'item',)