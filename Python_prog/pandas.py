

# WHAT IS PANDAS
# Pandas is a Python library used for working with data sets.
# It has functions for analyzing, cleaning, exploring, and manipulating data.

# DataFrames
# Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
# Series is like a column, a DataFrame is the whole table.

# to read .csv file
# import pandas as pd
#
# df = pd.read_csv('HRDataset_v14.csv')
#
# print(df.to_string())

# DICTIONARY TO DATAFRAME
# import pandas as pd
# dataF = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }
# df = pd.DataFrame.from_dict(dataF)
# print(df)


# LIST TO DATAFRAME
# import pandas as pd
# lst = ['Geeks', 'For', 'Geeks', 'is',
#        'portal', 'for', 'Geeks']
# df = pd.DataFrame(lst)
# print(df)

# TUPLE TO DATAFRAME
# from pandas import DataFrame as df
# tpl = ("Python", "Machine Learning", "Data Science", "Data Analyst")
# result = df(tpl, index=["a", "b", "c", "d"], columns=["Languages"])
# print(result)



print("completed")
