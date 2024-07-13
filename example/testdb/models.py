from django.db import models
from django.contrib.postgres.fields import JSONField

class Team(models.Model):
    TEAM_ID = models.IntegerField(primary_key=True)
    name = models.TextField(null=False)
    code = models.TextField(null=False)
    logo = models.TextField(null=False)
    city = models.TextField(null=False)
    abbreviation = models.TextField(null=False)
    state = models.TextField(null=False)
    year_founded = models.IntegerField(null=False)

    class Meta:
        db_table = 'teams'
        
    def __str__(self):
        return self.name


class Player(models.Model):
    id = models.AutoField(primary_key=True)
    FIRST_NAME = models.TextField(null=False)
    LAST_NAME = models.TextField(null=False)
    DISPLAY_FIRST_LAST = models.TextField(null=False)
    DISPLAY_LAST_COMMA_FIRST = models.TextField(null=False)
    DISPLAY_FI_LAST = models.TextField(null=False)
    PLAYER_SLUG = models.TextField(null=False)
    BIRTHDATE = models.TextField(null=False)
    SCHOOL = models.TextField(null=False)
    COUNTRY = models.TextField(null=False)
    LAST_AFFILIATION = models.TextField(null=False)
    HEIGHT = models.TextField(null=False)
    WEIGHT = models.TextField(null=False)
    SEASON_EXP = models.IntegerField(null=False)
    JERSEY = models.TextField(null=False)
    POSITION = models.TextField(null=False)
    ROSTERSTATUS = models.TextField(null=False)
    TEAM = models.ForeignKey(Team, on_delete=models.DO_NOTHING, db_column='TEAM_ID')
    TEAM_NAME = models.TextField(null=False)
    TEAM_ABBREVIATION = models.TextField(null=False)
    TEAM_CODE = models.TextField(null=False)
    TEAM_CITY = models.TextField(null=False)
    PLAYERCODE = models.TextField(null=False)
    FROM_YEAR = models.IntegerField(null=True)
    TO_YEAR = models.IntegerField(null=True)
    DLEAGUE_FLAG = models.TextField(null=True)
    NBA_FLAG = models.TextField(null=True)
    GAMES_PLAYED_FLAG = models.TextField(null=True)
    DRAFT_YEAR = models.TextField(null=True)
    DRAFT_ROUND = models.TextField(null=True)
    DRAFT_NUMBER = models.TextField(null=True)
    IS_ACTIVE = models.TextField(null=True)
    averages = JSONField(null=True)

    class Meta:
        db_table = 'players'
        
    def __str__(self):
        return f"{self.FIRST_NAME} {self.LAST_NAME}"
