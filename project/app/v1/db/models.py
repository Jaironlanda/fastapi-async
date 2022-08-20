from sqlalchemy import Column, Integer, String,  DateTime, ForeignKey
from sqlalchemy.orm import relationship, declarative_mixin

from datetime import datetime
from .config import Base


@declarative_mixin
class Timestamp:
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)


# Parrent
class Team(Timestamp, Base):

    __tablename__ = "teams"

    team_id = Column(Integer, primary_key=True)
    team_name = Column(String)

    users = relationship("User", back_populates="teams")

# Child
class User(Timestamp, Base):
    __tablename__ = "users"
    
    user_id = Column(Integer, primary_key=True)
    username = Column(String)
    age = Column(Integer)

    team_id = Column(Integer, ForeignKey("teams.team_id"), nullable=False)
    teams = relationship("Team", back_populates="users")