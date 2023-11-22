import pandas as pd

# my file has coding UTF-16, so I point it like this
wine_data = pd.read_csv('vivno_dataset.csv', encoding='UTF-16')

print(wine_data.head()) # we use this to first of all understand whether
# we have access to our data and also to see if the date is displayed correctly
# (namely the first 5 lines)

print(wine_data.info())  # my general info about dataset(number of rows and columns, data types..)

print(wine_data.isnull().sum()) # This command displays the number of missing values in each column
# the isnull() true -> for NaN false->for not NaN, sum() converts false to zero so in my case I don't have missing values
