from django.views.generic.base import TemplateView
from guild_bank.models import Scan


class GuildBankView(TemplateView):
    template_name = "guild_bank/bank.html"

    def get_context_data(self, **kwargs):
        return {'scan': Scan.objects.latest("created")}