import pandas as pd

# Load Dataset
df = pd.read_csv("01_Dataset/fraudTrain.csv")

# Show first 5 rows
print(df.head())
# Shape of dataset
print("Dataset Shape:", df.shape)

# Column names
print("\nColumns:")
print(df.columns)

# Dataset information
print("\nDataset Info:")
print(df.info())

# Statistical Summary
print(df.describe())

# Missing Values
print(df.isnull().sum())

# Check Missing Values
print("Missing Values:")
print(df.isnull().sum())

# Check Duplicate Rows
print("\nDuplicate Rows:", df.duplicated().sum())

# Dataset Shape
print("\nShape:", df.shape)

# Remove unwanted column
df.drop("Unnamed: 0", axis=1, inplace=True)

# Convert columns to datetime
df["trans_date_trans_time"] = pd.to_datetime(df["trans_date_trans_time"])
df["dob"] = pd.to_datetime(df["dob"])

# Check updated dataset information
print(df.info())

# Display first 5 rows
print(df.head())

# Extract date and time features
df["transaction_hour"] = df["trans_date_trans_time"].dt.hour
df["transaction_day"] = df["trans_date_trans_time"].dt.day
df["transaction_month"] = df["trans_date_trans_time"].dt.month
df["transaction_weekday"] = df["trans_date_trans_time"].dt.day_name()

# Customer Age
df["customer_age"] = (
    df["trans_date_trans_time"].dt.year - df["dob"].dt.year
)

# Check new columns
print(df[[
    "trans_date_trans_time",
    "transaction_hour",
    "transaction_day",
    "transaction_month",
    "transaction_weekday",
    "customer_age"
]].head())

# Total Transactions
print("Total Transactions:", len(df))

# Total Fraud Transactions
print("Total Fraud Transactions:", df["is_fraud"].sum())

# Fraud Percentage
fraud_percentage = (df["is_fraud"].mean()) * 100
print("Fraud Percentage:", round(fraud_percentage, 2), "%")

# Average Transaction Amount
print("Average Transaction Amount:", round(df["amt"].mean(), 2))

# Highest Transaction Amount
print("Highest Transaction Amount:", df["amt"].max())

# Lowest Transaction Amount
print("Lowest Transaction Amount:", df["amt"].min())

# Fraud transactions only
fraud_df = df[df["is_fraud"] == 1]

# Fraud count by category
fraud_by_category = fraud_df.groupby("category").size().sort_values(ascending=False)

print("Top 10 Fraud Categories:")
print(fraud_by_category.head(10))

# Fraud count by state
fraud_by_state = fraud_df.groupby("state").size().sort_values(ascending=False)

print("\nTop 10 Fraud States:")
print(fraud_by_state.head(10))

# Fraud by gender
fraud_by_gender = fraud_df.groupby("gender").size()

print("\nFraud by Gender:")
print(fraud_by_gender)

# Total transactions by category
total_by_category = df.groupby("category").size()

# Fraud transactions by category
fraud_by_category = df[df["is_fraud"] == 1].groupby("category").size()

# Fraud rate
fraud_rate = ((fraud_by_category / total_by_category) * 100).sort_values(ascending=False)

print("Fraud Rate by Category (%):")
print(fraud_rate.round(2))