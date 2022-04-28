from django import forms

from django.contrib.auth import forms as auth_forms, get_user_model

from poker_app.accounts.models import Profile
from poker_app.web.helpers import BootstrapFormMixin

UserModel = get_user_model()


class CreateProfileForm(BootstrapFormMixin, auth_forms.UserCreationForm):
    first_name = forms.CharField(
        max_length=Profile.FIRST_NAME_MAX_LENGTH,
    )

    last_name = forms.CharField(
        max_length=Profile.LAST_NAME_MAX_LENGTH,
    )

    age = forms.IntegerField()

    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            age=self.cleaned_data['age'],
            email=self.cleaned_data['email'],
            user=user,
        )

        if commit:
            profile.save()
        return user

    class Meta:
        model = UserModel
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', 'age')
        # fields = ('username', 'password1', 'password2')

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

            'password1': forms.TextInput(
                attrs={
                    'placeholder': 'Enter yor password',
                }
            ),

            'password2': forms.TextInput(
                attrs={
                    'placeholder': 'REPEAT yor password',
                }
            ),

            'age': forms.TextInput(
                attrs={
                    'placeholder': 'Enter yor age',
                }
            ),

        }


class EditProfileForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Profile
        exclude = 'user',


class DeleteProfileForm(forms.ModelForm, BootstrapFormMixin):

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()
