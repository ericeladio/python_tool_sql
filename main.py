import pandas as pd
import sqlite3





df = pd.read_csv('./data/categories.csv', encoding="ISO-8859-1")


# Creating our SQLite database.
conn = sqlite3.connect('database.db')
cursor = conn.cursor()


# insert the data from the DataFrame into the SQLite table
df.to_sql('categories', conn, if_exists='replace', index = False)

# Printing pandas dataframe
pd.read_sql('''SELECT * FROM orders ''', conn)
