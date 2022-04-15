from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model
from django.contrib.postgres import validators

from poker_app.web.helpers import BootstrapFormMixin
from poker_app.accounts.models import Profile

UserModel = get_user_model()


class CreateProfileForm(BootstrapFormMixin, auth_forms.UserCreationForm):
    # MAX_MONEY_VALUE = 100

    first_name = forms.CharField(
        max_length=Profile.FIRST_NAME_MAX_LENGTH,
    )
    last_name = forms.CharField(
        max_length=Profile.LAST_NAME_MAX_LENGTH,
    )
    picture = forms.URLField()
    date_of_birth = forms.DateField()
    money = forms.IntegerField()

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
            money=self.cleaned_data['money'],
            email=self.cleaned_data['email'],
            # gender=self.cleaned_data['gender'],
            # user=user,
        )

        if commit:
            profile.save()
        return user

    class Meta:
        model = UserModel
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', 'picture', 'money')
        # widgets = {
        #     'first_name': forms.TextInput(
        #         attrs={
        #             'placeholder': 'Enter first name',
        #         }
        #     ),
        #     'last_name': forms.TextInput(
        #         attrs={
        #             'placeholder': 'Enter last name',
        #         }
        #     ),
        #     'picture': forms.TextInput(
        #         attrs={
        #             'placeholder': 'Enter URL',
        #         }
        #     ),
        # }
