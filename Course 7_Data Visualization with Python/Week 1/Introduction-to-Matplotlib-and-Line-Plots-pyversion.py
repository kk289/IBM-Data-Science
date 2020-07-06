#!/usr/bin/env python
# coding: utf-8

# <a href="https://cognitiveclass.ai"><img src = "https://ibm.box.com/shared/static/9gegpsmnsoo25ikkbl4qzlvlyjbgxs5x.png" width = 400> </a>
# 
# <h1 align=center><font size = 5>Introduction to Matplotlib and Line Plots</font></h1>

# ## Introduction
# 
# The aim of these labs is to introduce you to data visualization with Python as concrete and as consistent as possible. 
# Speaking of consistency, because there is no *best* data visualization library avaiblable for Python - up to creating these labs - we have to introduce different libraries and show their benefits when we are discussing new visualization concepts. Doing so, we hope to make students well-rounded with visualization libraries and concepts so that they are able to judge and decide on the best visualitzation technique and tool for a given problem _and_ audience.
# 
# Please make sure that you have completed the prerequisites for this course, namely <a href='http://cocl.us/PY0101EN_DV0101EN_LAB1_Coursera'>**Python for Data Science**</a> and <a href='http://cocl.us/DA0101EN_DV0101EN_LAB1_Coursera'>**Data Analysis with Python**</a>, which are part of this specialization. 
# 
# **Note**: The majority of the plots and visualizations will be generated using data stored in *pandas* dataframes. Therefore, in this lab, we provide a brief crash course on *pandas*. However, if you are interested in learning more about the *pandas* library, detailed description and explanation of how to use it and how to clean, munge, and process data stored in a *pandas* dataframe are provided in our course <a href='http://cocl.us/DA0101EN_DV0101EN_LAB1_Coursera'>**Data Analysis with Python**</a>, which is also part of this specialization. 
# 
# ------------

# ## Table of Contents
# 
# <div class="alert alert-block alert-info" style="margin-top: 20px">
# 
# 1. [Exploring Datasets with *pandas*](#0)<br>
# 1.1 [The Dataset: Immigration to Canada from 1980 to 2013](#2)<br>
# 1.2 [*pandas* Basics](#4) <br>
# 1.3 [*pandas* Intermediate: Indexing and Selection](#6) <br>
# 2. [Visualizing Data using Matplotlib](#8) <br>
# 2.1 [Matplotlib: Standard Python Visualization Library](#10) <br>
# 3. [Line Plots](#12)
# </div>
# <hr>

# # Exploring Datasets with *pandas* <a id="0"></a>
# 
# *pandas* is an essential data analysis toolkit for Python. From their [website](http://pandas.pydata.org/):
# >*pandas* is a Python package providing fast, flexible, and expressive data structures designed to make working with “relational” or “labeled” data both easy and intuitive. It aims to be the fundamental high-level building block for doing practical, **real world** data analysis in Python.
# 
# The course heavily relies on *pandas* for data wrangling, analysis, and visualization. We encourage you to spend some time and  familizare yourself with the *pandas* API Reference: http://pandas.pydata.org/pandas-docs/stable/api.html.

# ## The Dataset: Immigration to Canada from 1980 to 2013 <a id="2"></a>

# Dataset Source: [International migration flows to and from selected countries - The 2015 revision](http://www.un.org/en/development/desa/population/migration/data/empirical2/migrationflows.shtml).
# 
# The dataset contains annual data on the flows of international immigrants as recorded by the countries of destination. The data presents both inflows and outflows according to the place of birth, citizenship or place of previous / next residence both for foreigners and nationals. The current version presents data pertaining to 45 countries.
# 
# In this lab, we will focus on the Canadian immigration data.
# 
# <img src = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DV0101EN/labs/Images/Mod1Fig1-Dataset.png" align="center" width=900>
# 
# For sake of simplicity, Canada's immigration data has been extracted and uploaded to one of IBM servers. You can fetch the data from [here](https://ibm.box.com/shared/static/lw190pt9zpy5bd1ptyg2aw15awomz9pu.xlsx).
# 
# ---

# ## *pandas* Basics<a id="4"></a>

# The first thing we'll do is import two key data analysis modules: *pandas* and **Numpy**.

# In[1]:


import numpy as np  # useful for many scientific computing in Python
import pandas as pd # primary data structure library


# Let's download and import our primary Canadian Immigration dataset using *pandas* `read_excel()` method. Normally, before we can do that, we would need to download a module which *pandas* requires to read in excel files. This module is **xlrd**. For your convenience, we have pre-installed this module, so you would not have to worry about that. Otherwise, you would need to run the following line of code to install the **xlrd** module:
# ```
# !conda install -c anaconda xlrd --yes
# ```

# Now we are ready to read in our data.

# In[2]:


df_can = pd.read_excel('https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DV0101EN/labs/Data_Files/Canada.xlsx',
                       sheet_name='Canada by Citizenship',
                       skiprows=range(20),
                       skipfooter=2)

print ('Data read into a pandas dataframe!')


# Let's view the top 5 rows of the dataset using the `head()` function.

# In[3]:


df_can.head()
# tip: You can specify the number of rows you'd like to see as follows: df_can.head(10) 


# We can also veiw the bottom 5 rows of the dataset using the `tail()` function.

# In[4]:


df_can.tail()


# When analyzing a dataset, it's always a good idea to start by getting basic information about your dataframe. We can do this by using the `info()` method.

# In[5]:


df_can.info()


# To get the list of column headers we can call upon the dataframe's `.columns` parameter.

# In[6]:


df_can.columns.values 


# Similarly, to get the list of indicies we use the `.index` parameter.

# In[7]:


df_can.index.values


# Note: The default type of index and columns is NOT list.

# In[8]:


print(type(df_can.columns))
print(type(df_can.index))


# To get the index and columns as lists, we can use the `tolist()` method.

# In[9]:


df_can.columns.tolist()
df_can.index.tolist()

print (type(df_can.columns.tolist()))
print (type(df_can.index.tolist()))


# To view the dimensions of the dataframe, we use the `.shape` parameter.

# In[14]:


# size of dataframe (rows, columns)
df_can.shape    


# Note: The main types stored in *pandas* objects are *float*, *int*, *bool*, *datetime64[ns]* and *datetime64[ns, tz] (in >= 0.17.0)*, *timedelta[ns]*, *category (in >= 0.15.0)*, and *object* (string). In addition these dtypes have item sizes, e.g. int64 and int32. 

# Let's clean the data set to remove a few unnecessary columns. We can use *pandas* `drop()` method as follows:

# In[15]:


# in pandas axis=0 represents rows (default) and axis=1 represents columns.
df_can.drop(['AREA','REG','DEV','Type','Coverage'], axis=1, inplace=True)
df_can.head(2)


# Let's rename the columns so that they make sense. We can use `rename()` method by passing in a dictionary of old and new names as follows:

# In[ ]:


df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True)
df_can.columns


# We will also add a 'Total' column that sums up the total immigrants by country over the entire period 1980 - 2013, as follows:

# In[ ]:


df_can['Total'] = df_can.sum(axis=1)


# We can check to see how many null objects we have in the dataset as follows:

# In[ ]:


df_can.isnull().sum()


# Finally, let's view a quick summary of each column in our dataframe using the `describe()` method.

# In[ ]:


df_can.describe()


# ---
# ## *pandas* Intermediate: Indexing and Selection (slicing)<a id="6"></a>
# 

# ### Select Column
# **There are two ways to filter on a column name:**
# 
# Method 1: Quick and easy, but only works if the column name does NOT have spaces or special characters.
# ```python
#     df.column_name 
#         (returns series)
# ```
# 
# Method 2: More robust, and can filter on multiple columns.
# 
# ```python
#     df['column']  
#         (returns series)
# ```
# 
# ```python 
#     df[['column 1', 'column 2']] 
#         (returns dataframe)
# ```
# ---

# Example: Let's try filtering on the list of countries ('Country').

# In[ ]:


df_can.Country  # returns a series


# Let's try filtering on the list of countries ('OdName') and the data for years: 1980 - 1985.

# In[ ]:


df_can[['Country', 1980, 1981, 1982, 1983, 1984, 1985]] # returns a dataframe
# notice that 'Country' is string, and the years are integers. 
# for the sake of consistency, we will convert all column names to string later on.


# ### Select Row
# 
# There are main 3 ways to select rows:
# 
# ```python
#     df.loc[label]        
#         #filters by the labels of the index/column
#     df.iloc[index]       
#         #filters by the positions of the index/column
# ```

# Before we proceed, notice that the defaul index of the dataset is a numeric range from 0 to 194. This makes it very difficult to do a query by a specific country. For example to search for data on Japan, we need to know the corressponding index value.
# 
# This can be fixed very easily by setting the 'Country' column as the index using `set_index()` method.

# In[ ]:


df_can.set_index('Country', inplace=True)
# tip: The opposite of set is reset. So to reset the index, we can use df_can.reset_index()


# In[ ]:


df_can.head(3)


# In[ ]:


# optional: to remove the name of the index
df_can.index.name = None


# Example: Let's view the number of immigrants from Japan (row 87) for the following scenarios:
#     1. The full row data (all columns)
#     2. For year 2013
#     3. For years 1980 to 1985

# In[ ]:


# 1. the full row data (all columns)
print(df_can.loc['Japan'])

# alternate methods
print(df_can.iloc[87])
print(df_can[df_can.index == 'Japan'].T.squeeze())


# In[ ]:


# 2. for year 2013
print(df_can.loc['Japan', 2013])

# alternate method
print(df_can.iloc[87, 36]) # year 2013 is the last column, with a positional index of 36


# In[ ]:


# 3. for years 1980 to 1985
print(df_can.loc['Japan', [1980, 1981, 1982, 1983, 1984, 1984]])
print(df_can.iloc[87, [3, 4, 5, 6, 7, 8]])


# Column names that are integers (such as the years) might introduce some confusion. For example, when we are referencing the year 2013, one might confuse that when the 2013th positional index. 
# 
# To avoid this ambuigity, let's convert the column names into strings: '1980' to '2013'.

# In[ ]:


df_can.columns = list(map(str, df_can.columns))
# [print (type(x)) for x in df_can.columns.values] #<-- uncomment to check type of column headers


# Since we converted the years to string, let's declare a variable that will allow us to easily call upon the full range of years:

# In[ ]:


# useful for plotting later on
years = list(map(str, range(1980, 2014)))
years


# ### Filtering based on a criteria
# To filter the dataframe based on a condition, we simply pass the condition as a boolean vector. 
# 
# For example, Let's filter the dataframe to show the data on Asian countries (AreaName = Asia).

# In[ ]:


# 1. create the condition boolean series
condition = df_can['Continent'] == 'Asia'
print(condition)


# In[ ]:


# 2. pass this condition into the dataFrame
df_can[condition]


# In[ ]:


# we can pass mutliple criteria in the same line. 
# let's filter for AreaNAme = Asia and RegName = Southern Asia

df_can[(df_can['Continent']=='Asia') & (df_can['Region']=='Southern Asia')]

# note: When using 'and' and 'or' operators, pandas requires we use '&' and '|' instead of 'and' and 'or'
# don't forget to enclose the two conditions in parentheses


# Before we proceed: let's review the changes we have made to our dataframe.

# In[ ]:


print('data dimensions:', df_can.shape)
print(df_can.columns)
df_can.head(2)


# ---
# # Visualizing Data using Matplotlib<a id="8"></a>

# ## Matplotlib: Standard Python Visualization Library<a id="10"></a>
# 
# The primary plotting library we will explore in the course is [Matplotlib](http://matplotlib.org/).  As mentioned on their website: 
# >Matplotlib is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms. Matplotlib can be used in Python scripts, the Python and IPython shell, the jupyter notebook, web application servers, and four graphical user interface toolkits.
# 
# If you are aspiring to create impactful visualization with python, Matplotlib is an essential tool to have at your disposal.

# ### Matplotlib.Pyplot
# 
# One of the core aspects of Matplotlib is `matplotlib.pyplot`. It is Matplotlib's scripting layer which we studied in details in the videos about Matplotlib. Recall that it is a collection of command style functions that make Matplotlib work like MATLAB. Each `pyplot` function makes some change to a figure: e.g., creates a figure, creates a plotting area in a figure, plots some lines in a plotting area, decorates the plot with labels, etc. In this lab, we will work with the scripting layer to learn how to generate line plots. In future labs, we will get to work with the Artist layer as well to experiment first hand how it differs from the scripting layer. 
# 

# Let's start by importing `Matplotlib` and `Matplotlib.pyplot` as follows:

# In[ ]:


# we are using the inline backend
get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib as mpl
import matplotlib.pyplot as plt


# *optional: check if Matplotlib is loaded.

# In[ ]:


print ('Matplotlib version: ', mpl.__version__) # >= 2.0.0


# *optional: apply a style to Matplotlib.

# In[ ]:


print(plt.style.available)
mpl.style.use(['ggplot']) # optional: for ggplot-like style


# ### Plotting in *pandas*
# 
# Fortunately, pandas has a built-in implementation of Matplotlib that we can use. Plotting in *pandas* is as simple as appending a `.plot()` method to a series or dataframe.
# 
# Documentation:
# - [Plotting with Series](http://pandas.pydata.org/pandas-docs/stable/api.html#plotting)<br>
# - [Plotting with Dataframes](http://pandas.pydata.org/pandas-docs/stable/api.html#api-dataframe-plotting)

# # Line Pots (Series/Dataframe) <a id="12"></a>

# **What is a line plot and why use it?**
# 
# A line chart or line plot is a type of plot which displays information as a series of data points called 'markers' connected by straight line segments. It is a basic type of chart common in many fields.
# Use line plot when you have a continuous data set. These are best suited for trend-based visualizations of data over a period of time.

# **Let's start with a case study:**
# 
# In 2010, Haiti suffered a catastrophic magnitude 7.0 earthquake. The quake caused widespread devastation and loss of life and aout three million people were affected by this natural disaster. As part of Canada's humanitarian effort, the Government of Canada stepped up its effort in accepting refugees from Haiti. We can quickly visualize this effort using a `Line` plot:
# 
# **Question:** Plot a line graph of immigration from Haiti using `df.plot()`.
# 

# First, we will extract the data series for Haiti.

# In[ ]:


haiti = df_can.loc['Haiti', years] # passing in years 1980 - 2013 to exclude the 'total' column
haiti.head()


# Next, we will plot a line plot by appending `.plot()` to the `haiti` dataframe.

# In[ ]:


haiti.plot()


# *pandas* automatically populated the x-axis with the index values (years), and the y-axis with the column values (population). However, notice how the years were not displayed because they are of type *string*. Therefore, let's change the type of the index values to *integer* for plotting.
# 
# Also, let's label the x and y axis using `plt.title()`, `plt.ylabel()`, and `plt.xlabel()` as follows:

# In[ ]:


haiti.index = haiti.index.map(int) # let's change the index values of Haiti to type integer for plotting
haiti.plot(kind='line')

plt.title('Immigration from Haiti')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')

plt.show() # need this line to show the updates made to the figure


# We can clearly notice how number of immigrants from Haiti spiked up from 2010 as Canada stepped up its efforts to accept refugees from Haiti. Let's annotate this spike in the plot by using the `plt.text()` method.

# In[ ]:


haiti.plot(kind='line')

plt.title('Immigration from Haiti')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')

# annotate the 2010 Earthquake. 
# syntax: plt.text(x, y, label)
plt.text(2000, 6000, '2010 Earthquake') # see note below

plt.show() 


# With just a few lines of code, you were able to quickly identify and visualize the spike in immigration!
# 
# Quick note on x and y values in `plt.text(x, y, label)`:
#     
#      Since the x-axis (years) is type 'integer', we specified x as a year. The y axis (number of immigrants) is type 'integer', so we can just specify the value y = 6000.
#     
# ```python
#     plt.text(2000, 6000, '2010 Earthquake') # years stored as type int
# ```
#     If the years were stored as type 'string', we would need to specify x as the index position of the year. Eg 20th index is year 2000 since it is the 20th year with a base year of 1980.
# ```python
#     plt.text(20, 6000, '2010 Earthquake') # years stored as type int
# ```
#     We will cover advanced annotation methods in later modules.

# We can easily add more countries to line plot to make meaningful comparisons immigration from different countries. 
# 
# **Question:** Let's compare the number of immigrants from India and China from 1980 to 2013.
# 

# Step 1: Get the data set for China and India, and display dataframe.

# In[ ]:


df_CI = df_can.loc[['India', 'China'], years]
df_CI.head()


# Step 2: Plot graph. We will explicitly specify line plot by passing in `kind` parameter to `plot()`.

# In[ ]:


df_CI.plot(kind='line')


# That doesn't look right...
# 
# Recall that *pandas* plots the indices on the x-axis and the columns as individual lines on the y-axis. Since `df_CI` is a dataframe with the `country` as the index and `years` as the columns, we must first transpose the dataframe using `transpose()` method to swap the row and columns.

# In[ ]:


df_CI = df_CI.transpose()
df_CI.head()


# *pandas* will auomatically graph the two countries on the same graph. Go ahead and plot the new transposed dataframe. Make sure to add a title to the plot and label the axes.

# In[ ]:


df_CI.index = df_CI.index.map(int) # change the index values of df_CI to type integer for plotting
df_CI.plot(kind='line')

plt.title('Immigrants from China and India')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')

plt.show()


# From the above plot, we can observe that the China and India have very similar immigration trends through the years. 

# *Note*: How come we didn't need to transpose Haiti's dataframe before plotting (like we did for df_CI)?
# 
# That's because `haiti` is a series as opposed to a dataframe, and has the years as its indices as shown below. 
# ```python
# print(type(haiti))
# print(haiti.head(5))
# ```
# >class 'pandas.core.series.Series' <br>
# >1980    1666 <br>
# >1981    3692 <br>
# >1982    3498 <br>
# >1983    2860 <br>
# >1984    1418 <br>
# >Name: Haiti, dtype: int64 <br>

# Line plot is a handy tool to display several dependent variables against one independent variable. However, it is recommended that no more than 5-10 lines on a single graph; any more than that and it becomes difficult to interpret.

# **Question:** Compare the trend of top 5 countries that contributed the most to immigration to Canada.

# In[ ]:


### type your answer here
df_can.sort_values(by='Total', ascending=False, axis=0, inplace=True)

# the top 5 entries
df_top5 = df_can.head(5)

# transpose the dataframe
df_top5 = df_top5[years].transpose() 

print(df_top5)

# Plot the dataframe. To make the plot more readeable, change the size using the `figsize` parameter.
df_top5.index = df_top5.index.map(int) # change the index values of df_top5 to type integer for plotting
df_top5.plot(kind='line', figsize=(14, 8)) # pass a tuple (x, y) size

plt.title('Immigration Trend of Top 5 Countries')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')

plt.show()


# ### Other Plots
# 
# Congratulations! you have learned how to wrangle data with python and create a line plot with Matplotlib. There are many other plotting styles available other than the default Line plot, all of which can be accessed by passing `kind` keyword to `plot()`. The full list of available plots are as follows:
# 
# * `bar` for vertical bar plots
# * `barh` for horizontal bar plots
# * `hist` for histogram
# * `box` for boxplot
# * `kde` or `density` for density plots
# * `area` for area plots
# * `pie` for pie plots
# * `scatter` for scatter plots
# * `hexbin` for hexbin plot

# ### Thank you for completing this lab!
# 
# This notebook was originally created by [Jay Rajasekharan](https://www.linkedin.com/in/jayrajasekharan) with contributions from [Ehsan M. Kermani](https://www.linkedin.com/in/ehsanmkermani), and [Slobodan Markovic](https://www.linkedin.com/in/slobodan-markovic).
# 
# This notebook was recently revised by [Alex Aklson](https://www.linkedin.com/in/aklson/). I hope you found this lab session interesting. Feel free to contact me if you have any questions!

# This notebook is part of a course on **Coursera** called *Data Visualization with Python*. If you accessed this notebook outside the course, you can take this course online by clicking [here](http://cocl.us/DV0101EN_Coursera_Week1_LAB1).

# <hr>
# 
# Copyright &copy; 2019 [Cognitive Class](https://cognitiveclass.ai/?utm_source=bducopyrightlink&utm_medium=dswb&utm_campaign=bdu). This notebook and its source code are released under the terms of the [MIT License](https://bigdatauniversity.com/mit-license/).
