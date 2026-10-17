import pandas as pd
from sqlalchemy import create_engine

df = pd.read_parquet("parquet/taxi_data.parquet")

engine = create_engine("postgresql://postgres:shahed@localhost:5432/taxi_db")

df.to_sql(
    "taxi_trips",
    engine,
    if_exists="replace",
    index=False
)

print("Data loaded successfully")
