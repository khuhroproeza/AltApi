import uvicorn
from fastapi import FastAPI

from src.routes import starwars


app = FastAPI()

app.include_router(starwars.router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8014)
