from django.contrib import admin
from sticker_collection_app.models import (
    NationalTeam, Sticker, WorldCupAlbum
)

# Register your models here.
class NationalTeamAdmin(admin.ModelAdmin):
    prepopulated_fields = {'team_slug': ('team_display_name',)}
admin.site.register(NationalTeam, NationalTeamAdmin)

class StickerAdmin(admin.ModelAdmin):
    prepopulated_fields = {'player_slug': ('player_name', )}
admin.site.register(Sticker, StickerAdmin)

class WorldCupAlbumAdmin(admin.ModelAdmin):
    pass
admin.site.register(WorldCupAlbum, WorldCupAlbumAdmin)