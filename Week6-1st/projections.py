from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
import create_base


class Projection(create_base.Base):
    __tablename__ = "projections"
    id = Column(Integer, primary_key=True)
    movieID = Column(Integer, ForeignKey("movies.id"))
    movie = relationship("Movie", backref="movieID")
    movie_type = Column(String)
    pdate = Column(String)
    ptime = Column(String)

    def __str__(self):
        return "{}| {} - {}".format(self.id, self.movie_type, self.ptime, self.pdate)

    def __repr__(self):
        return self.__str__()
