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

# Remove rows with invalid or placeholder country names
df = df[~df["Country"].isin(["Global", "Other", "International conveyance (Diamond Princess)", "International conveyance (Solomon Islands)", "International conveyance (Kiribati)", "International commercial vessel"])]

# Fix encoding issues in country names
df["Country"] = df["Country"].replace({
    "C�te d'Ivoire": "Côte d'Ivoire",
    "R�union": "Réunion",
    "Cura�ao": "Curaçao",
    "S�o Tom� and Pr�ncipe": "São Tomé and Príncipe",
    "Saint Barth�lemy": "Saint Barthélemy"
})

# Convert numeric columns to appropriate data types
numeric_columns = [
    "Cumulative_Cases", "Cases_Per_100k", "New_Cases_7_Days", "New_Cases_7_Days_Per_100k", 
    "New_Cases_24_Hours", "Cumulative_Deaths", "Deaths_Per_100k", "New_Deaths_7_Days", 
    "New_Deaths_7_Days_Per_100k", "New_Deaths_24_Hours"
]

df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors="coerce")

# Drop unnecessary columns
df = df.drop(columns=["New_Cases_24_Hours", "New_Deaths_24_Hours"])

# Handle outliers in numeric data (e.g., extreme values in Cases_Per_100k)
for column in ["Cases_Per_100k", "Deaths_Per_100k"]:
    q1 = df[column].quantile(0.25)
    q3 = df[column].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    df[column] = df[column].clip(lower=lower_bound, upper=upper_bound)

# Create calculated fields
df["Death_Rate"] = (df["Cumulative_Deaths"] / df["Cumulative_Cases"]) * 100

# Save the updated cleaned dataset
df.to_csv("data/covid-data-cleaned.csv", index=False)

print("Additional cleaning complete. Updated cleaned data saved to 'data/covid-data-cleaned.csv'.")