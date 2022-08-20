import json
import pytest
from httpx import AsyncClient

from .main import router


# @pytest.mark.anyio
# async def test_root():
#     async with AsyncClient(app=router, base_url="http://localhost:8000/") as ac:
#         response = await ac.get("/api/v1/")
#     assert response.status_code == 200
#     assert response.json() == {'message': 'Hello World'}

@pytest.mark.anyio
async def test_create_new_user():
    async with AsyncClient(app=router, base_url="http://localhost:8000/") as ac:
        response = await ac.post("/api/v1/create/user", json = { "username": "mama", "age": 10, "team_id": 1 })
        print(response)
    assert response.status_code == 200
    print(response.json())
    # assert response.json() == { "username": "Jairon Landa", "age": 10, "team_id": 1 }