import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import datetime
import matplotlib.ticker as mticker 

# Read CSV files using pandas
def read_csv_files(file1,file2):
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)
    return df1,df2
file1 = "../src/data/united22_23.csv"
file2 = "../src/data/united23_24.csv"

df_22_23, df_23_24 = read_csv_files(file1,file2)

print("Data for 2022/23 season:")
print(df_22_23.head())

print("Data for 2023/24 season:")
print(df_23_24.head())


# Convert Date to proper datetime format and extract the month
df_22_23['Date'] = pd.to_datetime(df_22_23['Date'])
df_22_23['Month'] = df_22_23['Date'].dt.month

# Total goals scored by united each month
def goals_scored_over_the_month(df):
    
    # Ensure the 'GF' column is numeric
    df['GF'] = pd.to_numeric(df['GF'], errors='coerce')
    # Group by month and sum the goals (GF), ensuring it is not cumulative
    goals_by_month = df.groupby('Month')['GF'].sum()

    # Sort the index based on the football season (Aug to May/Jun)
    month_order = [8, 9, 10, 11, 12, 1, 2, 3, 4, 5, 6]  # Aug to Jun
    goals_by_month = goals_by_month.reindex(month_order).fillna(0)  # Fill missing months with 0

    # Create the bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(goals_by_month.index, goals_by_month.values, color='red')
    plt.xlabel('Month')
    plt.ylabel('Total Goals Scored')
    plt.title('Manchester United Goals Scored by Month')

    # Fix the x-ticks to be labeled correctly for Aug to Jun
    month_labels = ['Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    plt.xticks(goals_by_month.index, month_labels)

    # --- Fixing the Y-Axis Formatting ---
    plt.gca().get_yaxis().set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{int(x)}'))  # Ensure normal integers
    plt.yticks(np.arange(0, goals_by_month.max() + 1, 5))  # Set y-ticks interval, adjust based on your data (e.g., 5)

    # Save the chart (optional)
    plt.savefig('goals_by_month_chart_fixed.png')

    # Show the chart
    plt.show()

# Call the function
#goals_scored_over_the_month(df_22_23)
goals_scored_over_the_month(df_23_24)

