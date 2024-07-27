###################################### DataFrame in Pandas ###############################################
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

data = [
    {'Name': 'Alice_lst', 'Age': 25, 'City': 'New York'},
    {'Name': 'Bob_lst', 'Age': 30, 'City': 'Los Angeles'},
    {'Name': 'Charlie_lst', 'Age': 35, 'City': 'Chicago'},
    {'Name': 'kalpesh', 'Age': 31.5, 'City': None}
]

df = pd.DataFrame(data, index=['a', 'b', 'c','d'])

# print('----- head -----')
# print(df.head())  # View the first few rows
# print('----- tail -----')
# print(df.tail())  # View the last few rows


# print('----- Name -----')
# print(df['Name'])          # Select a single column
# print('----- Name,Age -----')
# print(df[['Name', 'Age']]) # Select multiple columns
# print('----- iloc -----')
# print(df.iloc[0])          # Select a row by position
# print('----- loc -----')
# print(df.loc['a'])           # Select a row by index

# print('------------------------------------')
# print(df['Age'] > 25) 
# print('----- Filtering Data -----')
# print(df[df['Age'] > 25])  # Filter rows based on a condition

df['Salary'] = [50000, 60000, 70000, 80000]  # Add a new column
# df = df.fillna(0)          # Replace missing values with 0
# df = df.dropna()           # Drop rows with missing values
df = df.drop('Salary', axis=1)        # Remove a column
# print( df)
# print('----- shape -----')
# print(df.shape)   # View the dimensions (rows, columns)
# print('----- info -----')
# print(df.info())  # View summary information
# print('----- describe -----')
# print(df.describe())  # View statistical summary

################################### merge two lists in Python #########################################

list1 = [1, 2, 3]
list2 = [4, 5, 1]

# merged_list = list1 + list2

# list1.extend(list2)
# print(list1)

# merged_list = [item for sublist in (list1, list2) for item in sublist]
# for sublist in (list1, list2) :
#     for item in sublist : 
#         print('item : ', item)

# merged_list = [*list1, *list2]

import itertools
merged_list = list(itertools.chain(list1, list2))
print(merged_list)


