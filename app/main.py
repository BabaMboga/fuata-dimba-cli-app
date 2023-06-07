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
    teams = session.query(Team).all
    team_dict = {team.team_name: team for team in teams}

    team_name = input("Enter the name of the team: ")
    if team_name in team_dict:
        team = team_dict[team_name]
        print(f"Team Position: {team.id}")
        print(f"Team Name: {team.team_name}")
        print(f"Games Played: {team.played_games}")
        print(f"Games Won: {team.won_games}")
        print(f"Games Drawn: {team.drawn_games}")
        print(f"Games Lost: {team.lost_games}")
        print(f"Goals Scored: {team.goals_scored}")
        print(f"Goals Allowed: {team.goals_allowed}")
        print(f"Goal Difference: {team.goal_difference}")
        print(f"Points: {team.points}")
    else:
        print("Team not found.")

    
#returns all teams in our teams table
def view_teams():
    teams = session.query(Team).all()
    team_list = [team.team_name for team in teams]

    if team_list:
        print("Teams:")
        for team_name in team_list:
            print(team_name)
    else:
        print("No teams found.")
    

#returns all players in a particular team
def players_in_team():
    name = input("Enter the team name: ")
    team = session.query(Team).filter_by(team_name=name).first()
    if team:
        players = session.query(Player).join(team_player).filter_by(team_id = team.id).all()
        if players:
            print(f"Players in {name}:")
            for player in players:
                print (f"- {player.full_name}")
        else:
            print (f"No players found in {name}.")
    else:
        print("Team not found")
    

#sort teams by goal difference
def sort_team_goal_difference():
    teams = session.query(Team).order_by(Team.goal_difference.desc()).all()
    if teams:
        print("Teams sorted by Goal Difference:")
        print("*******")
        for team in teams:
            print(f"Team: {team.team_name}")
            print(f"Goal Difference: {team.goal_difference}")
            print("-----------")
    else:
        print("No teams found.")

#sort team by games won
def sort_team_wins():
    teams = session.query(Team).order_by(Team.won_games.desc()).all()
    if teams:
        print("Teams sorted by Wins:")
        print("-----------")
        for team in teams:
            print(f" -{team.team_name} (Wins: {team.won_games})")
    else:
        print("No teams found.")

#sort team by games lost
def sort_team_losses():
    teams = session.query(Team).order_by(Team.lost_games.desc()).all()
    if teams:
        print("Teams sorted by Losses: ")
        print("-----------")
        for team in teams:
            print(f"- {team.team_name} (Losses: {team.lost_games})")
    else:
        print("No teams found.")

#find the coach for a particular team
def find_coach():
    pass

#show all coaches in the database
def view_coaches():
    pass

#view all players for a particular coach
def view_coach_players():
    pass

#view all players in the database
def view_players():
    pass

#view stat for a particular player by name
def view_playerstat():
    pass

#display the player with the best conversion rate
def best_conversion_rate():
    pass

#display the top twenty scorers and generate a report on txt with the same
def top_twenty_scorers_report():
    pass

#display the top twenty assisters
def top_twenty_assisters():
    pass

#displays the player with the most yellow and red cards together
def most_indisciplined_player():
    pass

#displays the top 50 players in goal contributions and generate a report on txt reflexting the same
def top_def_50_goal_contributions_report():
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