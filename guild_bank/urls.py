from django.urls import path
from guild_bank.views import GuildBankView, BankUpdateView

urlpatterns = [
    path('', GuildBankView.as_view()),
    path('update/', BankUpdateView.as_view())
]
