from django import forms
from django.core.exceptions import ValidationError

from guild_bank.models import Character
from guild_bank.utils import decode_cgb_string


class CGBField(forms.CharField):
    def clean(self, value):
        try:
            return decode_cgb_string(value)
        except:
            raise ValidationError('Not a valid CGB string.')


class BankUpdateForm(forms.Form):
    character = forms.ModelChoiceField(Character.objects)
    encoded = CGBField(widget=forms.Textarea)
