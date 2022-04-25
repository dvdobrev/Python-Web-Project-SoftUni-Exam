from django import forms

from poker_app.dice.models import Dice
from poker_app.web.helpers import BootstrapFormMixin


# UserModel = get_user_model()


class CreateDiceRoomForm(forms.ModelForm, BootstrapFormMixin):
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
        fields = '__all__'
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
        }


class EditDiceRoomForm(BootstrapFormMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Dice
        fields = '__all__'


class DisabledFieldsFormMixin:
    pass


class DeleteDiceRoomForm(forms.ModelForm, BootstrapFormMixin, DisabledFieldsFormMixin):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self._init_bootstrap_form_controls()
    #     self._init_disabled_fields()

    def save(self, commit=True):
        # dice = GameType.objects.all()
        # games.delete()
        self.instance.delete()
        return self.instance

    class Meta:
        model = Dice
        fields = ()
        # fields = "__all__"
