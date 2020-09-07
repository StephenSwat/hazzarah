from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.db import transaction

from guild_bank.models import Bank, Scan, ScanItem
from guild_bank.forms import BankUpdateForm


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


class BankUpdateView(FormView):
    template_name = 'guild_bank/update.html'
    form_class = BankUpdateForm
    success_url = '/bank/'

    def form_valid(self, form):
        with transaction.atomic():
            scan = Scan.objects.create(character=form.cleaned_data['character'])

            for item, count in form.cleaned_data['encoded'].items():
                ScanItem.objects.create(scan=scan, item_id=item, quantity=count)

        return super().form_valid(form)