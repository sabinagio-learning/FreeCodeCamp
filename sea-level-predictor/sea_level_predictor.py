import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    df.plot.scatter(x = 'Year', y = 'CSIRO Adjusted Sea Level')

    # Create first line of best fit
    results = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    years = df['Year'].to_numpy()
    years = np.append(years, range(2014, 2051, 1))
    sea_level = lambda x: results.intercept + results.slope * x
    
    plt.plot(years, sea_level(years), 'r')

    # Create second line of best fit
    df_new = df[df["Year"] >= 2000]
    results_new = linregress(df_new['Year'], df_new["CSIRO Adjusted Sea Level"])

    years_new = df_new["Year"].to_numpy()
    years_new = np.append(years_new, range(2014, 2051, 1))
    sea_level_new = lambda x: results_new.intercept + results_new.slope * x

    plt.plot(years_new, sea_level_new(years_new), 'g')

    # Add labels and title
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()