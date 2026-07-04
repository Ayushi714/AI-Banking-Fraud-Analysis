import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("01_Dataset/fraudTrain.csv")

#Fraud vs Non Fraud Count
fraud_count = df["is_fraud"].value_counts()

plt.figure(figsize=(6,4))
fraud_count.plot(kind="bar")
plt.title("Fraud vs Non Fraud Transactions")
plt.xlabel("Fraud")
plt.ylabel("Count")
plt.savefig("07_Images/Fraud_vs_NonFraud.png")
plt.show()
plt.close()

#Top Fraud Categories
fraud_df = df[df["is_fraud"] == 1]

top_categories = fraud_df["category"].value_counts().head(10)

plt.figure(figsize=(10,5))
top_categories.plot(kind="bar")
plt.title("Top 10 Fraud Categories")
plt.xlabel("Category")
plt.ylabel("Fraud Count")
plt.xticks(rotation=45)
plt.savefig("07_Images/Top_Fraud_Categories.png")
plt.show()
plt.close()

#Fraud by Gender
gender = fraud_df["gender"].value_counts()

plt.figure(figsize=(5,5))
gender.plot(kind="pie", autopct="%1.1f%%")
plt.title("Fraud by Gender")
plt.ylabel("")
plt.savefig("07_Images/Fraud_by_Gender.png")
plt.show()
plt.close()

#Top Fraud States
state = fraud_df["state"].value_counts().head(10)

plt.figure(figsize=(8,5))
state.plot(kind="bar")
plt.title("Top Fraud States")
plt.xlabel("State")
plt.ylabel("Fraud Count")
plt.savefig("07_Images/Top_Fraud_States.png")
plt.show()
plt.close()

#Transaction Amount Distribution
plt.figure(figsize=(8,5))
df["amt"].hist(bins=50)
plt.title("Transaction Amount Distribution")
plt.xlabel("Amount")
plt.ylabel("Frequency")
plt.savefig("07_Images/Transaction_Amount_Distribution.png")
plt.show()
plt.close()