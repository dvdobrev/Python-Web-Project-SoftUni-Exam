from django import forms

from poker_app import poker
from poker_app.accounts import models
from poker_app.poker.models import Poker
from poker_app.web.helpers import BootstrapFormMixin


# UserModel = get_user_model()


class CreatePokerGameForm(forms.ModelForm, BootstrapFormMixin):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    #
    def save(self, commit=True):
        # commit false does not persist to database
        # just returns the object to be created
        poker = super().save(commit=False)

        poker.user = self.user
        if commit:
            poker.save()

        return poker

    # def form_valid(self, form):
    #     form.instance.owneeer_id = self.user.id
    #     return super().form_valid(form)

    class Meta:
        model = Poker
        exclude = ('user',)
        # exclude = ('user_id',)
        # exclude = ('owner_idd',)
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
        }


class EditPokerGameForm(forms.ModelForm, BootstrapFormMixin):

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self._init_bootstrap_form_controls()

    class Meta:
        model = Poker
        exclude = ('user',)

class DisabledFieldsFormMixin:
    pass


class DeletePokerGameForm(forms.ModelForm, BootstrapFormMixin, DisabledFieldsFormMixin):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self._init_bootstrap_form_controls()
    #     self._init_disabled_fields()

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Poker
        fields = ()
        # fields = "__all__"
