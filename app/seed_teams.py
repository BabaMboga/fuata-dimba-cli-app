from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Team, Base

#Defined data for teams

premier_league = [
    {
        "team_name": "Manchester City",
        "played_games": 38,
        "won_games": 28,
        "lost_games": 5,
        "drawn_games": 5,
        "goals_scored": 94,
        "goals_allowed": 33,
    },
    {
        "team_name": "Arsenal",
        "played_games": 38,
        "won_games": 26,
        "lost_games": 6,
        "drawn_games": 6,
        "goals_scored": 88,
        "goals_allowed": 43,
    },
    {
        "team_name": "Manchester United",
        "played_games": 38,
        "won_games": 23,
        "lost_games": 9,
        "drawn_games": 6,
        "goals_scored": 58,
        "goals_allowed": 43,
    },
    {
        "team_name": "Newcastle",
        "played_games": 38,
        "won_games": 19,
        "lost_games": 5,
        "drawn_games": 14,
        "goals_scored": 68,
        "goals_allowed": 33,
    },
    {
        "team_name": "Liverpool",
        "played_games": 38,
        "won_games": 19,
        "lost_games": 9,
        "drawn_games": 10,
        "goals_scored": 75,
        "goals_allowed": 47,
    },
    {
        "team_name": "Brighton",
        "played_games": 38,
        "won_games": 18,
        "lost_games": 12,
        "drawn_games": 8,
        "goals_scored": 72,
        "goals_allowed": 53,
    },
    {
        "team_name": "Aston Villa",
        "played_games": 38,
        "won_games": 18,
        "lost_games": 13,
        "drawn_games": 7,
        "goals_scored": 51,
        "goals_allowed": 46,
    },
    {
        "team_name": "Tottenham",
        "played_games": 38,
        "won_games": 18,
        "lost_games": 14,
        "drawn_games": 6,
        "goals_scored": 70,
        "goals_allowed": 63,
    },
    {
        "team_name": "Brentford",
        "played_games": 38,
        "won_games": 15,
        "lost_games": 9,
        "drawn_games": 14,
        "goals_scored": 58,
        "goals_allowed": 46,
    },
    {
        "team_name": "Fulham",
        "played_games": 38,
        "won_games": 15,
        "lost_games": 16,
        "drawn_games": 7,
        "goals_scored": 55,
        "goals_allowed": 53,
    },
    {
        "team_name": "Crystal Palace",
        "played_games": 38,
        "won_games": 11,
        "lost_games": 15,
        "drawn_games": 12,
        "goals_scored": 40,
        "goals_allowed": 49,
    },
    {
        "team_name": "Chelsea",
        "played_games": 38,
        "won_games": 11,
        "lost_games": 16,
        "drawn_games": 11,
        "goals_scored": 38,
        "goals_allowed": 47,
    },
    {
        "team_name": "Wolves",
        "played_games": 38,
        "won_games": 11,
        "lost_games": 19,
        "drawn_games": 8,
        "goals_scored": 38,
        "goals_allowed": 47,
    },
    {
        "team_name": "Westham",
        "played_games": 38,
        "won_games": 11,
        "lost_games": 20,
        "drawn_games": 7,
        "goals_scored": 42,
        "goals_allowed": 55,
    },
     {
        "team_name": "Bournemouth",
        "played_games": 38,
        "won_games": 11,
        "lost_games": 21,
        "drawn_games": 6,
        "goals_scored": 37,
        "goals_allowed": 71,
    },
     {
        "team_name": "Forest",
        "played_games": 38,
        "won_games": 9,
        "lost_games": 18,
        "drawn_games": 11,
        "goals_scored": 38,
        "goals_allowed": 68,
    },
     {
        "team_name": "Everton",
        "played_games": 38,
        "won_games": 8,
        "lost_games": 18,
        "drawn_games": 12,
        "goals_scored": 34,
        "goals_allowed": 57,
    },
     {
        "team_name": "Leicester",
        "played_games": 38,
        "won_games": 9,
        "lost_games": 22,
        "drawn_games": 7,
        "goals_scored": 51,
        "goals_allowed": 68,
    },
     {
        "team_name": "Leeds",
        "played_games": 38,
        "won_games": 7,
        "lost_games": 21,
        "drawn_games": 10,
        "goals_scored": 48,
        "goals_allowed": 78,
    }, {
        "team_name": "Southampton",
        "played_games": 38,
        "won_games": 6,
        "lost_games": 25,
        "drawn_games": 7,
        "goals_scored": 36,
        "goals_allowed": 73,
    }
    
]

engine = create_engine('sqlite:///fuata_dimba.db')
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

team_entries = session.query(Team).count()

#Limit the entries to 20 if they exceed the limit
if team_entries > 20:
    session.query(Team).delete()
    session.commit()

#Populates table
for data in premier_league:
    team = Team(
        team_name = data["team_name"],
        played_games = data["played_games"],
        won_games = data["won_games"],
        lost_games = data["lost_games"],
        drawn_games = data["drawn_games"],
        goals_scored = data["goals_scored"],
        goals_allowed = data["goals_allowed"],
        goal_difference = data["goals_scored"] - data["goals_allowed"],
        points = (data["won_games"] * 3) + data["drawn_games"],
    )
    session.add(team)


session.commit()