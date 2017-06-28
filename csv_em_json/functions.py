"""All usual function used by script."""

# Import the necesary libraries
import numpy as np


def add_fields_to_table(array, registers, table_name = ''):
    """Convert the registers of .csv in a dict to add the json."""
    registers1 = registers.replace(np.nan, '', regex=True)
    registers1['Field data type'] = 'text'
    registers1['Keys'] = ''
    array_food_code = [{"table": "Food", "field": "Food Code"}]
    array_subject_code = [{"table": "Subject", "field": "Subject Code"}]
    if 'Subjects' in table_name:
        registers1['Field data type'][registers1['Field'] == 'Height'] = 'Numeric'
        registers1['Field data type'][registers1['Field'] == 'Bodyweight'] = 'Numeric'
        registers1['Field data type'][registers1['Field'] == 'Age'] = 'Numeric'
        registers1['Field data type'][registers1['Field'] == 'Weighting'] = 'Numeric'
        registers1['Field data type'][registers1['Field'] == 'Day Count'] = 'Integer'
    elif 'Diary' in table_name:
        registers1['Field data type'][registers1['Field'] == 'Day'] = 'Integer'
        registers1['Keys'][registers1['Field'] == 'Food Code'] = array_food_code
        registers1['Keys'][registers1['Field'] == 'Subject Code'] = array_subject_code
    elif 'Nutrients' in table_name:
        registers1['Field data type'][registers1['Field'] == 'Concentration'] = 'Numeric Distribution'
        registers1['Keys'][registers1['Field'] == 'Food Code'] = array_food_code
    # elif 'Groups' in table_name:
    #     print('Groups')

    fields = registers1.to_dict(orient='records')
    array = fields
    return array
