from django.views.generic.base import TemplateView
from guild_bank.models import Bank, ScanItem


class GuildBankView(TemplateView):
    template_name = "guild_bank/bank.html"

    def get_context_data(self, **kwargs):
        bank = Bank.objects.get()
        items = ScanItem.objects.filter(scan__character__bank=bank)

        return {
            'bank': bank,
            'items': items
        }