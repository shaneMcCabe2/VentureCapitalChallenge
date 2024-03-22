from LoadData import load_data

# Load in the dataframes
dataframes = load_data()

# Print basic details of each dataframe
for dataframe in dataframes:
    print(dataframes[dataframe].head())
    print(dataframes[dataframe].tail())
    print(dataframes[dataframe].info())
    print(dataframes[dataframe].describe())


