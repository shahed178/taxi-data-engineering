import os
import pandas as pd
from sqlalchemy import create_engine

df = pd.read_parquet("parquet/taxi_data.parquet")

engine = create_engine(os.environ["DATABASE_URL"])
df.to_sql(
    "taxi_trips",
    engine,
    if_exists="replace",
    index=False
)

print("Data loaded successfully")
