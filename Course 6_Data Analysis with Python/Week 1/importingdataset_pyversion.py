#!/usr/bin/env python
# coding: utf-8

# <div class="alert alert-block alert-info" style="margin-top: 20px">
#     <a href="https://cocl.us/corsera_da0101en_notebook_top">
#          <img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/Images/TopAd.png" width="750" align="center">
#     </a>
# </div>
# 

# <a href="https://www.bigdatauniversity.com"><img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/Images/CCLog.png" width=300, align="center"></a>
# 
# <h1 align=center><font size = 5>Data Analysis with Python</font></h1>

# <h1>Introduction</h1>
# <h3>Welcome!</h3>
# 
# <p>
# In this section, you will learn how to approach data acquisition in various ways, and obtain necessary insights from a dataset. By the end of this lab, you will successfully load the data into Jupyter Notebook, and gain some fundamental insights via Pandas Library.
# </p>

# <h2>Table of Contents</h2>
# 
# <div class="alert alert-block alert-info" style="margin-top: 20px">
# <ol>
#     <li><a href="#data_acquisition">Data Acquisition</a>
#     <li><a href="#basic_insight">Basic Insight of Dataset</a></li>
# </ol>
# 
# Estimated Time Needed: <strong>10 min</strong>
# </div>
# <hr>

# <h1 id="data_acquisition">Data Acquisition</h1>
# <p>
# There are various formats for a dataset, .csv, .json, .xlsx  etc. The dataset can be stored in different places, on your local machine or sometimes online.<br>
# In this section, you will learn how to load a dataset into our Jupyter Notebook.<br>
# In our case, the Automobile Dataset is an online source, and it is in CSV (comma separated value) format. Let's use this dataset as an example to practice data reading.
# <ul>
#     <li>data source: <a href="https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data" target="_blank">https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data</a></li>
#     <li>data type: csv</li>
# </ul>
# The Pandas Library is a useful tool that enables us to read various datasets into a data frame; our Jupyter notebook platforms have a built-in <b>Pandas Library</b> so that all we need to do is import Pandas without installing.
# </p>

# In[1]:


# import pandas library
import pandas as pd


# <h2>Read Data</h2>
# <p>
# We use <code>pandas.read_csv()</code> function to read the csv file. In the bracket, we put the file path along with a quotation mark, so that pandas will read the file into a data frame from that address. The file path can be either an URL or your local file address.<br>
# Because the data does not include headers, we can add an argument <code>headers = None</code>  inside the  <code>read_csv()</code> method, so that pandas will not automatically set the first row as a header.<br>
# You can also assign the dataset to any variable you create.
# </p>

# This dataset was hosted on IBM Cloud object click <a href="https://cocl.us/DA101EN_object_storage">HERE</a> for free storage.

# In[2]:


# Import pandas library
import pandas as pd

# Read the online file by the URL provides above, and assign it to variable "df"
other_path = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv"
df = pd.read_csv(other_path, header=None)


# After reading the dataset, we can use the <code>dataframe.head(n)</code> method to check the top n rows of the dataframe; where n is an integer. Contrary to <code>dataframe.head(n)</code>, <code>dataframe.tail(n)</code> will show you the bottom n rows of the dataframe.
# 

# In[3]:


# show the first 5 rows using dataframe.head() method
print("The first 5 rows of the dataframe") 
df.head(5)


# <div class="alert alert-danger alertdanger" style="margin-top: 20px">
# <h1> Question #1: </h1>
# <b>check the bottom 10 rows of data frame "df".</b>
# </div>

# In[4]:


# Write your code below and press Shift+Enter to execute
df.head(10)


# <h3>Add Headers</h3>
# <p>
# Take a look at our dataset; pandas automatically set the header by an integer from 0.
# </p>
# <p>
# To better describe our data we can introduce a header, this information is available at:  <a href="https://archive.ics.uci.edu/ml/datasets/Automobile" target="_blank">https://archive.ics.uci.edu/ml/datasets/Automobile</a>
# </p>
# <p>
# Thus, we have to add headers manually.
# </p>
# <p>
# Firstly, we create a list "headers" that include all column names in order.
# Then, we use <code>dataframe.columns = headers</code> to replace the headers by the list we created.
# </p>

# In[5]:


# create headers list
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
print("headers\n", headers)


#  We replace headers and recheck our data frame

# In[6]:


df.columns = headers
df.head(10)


# we can drop missing values along the column "price" as follows  

# In[7]:


df.dropna(subset=["price"], axis=0)


# Now, we have successfully read the raw dataset and add the correct headers into the data frame.

#  <div class="alert alert-danger alertdanger" style="margin-top: 20px">
# <h1> Question #2: </h1>
# <b>Find the name of the columns of the dataframe</b>
# </div>

# In[13]:


# Write your code below and press Shift+Enter to execute 
print(df.columns)


# <h2>Save Dataset</h2>
# <p>
# Correspondingly, Pandas enables us to save the dataset to csv  by using the <code>dataframe.to_csv()</code> method, you can add the file path and name along with quotation marks in the brackets.
# </p>
# <p>
#     For example, if you would save the dataframe <b>df</b> as <b>automobile.csv</b> to your local machine, you may use the syntax below:
# </p>
df.to_csv("automobile.csv", index=False)
#  We can also read and save other file formats, we can use similar functions to **`pd.read_csv()`** and **`df.to_csv()`** for other data formats, the functions are listed in the following table:
# 

# <h2>Read/Save Other Data Formats</h2>
# 
# 
# 
# | Data Formate  | Read           | Save             |
# | ------------- |:--------------:| ----------------:|
# | csv           | `pd.read_csv()`  |`df.to_csv()`     |
# | json          | `pd.read_json()` |`df.to_json()`    |
# | excel         | `pd.read_excel()`|`df.to_excel()`   |
# | hdf           | `pd.read_hdf()`  |`df.to_hdf()`     |
# | sql           | `pd.read_sql()`  |`df.to_sql()`     |
# | ...           |   ...          |       ...        |

# <h1 id="basic_insight">Basic Insight of Dataset</h1>
# <p>
# After reading data into Pandas dataframe, it is time for us to explore the dataset.<br>
# There are several ways to obtain essential insights of the data to help us better understand our dataset.
# </p>

# <h2>Data Types</h2>
# <p>
# Data has a variety of types.<br>
# The main types stored in Pandas dataframes are <b>object</b>, <b>float</b>, <b>int</b>, <b>bool</b> and <b>datetime64</b>. In order to better learn about each attribute, it is always good for us to know the data type of each column. In Pandas:
# </p>

# In[14]:


df.dtypes


# returns a Series with the data type of each column.

# In[15]:


# check the data type of data frame "df" by .dtypes
print(df.dtypes)


# <p>
# As a result, as shown above, it is clear to see that the data type of "symboling" and "curb-weight" are <code>int64</code>, "normalized-losses" is <code>object</code>, and "wheel-base" is <code>float64</code>, etc.
# </p>
# <p>
# These data types can be changed; we will learn how to accomplish this in a later module.
# </p>

# <h2>Describe</h2>
# If we would like to get a statistical summary of each column, such as count, column mean value, column standard deviation, etc. We use the describe method:
dataframe.describe()
# This method will provide various summary statistics, excluding <code>NaN</code> (Not a Number) values.

# In[16]:


df.describe()


# <p>
# This shows the statistical summary of all numeric-typed (int, float) columns.<br>
# For example, the attribute "symboling" has 205 counts, the mean value of this column is 0.83, the standard deviation is 1.25, the minimum value is -2, 25th percentile is 0, 50th percentile is 1, 75th percentile is 2, and the maximum value is 3.
# <br>
# However, what if we would also like to check all the columns including those that are of type object.
# <br><br>
# 
# You can add an argument <code>include = "all"</code> inside the bracket. Let's try it again.
# </p>

# In[17]:


# describe all the columns in "df" 
df.describe(include = "all")


# <p>
# Now, it provides the statistical summary of all the columns, including object-typed attributes.<br>
# We can now see how many unique values, which is the top value and the frequency of top value in the object-typed columns.<br>
# Some values in the table above show as "NaN", this is because those numbers are not available regarding a particular column type.<br>
# </p>

# <div class="alert alert-danger alertdanger" style="margin-top: 20px">
# <h1> Question #3: </h1>
# 
# <p>
# You can select the columns of a data frame by indicating the name of  each column, for example, you can select the three columns as follows:
# </p>
# <p>
#     <code>dataframe[[' column 1 ',column 2', 'column 3']]</code>
# </p>
# <p>
# Where "column" is the name of the column, you can apply the method  ".describe()" to get the statistics of those columns as follows:
# </p>
# <p>
#     <code>dataframe[[' column 1 ',column 2', 'column 3'] ].describe()</code>
# </p>
# 
# Apply the  method to ".describe()" to the columns 'length' and 'compression-ratio'.
# </div>

# In[26]:


# Write your code below and press Shift+Enter to execute 
df[['length','compression-ratio']].describe()


# <h2>Info</h2>
# Another method you can use to check your dataset is:
dataframe.info
# It provide a concise summary of your DataFrame.

# In[27]:


# look at the info of "df"
df.info


# <p>
# Here we are able to see the information of our dataframe, with the top 30 rows and the bottom 30 rows.
# <br><br>
# And, it also shows us the whole data frame has 205 rows and 26 columns in total.
# </p>

# <h1>Excellent! You have just completed the  Introduction  Notebook!</h1>

# <div class="alert alert-block alert-info" style="margin-top: 20px">
# 
#     <p><a href="https://cocl.us/corsera_da0101en_notebook_bottom"><img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/Images/BottomAd.png" width="750" align="center"></a></p>
# </div>
# 

# <h3>About the Authors:</h3>
# 
# This notebook was written by <a href="https://www.linkedin.com/in/mahdi-noorian-58219234/" target="_blank">Mahdi Noorian PhD</a>, <a href="https://www.linkedin.com/in/joseph-s-50398b136/" target="_blank">Joseph Santarcangelo</a>, Bahare Talayian, Eric Xiao, Steven Dong, Parizad, Hima Vsudevan and <a href="https://www.linkedin.com/in/fiorellawever/" target="_blank">Fiorella Wenver</a> and <a href=" https://www.linkedin.com/in/yi-leng-yao-84451275/ " target="_blank" >Yi Yao</a>.
# 
# <p><a href="https://www.linkedin.com/in/joseph-s-50398b136/" target="_blank">Joseph Santarcangelo</a> is a Data Scientist at IBM, and holds a PhD in Electrical Engineering. His research focused on using Machine Learning, Signal Processing, and Computer Vision to determine how videos impact human cognition. Joseph has been working for IBM since he completed his PhD.</p>

# <hr>
# <p>Copyright &copy; 2018 IBM Developer Skills Network. This notebook and its source code are released under the terms of the <a href="https://cognitiveclass.ai/mit-license/">MIT License</a>.</p>
