from django import forms

from poker_app.roulette.models import Roulette
from poker_app.web.helpers import BootstrapFormMixin


class CreateRouletteForm(forms.ModelForm, BootstrapFormMixin):
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
        fields = '__all__'
        # widgets = {
        #     'name': forms.TextInput(
        #         attrs={
        #             'placeholder': 'Enter room name',
        #         }
        #     ),
        #
        #     'max_players': forms.TextInput(
        #         attrs={
        #             'placeholder': 'Enter max players',
        #         }
        #     ),
        # }


class EditRouletteForm(BootstrapFormMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Roulette
        fields = '__all__'


class DisabledFieldsFormMixin:
    pass


class DeleteRouletteForm(forms.ModelForm, BootstrapFormMixin, DisabledFieldsFormMixin):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self._init_bootstrap_form_controls()
    #     self._init_disabled_fields()

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Roulette
        fields = ()
        # fields = "__all__"
