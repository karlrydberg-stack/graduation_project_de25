import pandas as pd
from sqlalchemy import text
from backend.constants import DATA_PATH
from backend.database import engine

df = pd.read_csv(
    DATA_PATH / "total_harvest_area.csv",
    encoding="latin-1"
)

df = df.fillna("Missing")

with engine.begin() as connection:
    df.to_sql(
        "crops",
        con=connection,
        if_exists="replace",
        index=False
    )

print("to_sql completed")

with engine.connect() as connection:
    count = connection.execute(
        text("SELECT COUNT(*) FROM crops")
    ).scalar()

    print("ROWS IN CROPS:", count)