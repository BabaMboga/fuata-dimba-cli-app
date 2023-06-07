from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from models import Team, Coach, Base

engine = create_engine('sqlite:///fuata_dimba.db')
Session = sessionmaker(bind=engine)
session = Session()

#creating a faker instance
fake = Faker()

#Define the team names to choose from

team_names = ["Manchester City","Arsenal","Manchester United","Newcastle", "Liverpool",
              "Brighton", "Aston Villa","Tottenham", "Brentford","Fulham",
              "Crystal Palace", "Chelsea", "Wolves", "Westham", "Bournemouth", "Forest",
              "Everton", "Leicester", "Leeds", "Southampton"]

for c in range(20):
    #create a coach
    coach = Coach(
        first_name = fake.first_name(),
        second_name = fake.last_name(),
        nationality = fake.country(),
        age = fake.random_int(min=25, max=60),
    )

    #generate a random team
    team_name = fake.random_element(elements=team_names)
    team = session.query(Team).filter_by(team_name=team_name).first()

    #assign coach to the team
    team.coach = coach

    #adding coach to the session
    session.add(coach)

#commit the changes to the database
session.commit()

