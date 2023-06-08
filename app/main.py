from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from tqdm import tqdm
import time
from models import Team, Coach, Player, PlayerStat, team_coach, team_player


convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%referred_table_name)s",
}

metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

engine = create_engine('sqlite:///fuata_dimba.db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()




#Defining my functions
#search for a particular team via name
def find_team():
    teams = session.query(Team).all()
    team_dict = {team.team_name: team for team in teams}

    team_name = input("Enter the name of the team: ").title()
    if not team_name:
        print("Team name cannot be empty.")
        return
    
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
    name = input("Enter the team name: ").title()
    if not name:
        print("Team name cannot be empty: ")
        return
    
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
    name = input("Enter the name of the team: ").title()
    if not name:
        print("Coach name cannot be empty.")
        return
    
    team = session.query(Team).filter(Team.team_name == name ).first()

    if team:
        coach = session.query(Coach).join(team_coach).filter(team_coach.c.team_id == team.id).first()
        if coach:
            print(f"The coach of {team.team_name} is {coach.full_name}")
        else:
            print(f"No coach found for {team.team_name}")
    else:
        print("Team not found.")

#show all coaches in the database
def view_coaches():
    coaches = session.query(Coach).all()
    if coaches:
        print(f"All Coaches: ")
        print("-----------")
        print("")
        for coach in coaches:
            print(f" - {coach.full_name} from {coach.nationality} is {coach.age}")
    else:
        print("No coaches found.")

#view all players for a particular coach
def view_coach_players():
    coach_name = input("Enter the coach name: ").title()
    if not coach_name:
        print("Coach name cannot be empty.")
        return 
    
    coach = session.query(Coach).filter_by(full_name=coach_name).first()
    if coach:
        players = session.query(Player).join(team_player).filter(team_player.c.team_id == coach.team.id).all()
        for player in players:
            print(f"Player: {player.full_name}")
    else:
        print("Coach not found.")

#view all players in the database
def view_players():
    players = session.query(Player).all()
    if players:
        print("All Players: ")
        print("-----------")
        for player in players:
            print(f"{player.id} {player.full_name}")
    else:
        print("No players found.")

    

#view stat for a particular player by name
def view_playerstat():
    player_name = input("Enter the player name: ").title()
    if not player_name:
        print("Player name cannot be empty")
        return
    
    player_stat = session.query(PlayerStat).join(Player).filter(Player.full_name == player_name).first()
    if player_stat:
        player_info = (player_stat.goals, player_stat.assists, player_stat.shots, player_stat.goal_contributions,
                       player_stat.pass_completion_percentage, player_stat.clean_sheets,
                       player_stat.conversion_rate, player_stat.yellow_cards, player_stat.red_cards)
        if player_stat:
            print(f"Stats for {player_name}: ")
            print(f"- Goals: {player_info[0]}")
            print(f"- Assists: {player_info[1]}")
            print(f"- Shots: {player_info[2]}")
            print(f"- Goal Contributions: {player_info[3]}")
            print(f"- Pass Completion(%): {player_info[4]}")
            print(f"- Clean Sheets: {player_info[5]}")
            print(f"- Conversion Rate: {player_info[6]}")
            print(f"- Yellow Cards: {player_info[7]}")
            print(f"- Red Cards: {player_info[8]}")
        else:
            print(f"No stats found for {player_name}.")
    else:
        print("Player not found.")

#display the player with the best conversion rate
def best_conversion_rate():
    best_player = session.query(Player).join(PlayerStat).order_by(PlayerStat.conversion_rate.desc()).first()

    if best_player:
        print(f"Player with the best conversion rate in the league: {best_player.full_name}")
        print(f"Conversion Rate: {best_player.playerstat.conversion_rate}")
    else:
        print("No players found.")

#display the top twenty scorers and generate a report on txt with the same
def top_twenty_scorers_report():
    players = session.query(Player).join(PlayerStat).order_by(PlayerStat.goals.desc()).limit(20).all()
    print("Top 20 Scorers: ")
    print("******")
    for i, player in enumerate(players, start=1):
        print(f"{i}. {player.full_name} - Goals: {player.playerstat.goals}\n ")
    
    with open("top_scorers.txt", "w") as file:
        file.write("Top 20 Scorers: \n")
        for i, player in enumerate(players, start = 1):
            file.write(f"{i}. {player.full_name} - Goals: {player.playerstat.goals} ")
    
    print("Top 20 Scorers report generated.")

#display the top twenty assisters
def top_twenty_assisters():
    players = session.query(Player).join(PlayerStat).order_by(PlayerStat.assists.desc()).limit(20).all()
    if players:
        print("Top 20 Assisters:")
        print("******")
        for player in players:
            print(f"Player: {player.full_name} ===== {player.playerstat.assists}")
            print("----------")

    else:
        print("No players found.")

#displays the player with the most yellow and red cards together
def most_indisciplined_player():
    players = session.query(Player).all()
    indiscipline = []
    for player in players:
        player_stat = session.query(PlayerStat).filter_by(player_id=player.id).first()
        if player_stat:
            total_cards = player_stat.yellow_cards + player_stat.red_cards
            indiscipline.append((player.full_name, total_cards))
    if indiscipline:
        sorted_indiscipline = sorted(indiscipline, key=lambda x: x[1], reverse=True)
        most_indisciplined, total_cards = sorted_indiscipline[0]
        print(f"Most Indisciplined Player: {most_indisciplined} (Total Cards: {total_cards})")
    else:
        print("No player indiscipline found.")
    

#displays the top 50 players in goal contributions and generate a report on txt reflexting the same
def top_50_goal_contributions_report():
    players = session.query(Player).all()
    player_contributions = []
    for player in players:
        player_stat = session.query(PlayerStat).filter_by(player_id=player.id).first()
        if player_stat:
            contribution = player_stat.goals + player_stat.assists
            player_contributions.append((player.full_name, contribution))

    if player_contributions:
        sorted_contributions = sorted(player_contributions, key=lambda x: x[1], reverse=True)
        report_lines = []
        report_lines.append("Top 50 Players in Goal Contributions: ")
        report_lines.append("====================================")
        for i, (player, contribution) in enumerate(sorted_contributions[:50], start=1):
            report_lines.append(f"{i}. {player} (Contributions: {contribution})")
        report = "\n".join(report_lines)
        with open("top_goal_contributions_report.txt", "w") as file:
            file.write(report)

        print("Top 50 Players in Goal Contributions:")
        print("=====================================")
        for i, (player, contribution) in enumerate(sorted_contributions[:50], start=1):
            print(f"{i}. {player} (Contributions: {contribution})")

        print("Top 50 goal contributions report generated successfully.")
    else:
        print("No player contributions found.")
    


#this is the program menu for the user
def main_menu():
    # Add a 10-second delay with a progress bar
    for _ in tqdm(range(10), desc="Program Loading...", unit="s"):
        time.sleep(1)

    while True:
        print("===== FUATA DIMBA MENU =====")
        print("\n")
        print("TEAMS")
        print("........")
        print("\n")
        print("1). Find a Team")
        print("2). View All Teams")
        print("3). View Players in Team")
        print("4). Sort Teams by Goal Difference")
        print("5). Sort Teams by Wins")
        print("6). Sort Teams by Losses")
        print("\n")
        print("COACHES")
        print("........")
        print("\n")
        print("7). Find a Coach")
        print("8). View All Coaches")
        print("9). View Players for a Coach ")
        print("\n")
        print("PLAYERS & STATISTICS")
        print("........")
        print("\n")
        print("10). View All Players")
        print("11). View a Player's Statistics")
        print("12). Display Player with the Best Conversion Rate")
        print("13). Display Top 20 Scorers and Generate Report")
        print("14). Display Top 20 Assisters")
        print("15). Display Most Indisciplined Player")
        print("16). Display Top 50 Players in Goal Contributions and Generate Report")
        print("\n")
        print(".........")
        print("\n")
        print("0). Exit")
        print("\n")
        print(".........")
        print("\n")
        print("\n")

        choice = input("Enter your choice: ")
        if choice == "1":
            find_team()
        elif choice == "2":
            view_teams()
        elif choice == "3":
            players_in_team()
        elif choice == "4":
            sort_team_goal_difference()
        elif choice == "5":
            sort_team_wins()
        elif choice == "6":
            sort_team_losses()
        elif choice == "7":
            find_coach()
        elif choice == "8":
            view_coaches()
        elif choice == "9":
            view_coach_players()
        elif choice == "10":
            view_players()
        elif choice == "11":
            view_playerstat()
        elif choice == "12":
            best_conversion_rate()
        elif choice == "13":
            top_twenty_scorers_report()
        elif choice == "14":
            top_twenty_assisters()
        elif choice == "15":
            most_indisciplined_player()
        elif choice == "16":
            top_50_goal_contributions_report()
        elif choice == "0":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again")


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    session = Session()

    from models import Team, Coach, Player, PlayerStat, team_coach, team_player
    
    main_menu()