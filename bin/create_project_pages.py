import pandas as pd
import os

# Load the Abstracts.csv file
abstracts_df = pd.read_csv('_data/Abstracts.csv')
datasets_df = pd.read_csv('_data/Datasets.csv')

# Ensure the _projects directory exists
os.makedirs('_projects', exist_ok=True)

# Iterate through each row and create a Jekyll stub file
for index, row in abstracts_df.iterrows():
    filename = f"_projects/{row['Proj ID']}.md"
    with open(filename, 'w') as file:
        file.write('---\n')
        file.write(f"title: \"{row['Title']}\"\n")
        file.write(f"proj_id: \"{row['Proj ID']}\"\n")
        file.write(f"status: \"{row['Status']}\"\n")
        file.write(f"rdc: \"{row['RDC']}\"\n")
        file.write(f"start_year: \"{row['Start Year']}\"\n")
        file.write(f"end_year: \"{row['End Year']}\"\n")
        file.write(f"pi: \"{row['PI']}\"\n")
        file.write(f"abstract: \"{row['Abstract']}\"\n")
        file.write('---\n\n')


        # Add a section with a list of datasets used
        file.write("**Datasets Used:**\n")
        datasets = datasets_df[datasets_df['Proj ID'] == row['Proj ID']]['Data Name'].tolist()
        if datasets:
            file.write("\n")
            for dataset in datasets:
                file.write(f"  - {dataset} \n")
            file.write("\n")
        else:
            file.write("\nNo datasets listed.\n")
        
print("Jekyll stubs created in _projects directory.")