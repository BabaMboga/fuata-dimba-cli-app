# Fuata-Dimba-Cli-App

#### This python CLI appication will allow a user to see a database that contains players, player statistics, teams and coaches and generate a couple of reports based on user preferences. This allows user to get the data they need at their comfort and pleasure in no time and thus they can stay up to date on the latest football data. (version 1.08.06.2023)


#### This IP solely belongs to ** William Ayim **

## Description
Fuata Dimba is an application that provides detailed information to users on players, teams and coaches that they wish to access. It offers the fan a chance to stay up dated on current football data and allows them to get personalised data based on provided football statistics in the database. This eliminates the need for the user to access too many sources and get flooded with too much information that the player may not fully comprehend or need. We here at Fuata Dimba want the fan to have a more personalised football experience that not only leaves them satisfied but more knowledgable.

Fuata Dimba uses a personalised database with three distinct tables namely: coaches, teams and players that is regularly updated with current data.

The fan is able to:
- view all teams
- find a specific team
- view players in a team
- sort teams by goal difference
- sort teams by games won
- sort teams by games lost 
- find a coach
- view all coaches
- view players for a coach
- view all players
- view a player's statistics
- display player with the best conversion rate
- display top 20 scorers and generate report
- display top 20 assisters
- display most idisciplined player
- display top 50 players in goal contibutions and generate report

## Demo

Fork the repo and follow the setup below


## Setup/Installation Requirements IF yu need to contribute to the project

- One would need either linux or wsl for window users
- A copy of visual basic code installed
- A github account

1. Open your terminal and go to the directory you wish to work from.
2. Go to the following url using ur github account ("https://github.com/BabaMboga/fuata-dimba-cli-app")
3. Go to the code tab and clone the ssh key
4. Go back to the terminal and type git clone <-followed by the ssh key you copied /cloned ->
5. Enter your new cloned repository and type in code .
6. On the visual studio code that has now opened, go to the the run tab and hit start debugging.
7. Create a branch where you will make and add changes (git branch -b <branchname>)
8. Add the changes (git add .)
9. Commit changes (git commit -m "<add comment>")
10. Push your changes (git push origin <branchname>)
11. Use pipenv install and pipenv shell to install all dependencies
12. In the event the database is deleted run the models.py to create it then run seed data in this order teams, coaches, players & playerstats
12. Run the main.py and enjoy

## Technologies Used

This program is built with python 3.10.6 using the visual code environment.
It also has a database created using sqllite thus Slqalchemy is heavily employed.
The databases have seeded act that we can use

## Support and Contact Details

For any issues please email any of us on any of the below emails:

odhisayim@gmail.com

## License

Adventour is licensed under the Apache 2.0 License. See `LICENSE` for more information.

