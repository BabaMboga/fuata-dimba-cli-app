from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Team, Coach, Player, player_stats, team_coach


if __name__ == '__main__':
    engine = create_engine('sqlite:///fuata_dimba.db')
    Session = sessionmaker(bind=engine)
    session = Session()