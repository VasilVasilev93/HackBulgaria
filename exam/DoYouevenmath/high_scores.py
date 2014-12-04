from create_base import Base
from sqlalchemy import Column, Integer, String


class HighScores(Base):
    __tablename__ = "HighScores"
    id = Column(Integer, primary_key=True)
    player_name = Column(String)
    points = Column(Integer)

    def __str__(self):
        return "{}. {} with {} points".format(self.id, self.player_name, self.points)

    def __repr__(self):
        return self.__str__()
