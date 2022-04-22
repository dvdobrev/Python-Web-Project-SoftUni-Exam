from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

from poker_app.accounts.models import Profile
from poker_app.web.helpers import BootstrapFormMixin
from poker_app.web.models import Table

UserModel = get_user_model()


#
#
# TODO: 'add BootstrapFormMixin to the createtableform'
class CreateTableForm(forms.ModelForm, BootstrapFormMixin):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        # commit false does not persist to database
        # just returns the object to be created
        table = super().save(commit=False)

        table.user = self.user
        if commit:
            table.save()

        return table

    class Meta:
        model = Table
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter table name',
                }
            ),

            'max_players': forms.TextInput(
                attrs={
                    'placeholder': 'Enter max players',
                }
            ),
        }


class EditTableForm(BootstrapFormMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Table
        fields = '__all__'


class DisabledFieldsFormMixin:
    pass


class DeleteTableForm(forms.ModelForm, BootstrapFormMixin, DisabledFieldsFormMixin):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self._init_bootstrap_form_controls()
    #     self._init_disabled_fields()

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Table
        fields = ()
        # fields = "__all__"
