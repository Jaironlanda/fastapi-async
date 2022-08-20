from datetime import datetime
from mimetypes import init
from time import clock_settime
from typing import Optional, List, Tuple, Union
from pydantic import BaseModel


class UserBase(BaseModel):
    username: Optional[str]
    age: Optional[int] = 0
    

class User(UserBase):
    user_id: int
    team_id: int

    class Config:
        orm_mode = True

class UserCreate(UserBase):
    team_id: int

class TeamBase(BaseModel):
    team_name: str

class Team(TeamBase):
    team_id: int

    class Config:
        orm_mode = True

class TeamWithUser(Team):
    users: List[User] = None
