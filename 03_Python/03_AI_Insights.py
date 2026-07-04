import pandas as pd

# Load Dataset
df = pd.read_csv("01_Dataset/fraudTrain.csv")

# Fraud Transactions
fraud_df = df[df["is_fraud"] == 1]

# Basic Statistics
total_transactions = len(df)
fraud_transactions = len(fraud_df)
fraud_rate = (fraud_transactions / total_transactions) * 100

print("========== AI INPUT ==========\n")

print(f"Total Transactions: {total_transactions}")
print(f"Fraud Transactions: {fraud_transactions}")
print(f"Fraud Rate: {fraud_rate:.2f}%")

print("\nTop Fraud Categories:")
print((fraud_df["category"].value_counts(normalize=True) * 100).head(5).round(2))

print("\nTop Fraud States:")
print(fraud_df["state"].value_counts().head(5))

print("\nFraud by Gender:")
print(fraud_df["gender"].value_counts())

print("\nAverage Fraud Amount:")
print(round(fraud_df["amt"].mean(), 2))