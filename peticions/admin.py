from django.contrib import admin
from .models import Peticions, Vote


@admin.register(Peticions)
class PetitionsAdmin(admin.ModelAdmin):
    pass


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    pass
