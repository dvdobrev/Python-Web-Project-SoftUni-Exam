from django import forms

from poker_app.roulette.models import Roulette
from poker_app.web.helpers import BootstrapFormMixin


class CreateRouletteRoomForm(forms.ModelForm, BootstrapFormMixin):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        # commit false does not persist to database
        # just returns the object to be created
        roulette = super().save(commit=False)

        roulette.user = self.user
        if commit:
            roulette.save()

        return roulette

    class Meta:
        model = Roulette
        exclude = ('user',)
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter game name',
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


class EditRouletteRoomForm(BootstrapFormMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Roulette
        exclude = ('user',)


class DeleteRouletteRoomForm(forms.ModelForm, BootstrapFormMixin):

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Roulette
        fields = ()
