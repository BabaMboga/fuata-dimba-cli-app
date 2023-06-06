from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker


from models import Team, Coach, Player, player_stats, team_coach

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
    