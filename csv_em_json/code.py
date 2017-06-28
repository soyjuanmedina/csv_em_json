"""Create .json from csv."""

from functions import add_fields_to_table
import pandas as pd
import json
import numpy as np

# Load the table Dataset file
datasets_url = "csv/Datasets_Food Consumption Surveys_ Datasets Summary and Roadmap.csv"
datasets = pd.read_csv(datasets_url)

for dataset in datasets.iterrows():
    # Search for the Tables for this survey_abbreviation
    survey_abbreviation = dataset[1]['Survey Abbreviation']
    tables_url = 'csv/Table_MASTER Metadata All Tables.csv'
    registers = pd.read_csv(tables_url)
    tables = registers.loc[registers['Survey Abbreviation'] == survey_abbreviation]

    # Create the json structure
    dataset = dataset[1].replace(np.nan, '', regex=True)
    structure = dataset.to_dict()

    # Add tables to the dic
    structure['tables'] = []

    for table in tables.iterrows():
        # Avoid NaN and convert to a dictionary the
        table = table[1].replace(np.nan, '', regex=True)
        table_name = table['Table Name']

        # Build the file url and read it
        table_url = 'csv/Metadata_' + table['Creme Food ref'] + '.csv'
        registers = pd.read_csv(table_url)

        # Delete the unecesary columns and convert to a dictionary
        del table['Creme Food ref']
        structure_table = table.to_dict()

        # Add fields to the dic
        structure_table['fields'] = []

        # Add the fields of each table to the json
        structure_table['fields'] = add_fields_to_table(structure_table['fields'], registers, table_name)

        # Append the result to the tables array
        structure['tables'].append(structure_table)

    with open(survey_abbreviation + '.json', 'w') as outfile:
        json.dump(structure, outfile)
