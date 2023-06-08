from sqlalchemy import ForeignKey, Column, Integer, String, MetaData, Table, create_engine, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%referred_table_name)s",
}

metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

if __name__ == '__main__':

    engine = create_engine('sqlite:///fuata_dimba.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    team_coach = Table(
    'team_coaches',
    Base.metadata,
    Column('team_id', ForeignKey('teams.id'), primary_key=True),
    Column('coach_id', ForeignKey('coaches.id'), primary_key=True),
    extend_existing=True
)

team_player = Table(
    'team_players',
    Base.metadata,
    Column('team_id', ForeignKey('teams.id'), primary_key=True),
    Column('player_id', ForeignKey('players.id'), primary_key=True),
    extend_existing=True
)


class Team(Base):
    __tablename__ = 'teams'

    id = Column(Integer(), primary_key=True)
    team_name = Column(String())
    played_games = Column(Integer, default=38)
    won_games = Column(Integer)
    lost_games = Column(Integer)
    drawn_games = Column(Integer)
    goals_scored = Column(Integer)
    goals_allowed = Column(Integer)
    goal_difference = Column(Integer)
    points = Column(Integer)

    coach_id = Column(Integer(), ForeignKey('coaches.id'), unique=True)

    players = relationship('Player', secondary=team_player, backref=backref('teams', lazy='dynamic'))


class Coach(Base):
    __tablename__ = 'coaches'

    id = Column(Integer(), primary_key=True)
    full_name = Column(String())
    nationality = Column(String())
    age = Column(Integer())

    players = relationship('Player', backref=backref('coach'))
    team = relationship('Team', backref=backref('coach', uselist=False))


class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer(), primary_key=True)
    full_name = Column(String())
    nationality = Column(String())
    age = Column(String())

    coach_id = Column(Integer(), ForeignKey('coaches.id'))


class PlayerStat(Base):
    __tablename__ = 'playerstats'

    id = Column(Integer(), primary_key=True)
    shots = Column(Integer())
    goals = Column(Integer())
    assists = Column(Integer())
    goal_contributions = Column(Integer())
    pass_completion_percentage = Column(Integer())
    clean_sheets = Column(Integer())
    conversion_rate = Column(Integer())
    yellow_cards = Column(Integer())
    red_cards = Column(Integer())
    player_id = Column(Integer(), ForeignKey("players.id"), unique=True)

    player = relationship('Player', backref=backref('playerstat', uselist=False))


    import ipdb; ipdb.set_trace()