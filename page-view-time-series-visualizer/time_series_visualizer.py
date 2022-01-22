import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import datetime

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col = 0, parse_dates = True)

# Clean data
df = df[
  (df['value'] <= df['value'].quantile(0.975)) &
  (df['value'] >= df['value'].quantile(0.025))
]

def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize = (18, 7))
    sns.lineplot(data = df, color = 'red')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    fig.autofmt_xdate()

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['Years'] = df_bar.index.year
    df_bar['Months'] = df_bar.index.month_name()
    df_bar.rename(columns = {'value': 'Average Page Views'}, inplace = True)

    # Draw bar plot
    fig = plt.figure(figsize = (10, 10))
    
    hue_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    sns.barplot(x = "Years", y = "Average Page Views", hue = "Months", data = df_bar, hue_order = hue_order, errwidth = 0, saturation = 2, palette = 'deep')

    plt.legend(title = 'Months', loc = 'upper left')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace = True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2, figsize = (17, 8), sharey = True)
    sns.boxplot(x = 'year', y = 'value', data = df_box, ax = axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    axes[1] = sns.boxplot(x = 'month', y = 'value', data = df_box, ax = axes[1], order = order)
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
