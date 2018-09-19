from django.db import models
from datetime import datetime
from sticker_collection_app.constants import WorldCupGroup, WorldCups


class WorldCupAlbum(models.Model):
    location = models.CharField(choices=WorldCups.choices(), max_length=7)

    def __str__(self):
        return self.location


class NationalTeam(models.Model):
    album = models.ForeignKey(to=WorldCupAlbum, on_delete=models.CASCADE)
    team_order = models.IntegerField(blank=False, help_text="Order of teams in book")
    team_slug = models.SlugField(unique=False)
    team_display_name = models.CharField(blank=False, max_length=80)
    team_group = models.CharField(choices=WorldCupGroup.choices(), max_length=7)
    team_blurb = models.CharField(blank=True, max_length=250)

    def __str__(self):
        return self.team_display_name

    def save(self, *args, **kwargs):
        if not self.id:
            self.team_slug = slugify(self.team_display_name)

        super(NationalTeam, self).save(*args, **kwargs)


class Sticker(models.Model):
    player_slug = models.SlugField(unique=True)
    player_name = models.CharField(max_length=80, blank=False)
    card_number = models.IntegerField(blank=False)
    team = models.ForeignKey(to=NationalTeam, on_delete=models.CASCADE)
    special_card = models.BooleanField(default=False)
    count = models.IntegerField(default=0, blank=False)

    def __str__(self):
        return self.player_name

    def save(self, *args, **kwargs):
        if not self.id:
            self.player_slug = slugify(self.player_name)

        super(Sticker, self).save(*args, **kwargs)