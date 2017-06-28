from functions import add_fields_to_table
import pandas as pd
import json
import numpy as np

# Load the table Dataset file
datasets_url = "csv/Datasets_Food Consumption Surveys_ Datasets Summary and Roadmap.csv"
datasets = pd.read_csv(datasets_url)

for dataset in datasets.iterrows():
    # Ask for the json we go to build
    survey_abbreviation = dataset[1]['Survey Abbreviation']

    # Take only the row we go tu use
    selected_dataset = datasets.loc[datasets['Survey Abbreviation'] == survey_abbreviation]

    # Create the array to storege talbes for each dataset
    table_array = []

    # Read the document with all the tables
    tables_url = 'csv/Table_MASTER Metadata All Tables.csv'
    registers = pd.read_csv(tables_url)

    # Look for the tables we need
    selected_registers = registers.loc[registers['Survey Abbreviation'] == 'NHANES 2000']

    # Create the array to storege fields for each table
    fields_array = []

    # Loop for each table
    for table in selected_registers.iterrows():
        # Build the file url and read it
        table_name = table[1][1]
        table_url = 'csv/Metadata_' + table_name + '.csv'

        # Build the string with data from table
        fields = pd.read_csv(table_url)

        # Append the result to the tables array
        fields_array.append(fields)

    # Give each table his own fields
    selected_registers['fields'] = fields_array

    # Convert the dataset to string
    string = selected_registers.to_json(orient='records')

    selected_dataset['tables'] = selected_registers

    string2 = selected_dataset.to_json(orient='records')

# Writing the final json
with open('survey_abbreviation' + '.json', 'w') as outfile:
    outfile.write(string2)
