from django import forms

from poker_app.dice.models import Dice
from poker_app.web.helpers import BootstrapFormMixin


class CreateDiceGameForm(forms.ModelForm, BootstrapFormMixin):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        # commit false does not persist to database
        # just returns the object to be created
        dice = super().save(commit=False)

        dice.user = self.user
        if commit:
            dice.save()

        return dice

    class Meta:
        model = Dice
        exclude = ('user',)
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter room name',
                }
            ),

            'max_players': forms.TextInput(
                attrs={
                    'placeholder': 'Enter max players',
                }
            ),

            'min_bet': forms.TextInput(
                attrs={
                    'placeholder': 'Enter min bet',
                }
            ),

            'max_bet': forms.TextInput(
                attrs={
                    'placeholder': 'Enter max bet',
                }
            ),
        }


class EditDiceGameForm(BootstrapFormMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Dice
        exclude = ('user',)


class DeleteDiceGameForm(forms.ModelForm):

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Dice
        fields = ()
