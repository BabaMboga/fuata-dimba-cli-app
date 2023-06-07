from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


from models import Team, Coach, Player, PlayerStat, team_coach, team_player



convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%referred_table_name)s",
}

metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

#Defining my functions
#search for a particular team via name
def find_team():
    pass
#returns all teams in our teams table
def view_teams():
    pass

#returns all players in a particular team
def players_in_team():
    pass

#sort teams by goal difference
def sort_team_goal_difference():
    pass

#sort team by games won
def sort_team_wins():
    pass

#sort team by games lost
def sort_team_losses():
    pass

def find_coach():
    pass

def view_coaches():
    pass

def view_coach_player():
    pass

def view_players():
    pass

def view_playerstat():
    pass

def best_conversion_rate():
    pass

def top_twenty_scorers_report():
    pass

def top_twenty_assisters():
    pass

def most_indisciplined_player():
    pass





#this is the program menu for the user
def main_menu():
    pass


if __name__ == '__main__':
    engine = create_engine('sqlite:///fuata_dimba.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    main_menu()