import uvicorn
from api import router as api_router
from core.config import settings

from fastapi import FastAPI

app = FastAPI()
app.include_router(
    api_router,
    prefix=settings.api.prefix,
)


if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )
