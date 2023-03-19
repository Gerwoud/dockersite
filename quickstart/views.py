import requests
from django.contrib.auth.models import User, Group
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.viewsets import ViewSet

from quickstart.models import Player, Match, Team
from quickstart.serializers import UserSerializer, GroupSerializer, PlayerSerializer, TeamSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class MatchViewSet(ViewSet):

    def list(self, request, format=None):
        url = 'https://volleybieb.be/ajax/ajaxVVBWedstijden.php?wattedoen=1&provincie=6&reeks=OHP3&competitie=100&team=0&stamnummer=O-1283'
        # Fetch the data from the URL
        response = requests.get(url)
        # Deserialize the response content to a list of dicts
        data = response.json()
        # Create a list of MyModel instances from the data
        matchen = []
        for obj in data:
            if obj["thuisploeg"] == "Volley Team TEMSE B" or obj["bezoekers"] == "Volley Team TEMSE B":
                del obj['myOK']
                del obj['mySql']
                tmp = Match(Reeksnaam="augh", Reeks="kifesh")
                matchen.append(obj)
                # print(tmp)
        queryset = matchen

        return Response(data=queryset)
