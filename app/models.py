from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%referred_table_name)s",
}

metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Team(Base):
    __tablename__ = 'teams'

    id = Column(Integer(), primary_key = True)
    team_name = Column(String())
    played_games = Column(Integer, default = 38)
    won_games = Column(Integer)
    lost_games = Column(Integer)
    drawn_games = Column(Integer)
    goals_scored = Column(Integer)
    goals_allowed = Column(Integer)
    goal_difference = Column(Integer)
    points = Column(Integer)

    def __init__(self, team_name, played_games, won_games, 
                 lost_games, drawn_games, goals_scored, 
                 goals_allowed):
        self.team_name = team_name
        self.played_games = played_games
        self.won_games = won_games
        self.lost_games = lost_games
        self.drawn_games = drawn_games
        self.goals_scored = goals_scored
        self.goals_allowed = goals_allowed
        self.goal_difference = (goals_scored - goals_allowed)
        self.points = (won_games*3)

class Coach(Base):
    __tablename__ = 'coaches'

    id = Column(Integer(), primary_key = True)
    first_name = Column(String())
    second_name = Column(String())
    nationality = Column(String())
    age = Column(Integer())
    team_id = Column(Integer())

    def __init__(self, first_name, second_name, nationality, age, team_id):
        self.first_name = first_name
        self.second_name = second_name
        self.nationality = nationality
        self.age = age
        self.team_id = team_id

class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer(), primary_key = True)
    first_name = Column(String())
    second_name = Column(String())
    nationality = Column(String())
    age = Column(String())
    player_id = Column(Integer(), ForeignKey("player.id"))

    

class PlayerStat(Base):
    __tablename__ = 'playerstats'

    id = Column(Integer(), primary_key = True)
    shots = Column(Integer())
    goals = Column(Integer())
    assists = Column(Integer())
    pass_completion_percentage = Column(Integer())
    clean_sheets = Column(Integer())
    conversion_rate = Column(Integer())
    yellow_cards = Column(Integer())
    red_cards = Column(Integer())
    player = relationship('Player', backref=backref('playerstat', uselist=False))




