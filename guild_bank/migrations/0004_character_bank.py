from django.db import migrations, models
import django.db.models.deletion


def create_dummy_bank(apps, schema_editor):
    Bank = apps.get_model("guild_bank", "Bank")
    Character = apps.get_model("guild_bank", "Character")
    db_alias = schema_editor.connection.alias

    dummy_bank = Bank(name="DUMMY BANK")
    dummy_bank.save()

    for x in Character.objects.all():
        x.bank = dummy_bank
        x.save()


def delete_dummy_bank(apps, schema_editor):
    Bank = apps.get_model("guild_bank", "Bank")
    Bank.objects.get(name="DUMMY BANK").delete()


class Migration(migrations.Migration):

    dependencies = [
        ('guild_bank', '0003_add_bank_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='bank',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='guild_bank.Bank'),
        ),
        migrations.RunPython(create_dummy_bank, delete_dummy_bank),
        migrations.AlterField(
            model_name='character',
            name='bank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guild_bank.Bank'),
        ),
    ]
