from fastapi import APIRouter, Depends, HTTPException
from client.api.controller.register_user import register_user
from client.api.controller.authentication import validate_token
from client.crud.user import get_user
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
register_user_router = APIRouter()


@register_user_router.post("/create_user")
async def register_user_endpoint(
    username: str,
    name: str,
    app_id: int,
    email_id: str,
    password: str = None,
    token: str = Depends(oauth2_scheme),
):
    if len(validate_token(token=token)) == 0:
        raise HTTPException(status_code=403, detail=f"Not authorized.")
    user_data = get_user({"username": username})
    if len(user_data) > 0:
        raise HTTPException(status_code=400, detail=f"{username} already exists.")
    register_user(
        {
            "username": username,
            "name": name,
            "app_id": app_id,
            "password": password,
            "email_id": email_id,
        }
    )
    return {"status": "user created successfully"}
