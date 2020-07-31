from django.urls import path
from guild_bank.views import GuildBankView

urlpatterns = [
    path('', GuildBankView.as_view()),
]
