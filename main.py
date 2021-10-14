import time
import os
from typing import Optional

from sqlalchemy.exc import OperationalError
from sqlalchemy.engine import URL
from sqlmodel import Field, Session, SQLModel, create_engine, select

from loguru import logger


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None


def main():
    hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
    hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
    hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)

    host_name = "postgres" if os.environ.get("IS_INSIDE_DOCKER") else "localhost"
    url = URL.create(drivername="postgresql", username="postgres", password="changeme", host=host_name, port=5432)
    engine = create_engine(url)
    for _ in range(5):
        try:
            SQLModel.metadata.create_all(engine)
            break
        except OperationalError:
            logger.error("Is postgres database running?")
            time.sleep(2)

    with Session(engine) as session:
        session.add_all([hero_1, hero_2])
        session.add(hero_3)
        session.commit()

    with Session(engine) as session:
        statement = select(Hero).where(Hero.name == "Spider-Boy")
        hero = session.exec(statement).first()
        logger.info(hero)


if __name__ == '__main__':
    main()
