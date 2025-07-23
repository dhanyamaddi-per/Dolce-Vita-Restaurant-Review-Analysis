# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 19:24:59 2024

@author: Harshyn
"""

import pandas as pd
import numpy as np

# Load the dataset
file_path = "c:/Users/Harshyn/Dolche Vita Reviews.csv" 
df = pd.read_csv(file_path) 
df.head() 

# Updated rating columns list with exact column names
rating_columns = ['Value Rating', 'Food Rating ', 'Service  Rating ', 'Atmosphere  Rating ']

# Clean and fill missing values in these columns
for col in rating_columns:
    # Remove text and convert to float
    df[col] = df[col].str.replace(" of 5 bubbles", "").astype(float)

# Fill missing values with the mean of each column
df[rating_columns] = df[rating_columns].apply(lambda x: x.fillna(x.mean()))

# Columns we want to modify
rating_columns = ['Value Rating', 'Food Rating ', 'Service  Rating ', 'Atmosphere  Rating ']

# Remove the decimal part by converting each value to integer
for col in rating_columns:
    df[col] = df[col].astype(float).astype(int)

# Display the first few rows to confirm the changes
df.head()

# Save the cleaned DataFrame to a new CSV file
output_file_path = "c:/Users/Harshyn/Cleaned_Dolche_Vita_Reviews.csv"
df.to_csv(output_file_path, index=False)