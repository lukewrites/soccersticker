from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from sticker_collection_app.models import NationalTeam, Sticker


class SingleCardView(DetailView):
    model = Sticker
    template_name = 'player_page.html'


class TeamView(DetailView):
    model = NationalTeam
    template_name = 'team_page.html'


class AllTeamsView(ListView):
    model = NationalTeam
    template_name='all_teams.html'
