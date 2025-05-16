import pandas as pd
import os

# Read the Abstracts.csv file
df = pd.read_csv('_data/Abstracts.csv')

# Convert Start Year to numeric, handling any non-numeric values
df['Start Year'] = pd.to_numeric(df['Start Year'], errors='coerce')

# Get the earliest and latest start dates
earliest_start = int(df['Start Year'].min())
latest_start = int(df['Start Year'].max())

# Create summary data
summary_df = pd.DataFrame({
    'Earliest start date': [earliest_start],
    'Latest start date': [latest_start]
})



# Check if the summary file exists

try:
    summary_df_existing = pd.read_csv('_data/summary.csv')
    # Check for missing columns and add them if needed
    for col in summary_df.columns:
        if col not in summary_df_existing.columns:
            summary_df_existing[col] = summary_df[col]
        else:
            # Update existing columns
            summary_df_existing[col].update(summary_df[col])
    
    summary_df_existing.to_csv('_data/summary.csv', index=False)
    print("Updated summary statistics in _data/summary.csv")
except FileNotFoundError:
    # Create a new file
    summary_df.to_csv('_data/summary.csv', index=False)
    print("Created summary statistics file _data/summary.csv")

