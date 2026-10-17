import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load dataset

df = pd.read_csv("yellow_tripdata_2016-02.csv", nrows=10000)
print(" ####BEFORE CLEANING#### ")
print("Shape:", df.shape)
print("\nMissing Values:")
print(df.isnull().sum())


# Fill missing passenger_count with median
df["passenger_count"] = df["passenger_count"].fillna(

    df["passenger_count"].median()
)

# Fill missing fare_amount with mean
df["fare_amount"] = df["fare_amount"].fillna(

    df["fare_amount"].mean()
)
# REMOVE DUPLICATES
before_duplicates = df.shape[0]
df = df.drop_duplicates()
after_duplicates = df.shape[0]
print("\nDuplicates Removed:", before_duplicates - after_duplicates)

# REMOVE IRRELEVANT RECORDS
df = df[df["trip_distance"] > 0]
df = df[df["fare_amount"] >= 0]
df = df[df["total_amount"] >= 0]
df = df[df["passenger_count"] > 0]

# Convert datetime columns
df["tpep_pickup_datetime"] = pd.to_datetime(df["tpep_pickup_datetime"])
df["tpep_dropoff_datetime"] = pd.to_datetime(df["tpep_dropoff_datetime"])

# Create trip duration feature
df["trip_duration_minutes"] = (

    df["tpep_dropoff_datetime"] -

    df["tpep_pickup_datetime"]

).dt.total_seconds() / 60

# Create fare_per_mile feature
df["fare_per_mile"] = (

    df["fare_amount"] / df["trip_distance"]
)
# SCALING
scaler = MinMaxScaler()
df[["trip_distance"]] = scaler.fit_transform(

    df[["trip_distance"]]

)
# FEATURE SELECTION
selected_columns = [

    "VendorID",
    "passenger_count",

    "trip_distance",

    "fare_amount",

    "total_amount",

    "trip_duration_minutes",

    "fare_per_mile"
]

df = df[selected_columns]
print("\n AFTER CLEANING ")
print("Shape:", df.shape)
print("\nMissing Values:")
print(df.isnull().sum())

# SAVE CLEANED DATA
df.to_csv(

    "cleaned_taxi_data.csv",

    index=False
)
print("\nCleaned dataset saved successfully")
 
