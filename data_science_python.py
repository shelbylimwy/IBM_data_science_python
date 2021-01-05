import pandas as pd

file_path = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%204/Datasets/TopSellingAlbums.csv"

data = pd.read_csv(file_path)

df = pd.DataFrame(data)

date = df[['Released', 'Album', 'Artist']]

# Quiz 1: Use a variable q to store the column Rating as a dataframe

q = df[['Rating']]

# Quiz 2: Assign the variable q to the dataframe that is made up of the column Released and Artist

q = df[['Released', 'Artist']]

# Quiz 3: Access the 2nd row and the 3rd column of df

df.iloc[1, 2]

# Quiz 4: Use the following list to convert the dataframe index df to characters and assign it to df_new; 
# find the element corresponding to the row index a and column 'Artist'. 
# Then select the rows a through d for the column 'Artist'

# new_index=['a','b','c','d','e','f','g','h']

new_index=['a','b','c','d','e','f','g','h']

df_new = df
df_new.index = new_index
df_new.loc['a', 'Artist']
df_new.loc['a':'d', 'Artist']