from django.views.generic.base import TemplateView
from guild_bank.models import Bank, Scan, ScanItem


class GuildBankView(TemplateView):
    template_name = "guild_bank/bank.html"

    def get_context_data(self, **kwargs):
        bank = Bank.objects.get()
        scans = [c.scan_set.latest("created") for c in bank.character_set.all()]
        items = ScanItem.objects.filter(scan__in=scans)

        return {
            'bank': bank,
            'items': items
        }