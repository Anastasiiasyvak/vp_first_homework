import pandas as pd
import matplotlib.pyplot as plt
plt.switch_backend('TkAgg')  # for creating a window of our graphics

# my file has coding UTF-16, so I point it like this
wine_data = pd.read_csv('vivno_dataset.csv', encoding='UTF-16')

# print(wine_data.head()) # we use this to first of all understand whether
# # we have access to our data and also to see if the date is displayed correctly
# # (namely the first 5 lines)
#
# print(wine_data.info())  # my general info about dataset(number of rows and columns, data types..)
#
# print(wine_data.isnull().sum()) # This command displays the number of missing values in each column
# # the isnull() true -> for NaN false->for not NaN, sum() converts false to zero so in my case I don't have missing values

#===================================================

# Data Cleaning

# so here we replace all NaN values in the ABV % column with the average value of this column
wine_data['ABV %'].fillna(wine_data['ABV %'].mean(), inplace=True)


#====================================================

# data vizualization


#name - name of the wine
#color_wine - color of the wine
# Prices - price of the wine
# ML - Wine volume in millilitres
# Ratings - rating of wine
# Ratingsnum - Number of ratings determining the ratings
# Countrys - country of wine
# ABV% - The alcohol content of wine is shown as a percentage
# rates - addition ratings or information


# bar chart
wine_data['color_wine'].value_counts().plot(kind='bar', color=['skyblue', 'lightcoral']) # count our color_wine and realization of it
plt.title('Distribution of Wine Colors') # the name
plt.xlabel('Wine Color') # for x
plt.ylabel('Count') # for y


# adding annotations (text labels) to each column
for i, count in enumerate(wine_data['color_wine'].value_counts()):
    plt.text(i, count + 0.1, str(count), ha='center', va='bottom')

plt.show() # creating and show this bar chart

# line chart


