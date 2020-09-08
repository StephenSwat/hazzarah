import collections
import base64

from django.db import transaction

from guild_bank.models import Scan, ScanItem


def parse_item(item):
    q = item[1:-1]
    _, _, item_id, quantity = q.split(",")

    return int(item_id), int(quantity)


def decode_cgb_string(b64):
    dec = base64.b64decode(b64).decode("ASCII")

    raw_money, _, *items_raw = dec.split(";")
    money = int(raw_money.split(",")[1])
    items = collections.defaultdict(int)

    for x in items_raw:
        if not x:
            continue

        item_id, quantity = parse_item(x)
        items[item_id] += quantity

    return money, dict(items)
