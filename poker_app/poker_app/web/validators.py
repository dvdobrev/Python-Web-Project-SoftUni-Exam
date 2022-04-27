from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


def validate_only_letters(value):
    for ch in value:
        if not ch.isalnum():
            raise ValidationError('Please insert only letters and digits')


@deconstructible
class GameMaxPlayersValidator:
    def __init__(self, max_value):
        self.max_value = max_value

    def __call__(self, value):
        if value > self.max_value:
            raise ValidationError(f'You can play the game with max {self.max_value}. Please choose less players.')


@deconstructible
class GameMinPlayersValidator:
    def __init__(self, min_value):
        self.min_value = min_value

    def __call__(self, value):
        if value < self.min_value:
            raise ValidationError(
                f'You can play the game with min {self.min_value} another players. Please choose more players.')


@deconstructible
class RouletteMinPlayersValidator:
    def __init__(self, min_value):
        self.min_value = min_value

    def __call__(self, value):
        if value <= 0:
            raise ValidationError(
                f'Hey! It have to be atleast one player.')


@deconstructible
class RouletteMaxPlayersValidator:
    def __init__(self, min_value):
        self.min_value = min_value

    def __call__(self, value):
        if value < self.min_value:
            raise ValidationError(
                f'The casino made the min bet for this game to be {self.min_value} $. Please choose another min bet.')


@deconstructible
class MaxBetValidator:
    def __init__(self, min_value):
        self.min_value = min_value

    def __call__(self, value):
        if value > self.min_value:
            raise ValidationError(
                f'The casino made the max bet for this game to be {self.min_value} $. Please choose another max bet.')
