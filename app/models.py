from sqlalchemy import Integer, String, Column
from .database import Base


class Feedback(Base):
    __tablename__ = "feedback"
    id=Column(Integer, primary_key=True)
    feedback= Column(String)
    rating= Column(Integer)
    polarity = Column(Integer)
    subjectivity = Column(Integer)

