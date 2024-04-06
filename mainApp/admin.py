from django.contrib import admin

from statsApp.models import *


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prezident', 'trener', 't_sana', 'kapital', 'davlat')
    search_fields = ('nom', )
    list_filter = ('davlat',)
@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('ism', 'raqam', 'club', 't_sana', 'maosh', 'narx', 'davlat', 'possitsiya')
    list_filter = ('club', 'davlat', 'possitsiya')
    search_fields = ('ism', 'club__nom')
@admin.register(Davlat)
class DavlatAdmin(admin.ModelAdmin):
    list_display = ('nom',)
@admin.register(Pozitsiya)
class PozitsiyaAdmin(admin.ModelAdmin):
    list_display = ('nom', 'turi')



