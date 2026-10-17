import pandas as pd
import os

os.makedirs("parquet", exist_ok=True)

# Read CSV files
csv1 = pd.read_csv("data/yellow_tripdata_2015-01.csv", nrows=10000)
csv2 = pd.read_csv("data/yellow_tripdata_2016.csv", nrows=10000)
csv3 = pd.read_csv("data/yellow_tripdata_2016-02.csv", nrows=10000)
csv4 = pd.read_csv("data/yellow_tripdata_2016-03.csv", nrows=10000)

json_data = pd.read_json("data/taxi_data.json.txt", lines=True)

combined_csv = pd.concat([csv1, csv2, csv3, csv4])

combined_csv.to_parquet(
    "parquet/taxi_data.parquet",
    engine="pyarrow",
    index=False
)

print("CSV and JSON files loaded successfully")
print("Parquet file created successfully")
