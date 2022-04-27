from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


def validate_only_letters(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError('Please insert only letters')


@deconstructible
class GameMaxPlayersValidator:
    def __init__(self, max_value):
        self.max_value = max_value

    def __call__(self, value):
        if value < self.max_value:
            raise ValidationError(f'You can play the game with max {self.max_value}. Please choose less players.')


@deconstructible
class GameMinPlayersValidator:
    def __init__(self, min_value):
        self.min_value = min_value

    def __call__(self, value):
        if value < self.min_value:
            raise ValidationError(f'You can play the game with min {self.min_value}. Please choose less players.')
