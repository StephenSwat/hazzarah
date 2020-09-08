from django.apps import AppConfig


class GuildBankConfig(AppConfig):
    name = 'guild_bank'

    def ready(self):
        import guild_bank.signals