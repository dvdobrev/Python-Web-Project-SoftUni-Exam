from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

from poker_app.accounts.models import Profile
from poker_app.web.helpers import BootstrapFormMixin
from poker_app.web.models import Table

UserModel = get_user_model()


class CreateProfileForm(BootstrapFormMixin, auth_forms.UserCreationForm):
    first_name = forms.CharField(
        max_length=Profile.FIRST_NAME_MAX_LENGTH,
    )
    last_name = forms.CharField(
        max_length=Profile.LAST_NAME_MAX_LENGTH,
    )
    picture = forms.URLField()
    date_of_birth = forms.DateField()
    slogan = forms.CharField(
        widget=forms.Textarea,
    )
    email = forms.EmailField()

    # gender = forms.ChoiceField(
    #     choices=Profile.GENDERS,
    # )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            picture=self.cleaned_data['picture'],
            date_of_birth=self.cleaned_data['date_of_birth'],
            slogan=self.cleaned_data['slogan'],
            email=self.cleaned_data['email'],
            # gender=self.cleaned_data['gender'],
            user=user,
        )

        if commit:
            profile.save()
        return user

    class Meta:
        model = UserModel
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', 'picture', 'slogan')
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter first name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter last name',
                }
            ),
            'picture': forms.TextInput(
                attrs={
                    'placeholder': 'Enter URL',
                }
            ),
        }


#
#
class CreateTableForm(BootstrapFormMixin, forms.ModelForm):

    # def __init__(self, user, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.user = user
    #     self._init_bootstrap_form_controls()
    #
    # def save(self, commit=True):
    #     # commit false does not persist to database
    #     # just returns the object to be created
    #     table = super().save(commit=False)
    #
    #     table.user = self.user
    #     if commit:
    #         table.save()
    #
    #     return table

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
