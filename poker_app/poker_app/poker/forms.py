from django import forms

from poker_app.poker.models import Poker
from poker_app.web.helpers import BootstrapFormMixin


class CreatePokerGameForm(forms.ModelForm, BootstrapFormMixin):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        # commit false does not persist to database
        # just returns the object to be created
        poker = super().save(commit=False)

        poker.user = self.user
        if commit:
            poker.save()

        return poker

    class Meta:
        model = Poker
        exclude = ('user', )

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Game Name',
                }
            ),

            'max_players': forms.TextInput(
                attrs={
                    'placeholder': 'Enter max players',
                }
            ),

            'min_bet': forms.TextInput(
                attrs={
                    'placeholder': 'Enter min bet for the game',
                }
            ),

            'max_bet': forms.TextInput(
                attrs={
                    'placeholder': 'Enter max bet for the game',
                }
            ),

            # 'game_types': forms.TextInput(
            #     attrs={
            #         'placeholder': 'Choose your game type',
            #     }
            # ),
        }


class EditPokerGameForm(forms.ModelForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Poker
        exclude = ('user',)


class DisabledFieldsFormMixin:
    pass


class DeletePokerGameForm(forms.ModelForm, BootstrapFormMixin):

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Poker
        fields = ()
