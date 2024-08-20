from fastapi import FastAPI

import uvicorn

app = FastAPI()


@app.get("/")
async def main():
    return {"message": "you lose"}


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)
