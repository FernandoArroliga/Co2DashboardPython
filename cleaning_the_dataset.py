# Importing the useful libraries and modules
import numpy as np
import pandas as pd

# Load the Data
data = pd.read_csv("owid-co2-data.csv")

# Function to clean data
def fill_na_values(data):
    
    data = data.fillna(0)
    return data 

def add_column(data):
    
    data["gdp_per_capita"] = np.where(data["population"] != 0, data["gdp"]/data["population"], 0) 
    return data 

def clean_data_module(data):
    
    non_na_data = fill_na_values(data)
    clean_data = add_column(data)
    
    # Export DataFrame to a CSV file
    return clean_data.to_csv("clean_data.csv", index=False)

# Run the main program
if __name__ == "__main__":
    clean_data_module(data)