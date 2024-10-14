from fastapi import FastAPI
from api.routes import ping

app = FastAPI(
    docs_url="/docs",
    redoc_url="/"
)

app.include_router(ping.router)