from django.test import TestCase
from django.urls import reverse

from poker_app.accounts.models import Profile


class RegisterViewTests(TestCase):
    PROFILE_DATA = {
        'first_name': 'Dobri',
        'last_name': 'Dobrev',
        'age': 20,
        'email': '1@abv.bg',
        'id': 5,
    }

    def test_expect_to_create_profile__when_all_valid_(self):
        self.client.post(
            reverse('register'),
            data=self.PROFILE_DATA,
        )

        profile = Profile.objects.first()
        self.assertIsNotNone(profile)
        self.assertEqual(self.PROFILE_DATA['first_name'], profile.first_name)
        self.assertEqual(self.PROFILE_DATA['last_name'], profile.last_name)
        self.assertEqual(self.PROFILE_DATA['age'], profile.age)
        self.assertEqual(self.PROFILE_DATA['email'], profile.email)


