from django.contrib import admin

# Register your models here.

from django.contrib import admin

from poker_app.accounts.models import PokerUser, Profile
from poker_app.dice.models import Dice
from poker_app.poker.models import Poker
from poker_app.roulette.models import Roulette


@admin.register(PokerUser)
class PokerUserAdmin(admin.ModelAdmin):
    list_display = ('username',)

    def username(self, object):
        return object.user.username


@admin.register(Profile)
class PokerUserAdmin(admin.ModelAdmin):
    list_display = ('username',)

    def username(self, object):
        return object.user.username


@admin.register(Dice)
class PokerUserAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Poker)
class PokerUserAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Roulette)
class PokerUserAdmin(admin.ModelAdmin):
    list_display = ('name',)
