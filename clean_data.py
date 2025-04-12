import pandas as pd

# Load the dataset
data_path = "data/covid-data.csv"
df = pd.read_csv(data_path)

# Standardize column names
df.columns = [
    "Country", "Region", "Cumulative_Cases", "Cases_Per_100k", "New_Cases_7_Days", 
    "New_Cases_7_Days_Per_100k", "New_Cases_24_Hours", "Cumulative_Deaths", 
    "Deaths_Per_100k", "New_Deaths_7_Days", "New_Deaths_7_Days_Per_100k", "New_Deaths_24_Hours"
]

# Handle missing values (replace empty strings with NaN)
df = df.replace("", pd.NA)

# Drop rows with missing critical data (e.g., Country, Cumulative_Cases, Cumulative_Deaths)
df = df.dropna(subset=["Country", "Cumulative_Cases", "Cumulative_Deaths"])

# Convert numeric columns to appropriate data types
numeric_columns = [
    "Cumulative_Cases", "Cases_Per_100k", "New_Cases_7_Days", "New_Cases_7_Days_Per_100k", 
    "New_Cases_24_Hours", "Cumulative_Deaths", "Deaths_Per_100k", "New_Deaths_7_Days", 
    "New_Deaths_7_Days_Per_100k", "New_Deaths_24_Hours"
]

df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors="coerce")

# Create calculated fields
df["Death_Rate"] = (df["Cumulative_Deaths"] / df["Cumulative_Cases"]) * 100

# Save the cleaned dataset
df.to_csv("data/covid-data-cleaned.csv", index=False)

print("Data cleaning and transformation complete. Cleaned data saved to 'data/covid-data-cleaned.csv'.")