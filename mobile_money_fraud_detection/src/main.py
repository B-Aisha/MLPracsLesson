import pandas as pd

# Step 1: Load the dataset
df = pd.read_csv("data/transactions.csv")
 # Step 2: Display the first five transactions
print("\nFIRST FIVE TRANSACTIONS")
print(df.head())

#Step 3: Dsiplay Dataset dimension
print("\nDATASET SHAPE")
print(df.shape)

#Step 4: Dsiplay column names
print("\nDATASET COLUMNS")
print(df.columns)

#step 5:display data types
print("\nDATA TYPES")
print(df.dtypes)

#step 6 Display dataset info
print("\nDATASET INFORMATION")
df.info

#step 7: Displaying statistical info
print("\nSTATISTICAL SUMMARY")
print(df.describe())

#How mamy legitimate transactions exist
print("\nFRAUD DISRIBUTION")
print(df["is_fraud"].value_counts())

# Calculate Percentages
print("\nFRAUD PERCENTAGES")
print(df["is_fraud"].value_counts(normalize=True) * 100)
# Calculate average transaction amount by class
print("\nAVERAGE TRANSACTION AMOUNT BY CLASS")
print(df.groupby("is_fraud")["transaction_amount"].mean())