# ApexPlanet Internship - Task 1

## Task Name
Data Cleaning and Preprocessing

## Objective
Clean and preprocess the provided sales dataset using Python.

## Tools Used
- Python
- Pandas
- NumPy
- OpenPyXL
- Visual Studio Code

## Dataset
ApexPlanet_DataAnalytics_Dataset.xlsx

## Steps Performed
- Loaded the dataset using Pandas.
- Explored dataset structure.
- Checked dataset shape and columns.
- Identified missing values.
- Checked duplicate records.
- Filled missing Age values using the median.
- Filled missing City values using the mode.
- Converted Order_Date to datetime format.
- Standardized text columns by removing extra spaces.
- Verified Total_Sales calculations.
- Saved the cleaned dataset.

## Output
- Cleaned_Sales_Dataset.xlsx

## Project Structure

ApexPlanet_Task1/
├── Dataset/
│   └── ApexPlanet_DataAnalytics_Dataset.xlsx
├── Scripts/
│   └── data_cleaning.py
├── Output/
│   └── Cleaned_Sales_Dataset.xlsx
└── README.md