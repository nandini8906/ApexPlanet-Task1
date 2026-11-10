import pandas as pd
import numpy as np

# Load dataset
df = pd.read_excel("Dataset/ApexPlanet_DataAnalytics_Dataset.xlsx")

# -------------------------------
# Basic Information
# -------------------------------
print("First 5 Rows")
print(df.head())

print("\nDataset Shape")
print(df.shape)

print("\nColumn Names")
print(df.columns)

print("\nDataset Information")
df.info()

# -------------------------------
# Data Quality Assessment
# -------------------------------
print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicate Records")
df=df.drop_duplicates()

# -------------------------------
# Data Cleaning
# -------------------------------

# Fill missing Age with median
df["Age"] = df["Age"].fillna(df["Age"].median())

# Fill missing City with mode
df["City"] = df["City"].fillna(df["City"].mode()[0])

# Convert Order_Date to datetime
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Remove extra spaces from text columns
text_columns = [
    "Customer_Name",
    "Gender",
    "City",
    "Product",
    "Category"
]

for col in text_columns:
    df[col] = df[col].str.strip().str.title()

print("\nMissing Values After Cleaning")
print(df.isnull().sum())
# -------------------------------
# Verify Total Sales
# -------------------------------

df["Calculated_Sales"] = df["Quantity"] * df["Unit_Price"]

print("\nVerifying Total Sales")
print(df[["Quantity", "Unit_Price", "Total_Sales", "Calculated_Sales"]].head())
# Check if Total_Sales is correct


# Check if Total_Sales values are approximately equal
if np.allclose(df["Total_Sales"], df["Calculated_Sales"]):
    print("\n✅ Total_Sales values are correct.")
else:
    print("\n❌ Some Total_Sales values are incorrect.")
# Remove helper column
df.drop(columns=["Calculated_Sales"], inplace=True)

# Save the cleaned dataset
df.to_excel("Output/Cleaned_Sales_Dataset.xlsx", index=False)

print("\n✅ Cleaned dataset saved successfully!")