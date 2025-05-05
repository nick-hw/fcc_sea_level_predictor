import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    
    # Create scatter plot
    plt.scatter(x, y)

    # Create first line of best fit
    line1 = linregress(x , y)
    x1_extended_all = np.arange(x.min(), 2051., 1)
    # x_extended = np.arange(x.min(), 2076., 25.)
    y1_extended = np.round(line1.slope * x1_extended_all + line1.intercept, decimals = 10)
    plt.plot(x1_extended_all, y1_extended, color = 'red')
             
    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    x_recent = df_recent['Year']
    y_recent = df_recent['CSIRO Adjusted Sea Level']
    line2 = linregress(x_recent , y_recent)
    x2_extended_all = np.arange(2000., 2051., 1)
    y2_extended = np.round(line2.slope * x2_extended_all + line2.intercept, decimals = 10)
    plt.plot(x2_extended_all, y2_extended, color = 'blue')
    
    # Add labels and title
    plt.xlabel("Year")
    plt.xticks(np.arange(1850., 2076., 25.))
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

def check_mismatches(arr1, arr2, decimal=7):
    # Check if shapes are equal
    if len(arr1) != len(arr2):
        raise ValueError("Arrays must have the same shape.")
    
    # Compute absolute difference and round to 7 decimals
    abs_diff = np.abs(arr1 - arr2)
    mismatches = abs_diff > 10**(-decimal)
    
    # Get indices where mismatches occur
    mismatch_indices = np.where(mismatches)
    
    # Print mismatched values (optional)
    for idx in zip(*mismatch_indices):
        print(f"Mismatch at index {idx}: {arr1[idx]} vs {arr2[idx]}")
    
    return mismatch_indices