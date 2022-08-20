from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload

from .models import Team, User
from .schemas import UserBase, TeamBase

async def create_user(user: UserBase, session: AsyncSession):
    # db_user = User(name=user.name, age=user.age)
    db_user = User(**user.dict())
    session.add(db_user)
    await session.commit()
    await session.refresh(db_user)
    return db_user

async def create_team(team: TeamBase, session: AsyncSession):
    # db_user = User(name=user.name, age=user.age)
    db_team = Team(**team.dict())
    session.add(db_team)
    await session.commit()
    await session.refresh(db_team)
    return db_team

async def get_user(id: int, session: AsyncSession):

    return await session.get(User, id)

async def get_all_user(session: AsyncSession):
    result = await session.execute(select(User))

    return result.scalars().all()

async def get_all_team(session: AsyncSession):
    result = await session.execute(select(Team))

    return result.scalars().all()
    
async def get_team(id: int, session: AsyncSession):
    return await session.get(Team, id)

async def get_team_with_user(id: int, session: AsyncSession):
   
    query = select(Team).options(selectinload(Team.users)).where(Team.team_id == id)
    result = await session.execute(query)   

    team_data = []
    users_data = []
    for team in result.scalars().all():
        team_data.append({
            'team_id': team.team_id,
            'team_name': team.team_name,
            'users': None
        })
        for users in team.users:
            users_data.append({
                'user_id': users.user_id,
                'username': users.username,
                'age': users.age,
                'team_id': users.team_id
            })

    for value in team_data:
        value['users'] = users_data

    return team_data[0]

async def delete_user_with_id(id: int, session: AsyncSession):
    row = await session.execute(select(User).where(User.user_id == id))
    row = row.scalar_one()
    await session.delete(row)
    await session.commit()

async def update_user_by_id(id: int, user_update: UserBase, session: AsyncSession):

    if user_db:= await get_user(id, session=session):
        update_data = user_update.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(user_db, key, value)
    
        await session.commit()
        await session.refresh(user_db)
        return user_db
    else:
        return False
