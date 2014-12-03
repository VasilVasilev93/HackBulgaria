from sqlalchemy import Column, Integer, String, Float
import create_base

MAX_RATING = 10
MIN_RATING = 1


class Movie(create_base.Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    rating = Column(Float)

    def __str__(self):
        return "[{}] - {} ({})".format(self.id, self.name, self.rating)

    def __repr__(self):
        return self.__str__()
