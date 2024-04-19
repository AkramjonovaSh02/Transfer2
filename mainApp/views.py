from django.shortcuts import render
from django.views import View
from .models import *

class Home(View):
    def get(self, request):
        return render(request, "index.html")


class About(View):
    def get(self, request):
        return render(request, "about.html")

class Tryouts(View):
    def get(self, request):
        return render(request, "tryouts.html")

class ClubsView(View):
    def get(self, request):
        context = {
            'clublar': Club.objects.order_by('-kapital')
        }
        return render(request, "clubs.html", context)

class CountryClubView(View):
    def get(self, request, pk):
        context = {
            'clubs': Club.objects.filter(davlat__id=pk),
            'davlat': Davlat.objects.get(id=pk)
        }
        return render(request, 'club-players.html', context)

class PlayerView(View):
    def get(self, request):
        players = Player.objects.order_by('ism')
        return render(request, 'players.html', {'players': players})

class U20View(View):
    def get(self, request):
        all = Player.objects.all()
        players = []
        for player in all:
            if player.yosh() <= 20:
                players.append(player)
        context = {
            'player': players
        }

        return render(request, "U-20 players.html", context)

class ClubPlayerView(View):
    def get(request, pk):
        club = Club.objects.get(id=pk)
        players = Player.objects.filter(club=club)
        context = {'club': club,
                   'players': players}
        return render(request, 'club-players.html', context)

class Stats(View):
    def get(self, request):
        return render(request, "stats.html")


