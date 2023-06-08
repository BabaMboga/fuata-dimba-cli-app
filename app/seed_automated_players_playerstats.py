from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from models import Player, PlayerStat, Base


engine = create_engine('sqlite:///fuata_dimba.db')
Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()

#generate seed data for 500 players
for p in range(500):
    #create a player

    player = Player(
        full_name=fake.name(),
        nationality = fake.country(),
        age = fake.random_int(min=16, max=40),
    )

    #create player stats for the player
    shots = fake.random_int(min=0, max=100)
    goals = fake.random_int(min=0, max=50)
    assists = fake.random_int(min=0, max=25)

    if shots > 0 :
        conversion_rate = (goals/shots) * 100
    else:
        conversion_rate = 0
    
    goal_contributions = goals + assists

    player_stat = PlayerStat(
        shots = shots,
        goals = goals,
        assists = assists,
        goal_contributions = goal_contributions,
        pass_completion_percentage = fake.random_int(min=0, max=100),
        clean_sheets = fake.random_int(min=0, max=20),
        conversion_rate = conversion_rate,
        yellow_cards = fake.random_int(min=0, max=20),
        red_cards =fake.random_int(min=0, max =10),
        player=player,
    )

    session.add(player)
    session.add(player_stat)

session.commit()
