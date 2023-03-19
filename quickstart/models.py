from django.db import models

class Player(models.Model):
    name = models.TextField(default="")
    position = models.TextField(default="")
    birth_date = models.DateField(default="0001-01-01")

class Match(models.Model):
    Reeks = models.TextField(default="goofy")
    Reeksnaam = models.TextField(default="")
    '''dag = models.TextField(default="")
    WNR = models.TextField(default="")
    Provincie = models.TextField(default="")
    myurl = models.TextField(default="")
    Competitie = models.TextField(default="")
    Datum = models.TextField(default="")
    aanvangsuur = models.TextField(default="")
    thuisploeg = models.TextField(default="")
    bezoekers = models.TextField(default="")
    idthuis = models.TextField(default="")
    idbezoek = models.TextField(default="")
    stamnrthuis = models.TextField(default="")
    stamnrbezoek = models.TextField(default="")
    resulthoofd = models.TextField(default="")
    forfaithoofd = models.TextField(default="")
    resultset1h = models.TextField(default="")
    resultset2h = models.TextField(default="")
    resultset3h = models.TextField(default="")
    resultset4h = models.TextField(default="")
    resultset5h = models.TextField(default="")
    resultreserve = models.TextField(default="")
    forfaitreserve = models.TextField(default="")
    resultset1r = models.TextField(default="")
    resultset2r = models.TextField(default="")
    resultset3r = models.TextField(default="")
    sporthalafk = models.TextField(default="")
    sporthalnaam = models.TextField(default="")
    sporthalstraat = models.TextField(default="")
    sporthalnummer = models.TextField(default="")
    sporthalgemeente = models.TextField(default="")'''

    def __str__(self):
        return f"{self.Reeks} - {self.Reeksnaam}"

class Team(models.Model):
    name = models.TextField(default="")
    league = models.TextField(default="")
    gender = models.TextField(default='')
