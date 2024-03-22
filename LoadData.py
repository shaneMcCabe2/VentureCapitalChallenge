import pandas as pd
import os 

## Load the datasets provided into Pandas DataFrames ##

def load_data():
    # Check if the data is already loaded and up to date
    if 'dataframes' in globals() and globals()['dataframes']:
        return globals()['dataframes']
    
    # Specify the folder path containing the CSV files
    folder_path_1 = 'C:/Users/Eilhart/Documents/OceanDataChallenges/VentureCapital/Data/dataset1'
    folder_path_2 = 'C:/Users/Eilhart/Documents/OceanDataChallenges/VentureCapital/Data'

    # Create a list containing the folders
    folders = [folder_path_1, folder_path_2]

    # Create an empty dictionary to store the DataFrames
    dataframes = {}

    # Iterate over the folders
    for folder in folders:
        # Iterate over the files in each folder
        for file_name in os.listdir(folder):
            # Check if the file has a .csv extension
            if file_name.endswith('.csv'):
                # Construct the full file path
                file_path = os.path.join(folder, file_name)
                
                # Extract the file name without the extension to use as the DataFrame name
                df_name = file_name.split('.')[0]
                
                # Read the CSV file into a DataFrame
                df = pd.read_csv(file_path)
                
                # Store the DataFrame in the dictionary with the corresponding name
                dataframes[df_name] = df

    # Store the loaded DataFrames in the global scope
    globals()['dataframes'] = dataframes

    return dataframes

