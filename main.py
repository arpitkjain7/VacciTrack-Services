from fastapi import FastAPI
from starlette.routing import Host
import uvicorn
from client.api.api import api_router

app = FastAPI()
if __name__ == "__main__":
    app.include_router(api_router)
    uvicorn.run(app, host="0.0.0.0", port=7000)
