from fastapi import FastAPI
from sqlalchemy import text
from backend.database import engine

app = FastAPI()

@app.get("/crops")
async def show_data():
    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT * FROM crops LIMIT 10")
        )

        return [dict(row._mapping) for row in result]