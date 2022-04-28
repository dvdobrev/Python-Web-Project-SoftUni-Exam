from django.core.exceptions import ValidationError
from django.test import TestCase

from poker_app.accounts.models import Profile

#
# class ProfileTests(TestCase):
#     PROFILE_DATA = {
#         'first_name': 'Dobri',
#         'last_name': 'Dobrev',
#         'age': 20,
#         # 'email': '1@abv.bg',
#         'user_id': 2,
#     }
#
#     def test_profile_has_dollar_sign_expect_to_fail(self):
#         first_name = ''
#         profile = Profile(
#             first_name=first_name,
#             last_name=self.PROFILE_DATA['last_name']
#         )
#
#         with self.assertRaises(ValidationError) as context:
#             profile.full_clean()
#             profile.save()
#
#         self.assertIsNotNone(context.exception)
#
#     def test_profile_takes_valid_data(self):
#         # profile = Profile(
#         #     first_name=self.PROFILE_DATA['first_name'],
#         #     last_name=self.PROFILE_DATA['last_name'],
#         # )
#         profile = Profile(**self.PROFILE_DATA)
#         profile.save()
#
#         # self.assertIsNotNone(profile.user_id)
