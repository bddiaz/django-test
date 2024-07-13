from django.shortcuts import render

# Create your views here.
from .models import Team, Player

def team_list(request):
    teams = Team.objects.all()
    return render(request, 'team_list.html', {'teams': teams})

def player_list(request):
    players = Player.objects.all()[:50]  # Limit to first 50 for performance
    return render(request, 'player_list.html', {'players': players})