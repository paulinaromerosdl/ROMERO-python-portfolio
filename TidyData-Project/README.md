The aim for this project is to be able to analyze a dataset that contains information about sports and gender-based medal counts through the use of Tidy Data Principles. These principles help format the data, and clean null values to make the data more readable. 

Some features included in this project are: columns, rows, visualization types, and tables. 

To be able to run the notebook make sure you have Python libraries installed- if you do not have a Python library you can install it using the 'pip':'''bash 
pip install pandas matplotlib command in your terminal

As previously mentioned this dataset contains information on medal counts across various sports, the columns included are Sport_gender which show the specific category of gender in a sport. Then medalist_name is the name of the medalist, and medals the number of medals. 

Some of the preprocessing steps included replaced the 'NaN' values with a 0 to handle the missing data, then reformatting the data set using the 'pd.melt()' design, and finally splitting the sport_gender column into a separate column for sport, and a separate column for gender. 

References used: 

Pandas Cheat Sheet: https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf

Tidy Data Principles: https://vita.had.co.nz/papers/tidy-data.pdf
