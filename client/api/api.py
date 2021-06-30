from fastapi import APIRouter

from client.api.routes import data_collection, register_user, authenticate

api_router = APIRouter()
api_router.include_router(data_collection.data_import_router, tags=["data"])
api_router.include_router(register_user.register_user_router, tags=["user"])
api_router.include_router(authenticate.auth, tags=["authorization"])
