from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from models import Team, Coach, Base

engine = create_engine('sqlite:///app/fuata_dimba.db')
Session = sessionmaker(bind=engine)
session = Session()

# Creating a faker instance
fake = Faker()

# Define the team names to choose from
team_names = ["Manchester City", "Arsenal", "Manchester United", "Newcastle", "Liverpool",
              "Brighton", "Aston Villa", "Tottenham", "Brentford", "Fulham",
              "Crystal Palace", "Chelsea", "Wolves", "Westham", "Bournemouth", "Forest",
              "Everton", "Leicester", "Leeds", "Southampton"]

# Get the existing number of coach entries
coach_entries = session.query(Coach).count()

# Limit the entries to 20 if they exceed the limit
if coach_entries > 20:
    session.query(Coach).delete()
    session.commit()

# Shuffle the team names to randomize the order
fake.random.shuffle(team_names)

coaches = []

for i in range(20):
    # Create a coach
    coach = Coach(
        full_name=fake.name(),
        nationality=fake.country(),
        age=fake.random_int(min=25, max=60),
    )
    coaches.append(coach)

# Assign teams to coaches in a one-to-one manner
for i in range(len(coaches)):
    team_name = team_names[i % len(team_names)]  # Use modulo operator for cyclic team assignment
    team = session.query(Team).filter_by(team_name=team_name).first()
    coaches[i].team_id = team.id
    session.add(coaches[i])

# Commit the changes to the database
session.commit()
