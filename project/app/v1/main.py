from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from .db.models import Team, User
from .db.config import get_session
from .db.utils import create_user, create_team, get_user, get_all_user, get_team_with_user, get_all_team, delete_user_with_id, update_user_by_id
from .db.schemas import TeamBase, User, UserBase, TeamWithUser, Team, UserCreate



router = APIRouter(prefix="/api/v1")


@router.get('/')
async def root():
    return {'message': 'Hello World'}

@router.post("/create/user", response_model= User)
async def create_new_user(user: UserCreate, session: AsyncSession = Depends(get_session)):
    
    return await create_user(user, session=session)

@router.post("/create/team", response_model= Team)
async def create_new_team(team: TeamBase, session: AsyncSession = Depends(get_session)):
    
    return await create_team(team, session=session)

@router.get("/user/{id}", response_model= User)
async def get_user_id(id: int, session: AsyncSession = Depends(get_session)):
    
    return await get_user(id, session=session)

@router.get("/users", response_model= List[User])
async def get_all(session: AsyncSession = Depends(get_session)):
    user = await get_all_user(session=session)

    return user

@router.get("/teams", response_model= List[Team])
async def get_all(session: AsyncSession = Depends(get_session)):
    team = await get_all_team(session=session)

    return team

@router.get("/user/team/{id}", response_model=TeamWithUser)
async def get_teamate(id: int, session: AsyncSession = Depends(get_session)):
    data = await get_team_with_user(id, session=session)
    
    return data

@router.delete('/user/{id}')
async def delete_user(id: int, session: AsyncSession = Depends(get_session)):
    
    # check first
    data = await get_user(id, session=session)

    if data:
        res = await delete_user_with_id(id, session=session)
        print(res)

    raise HTTPException(status_code=200, detail="User with ID {}  not exist!".format(id))

@router.put('/user/{id}', response_model = User)
async def update_user(id: int, user: UserBase, session: AsyncSession = Depends(get_session)):
    
    if data:= await update_user_by_id(id, user, session=session):
        return data

    raise HTTPException(status_code=404, detail="User with ID {}  not exist!".format(id))
    