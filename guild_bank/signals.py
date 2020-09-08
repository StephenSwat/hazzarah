from django.db.models.signals import post_save
from django.dispatch import receiver

import discord_webhook

from guild_bank.models import Scan


@receiver(post_save, sender=Scan)
def send_discord_embed(sender, instance, created, **kwargs):
    if not created:
        return

    webhook = discord_webhook.DiscordWebhook(
        url="https://discord.com/api/webhooks/745225644576866305/Y_1AfnQWxlfAaV49ejZn9SHQuaxFQHwThmsXK4SqAcM2rL5oZEr_m2UpixglXuor3xaD"
    )
    embed = discord_webhook.DiscordEmbed(
        title='Guild bank updated',
        description='The guild bank contents for the character {} were just updated.'.format(instance.character.name),
        color=997000
    )
    embed.set_author(
        name='Bridgehill guild gank',
        url="https://bridgehill.site/bank/",
        icon_url="https://cdn.discordapp.com/icons/618342890049110017/69fe53efcc512a6b43245baffc2df0ff.png?size=256"
    )
    embed.set_timestamp()
    embed.set_url("https://bridgehill.site/bank/")
    embed.set_thumbnail(url="https://cdn.discordapp.com/icons/618342890049110017/69fe53efcc512a6b43245baffc2df0ff.png?size=256")
    webhook.add_embed(embed)
    webhook.execute()