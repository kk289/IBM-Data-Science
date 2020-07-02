#!/usr/bin/env python
# coding: utf-8

# <div class="alert alert-block alert-info" style="margin-top: 20px">
#     <a href="https://cocl.us/corsera_da0101en_notebook_top">
#          <img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/Images/TopAd.png" width="750" align="center">
#     </a>
# </div>
# 

# <a href="https://www.bigdatauniversity.com"><img src = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/Images/CCLog.png" width = 300, align = "center"></a>
# 
# <h1 align=center><font size = 5>Data Analysis with Python</font></h1>

# Exploratory Data Analysis

# <h3>Welcome!</h3>
# In this section, we will explore several methods to see if certain characteristics or features can be used to predict car price. 

# <h2>Table of content</h2>
# 
# <div class="alert alert-block alert-info" style="margin-top: 20px">
# <ol>
#     <li><a href="#import_data">Import Data from Module</a></li>
#     <li><a href="#pattern_visualization">Analyzing Individual Feature Patterns using Visualization</a></li>
#     <li><a href="#discriptive_statistics">Descriptive Statistical Analysis</a></li>
#     <li><a href="#basic_grouping">Basics of Grouping</a></li>
#     <li><a href="#correlation_causation">Correlation and Causation</a></li>
#     <li><a href="#anova">ANOVA</a></li>
# </ol>
#     
# Estimated Time Needed: <strong>30 min</strong>
# </div>
#  
# <hr>

# <h3>What are the main characteristics which have the most impact on the car price?</h3>

# <h2 id="import_data">1. Import Data from Module 2</h2>

# <h4>Setup</h4>

#  Import libraries 

# In[1]:


import pandas as pd
import numpy as np


#  load data and store in dataframe df:

# This dataset was hosted on IBM Cloud object click <a href="https://cocl.us/DA101EN_object_storage">HERE</a> for free storage

# In[2]:


path='https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/automobileEDA.csv'
df = pd.read_csv(path)
df.head()


# <h2 id="pattern_visualization">2. Analyzing Individual Feature Patterns using Visualization</h2>

# To install seaborn we use the pip which is the python package manager.

# In[3]:


get_ipython().run_cell_magic('capture', '', '! pip install seaborn')


#  Import visualization packages "Matplotlib" and "Seaborn", don't forget about "%matplotlib inline" to plot in a Jupyter notebook.

# In[4]:


import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# <h4>How to choose the right visualization method?</h4>
# <p>When visualizing individual variables, it is important to first understand what type of variable you are dealing with. This will help us find the right visualization method for that variable.</p>
# 

# In[5]:


# list the data types for each column
print(df.dtypes)


# <div class="alert alert-danger alertdanger" style="margin-top: 20px">
# <h3>Question  #1:</h3>
# 
# <b>What is the data type of the column "peak-rpm"? </b>
# </div>

# In[8]:


df.dtypes['peak-rpm']


# for example, we can calculate the correlation between variables  of type "int64" or "float64" using the method "corr":

# In[9]:


df.corr()


# The diagonal elements are always one; we will study correlation more precisely Pearson correlation in-depth at the end of the notebook.

# <div class="alert alert-danger alertdanger" style="margin-top: 20px">
# <h1> Question  #2: </h1>
# 
# <p>Find the correlation between the following columns: bore, stroke,compression-ratio , and horsepower.</p>
# <p>Hint: if you would like to select those columns  use the following syntax: df[['bore','stroke' ,'compression-ratio','horsepower']]</p>
# </div>

# In[11]:


# Write your code below and press Shift+Enter to execute 
df1 = df[['bore', 'compression-ratio', 'horsepower']]
df1.corr()


# <h2>Continuous numerical variables:</h2> 
# 
# <p>Continuous numerical variables are variables that may contain any value within some range. Continuous numerical variables can have the type "int64" or "float64". A great way to visualize these variables is by using scatterplots with fitted lines.</p>
# 
# <p>In order to start understanding the (linear) relationship between an individual variable and the price. We can do this by using "regplot", which plots the scatterplot plus the fitted regression line for the data.</p>

#  Let's see several examples of different linear relationships:

# <h4>Positive linear relationship</h4>

# Let's find the scatterplot of "engine-size" and "price" 

# In[12]:


# Engine size as potential predictor variable of price
sns.regplot(x="engine-size", y="price", data=df)
plt.ylim(0,)


# <p>As the engine-size goes up, the price goes up: this indicates a positive direct correlation between these two variables. Engine size seems like a pretty good predictor of price since the regression line is almost a perfect diagonal line.</p>

#  We can examine the correlation between 'engine-size' and 'price' and see it's approximately  0.87

# In[13]:


df[["engine-size", "price"]].corr()


# Highway mpg is a potential predictor variable of price 

# In[14]:


sns.regplot(x="highway-mpg", y="price", data=df)


# <p>As the highway-mpg goes up, the price goes down: this indicates an inverse/negative relationship between these two variables. Highway mpg could potentially be a predictor of price.</p>

# We can examine the correlation between 'highway-mpg' and 'price' and see it's approximately  -0.704

# In[15]:


df[['highway-mpg', 'price']].corr()


# <h3>Weak Linear Relationship</h3>

# Let's see if "Peak-rpm" as a predictor variable of "price".

# In[16]:


sns.regplot(x="peak-rpm", y="price", data=df)


# <p>Peak rpm does not seem like a good predictor of the price at all since the regression line is close to horizontal. Also, the data points are very scattered and far from the fitted line, showing lots of variability. Therefore it's it is not a reliable variable.</p>

# We can examine the correlation between 'peak-rpm' and 'price' and see it's approximately -0.101616 

# In[17]:


df[['peak-rpm','price']].corr()


#  <div class="alert alert-danger alertdanger" style="margin-top: 20px">
# <h1> Question  3 a): </h1>
# 
# <p>Find the correlation  between x="stroke", y="price".</p>
# <p>Hint: if you would like to select those columns  use the following syntax: df[["stroke","price"]]  </p>
# </div>

# In[18]:


# Write your code below and press Shift+Enter to execute
df[['stroke', 'price']].corr()

# 0.08231


# <div class="alert alert-danger alertdanger" style="margin-top: 20px">
# <h1>Question  3 b):</h1>
# 
# <p>Given the correlation results between "price" and "stroke" do you expect a linear relationship?</p> 
# <p>Verify your results using the function "regplot()".</p>
# </div>

# In[22]:


# Write your code below and press Shift+Enter to execute 
sns.regplot(x = 'stroke', y = 'price', data = df)


# <h3>Categorical variables</h3>
# 
# <p>These are variables that describe a 'characteristic' of a data unit, and are selected from a small group of categories. The categorical variables can have the type "object" or "int64". A good way to visualize categorical variables is by using boxplots.</p>

# Let's look at the relationship between "body-style" and "price".

# In[23]:


sns.boxplot(x="body-style", y="price", data=df)


# <p>We see that the distributions of price between the different body-style categories have a significant overlap, and so body-style would not be a good predictor of price. Let's examine engine "engine-location" and "price":</p>

# In[24]:


sns.boxplot(x="engine-location", y="price", data=df)


# <p>Here we see that the distribution of price between these two engine-location categories, front and rear, are distinct enough to take engine-location as a potential good predictor of price.</p>

#  Let's examine "drive-wheels" and "price".

# In[25]:


# drive-wheels
sns.boxplot(x="drive-wheels", y="price", data=df)


# <p>Here we see that the distribution of price between the different drive-wheels categories differs; as such drive-wheels could potentially be a predictor of price.</p>

# <h2 id="discriptive_statistics">3. Descriptive Statistical Analysis</h2>

# <p>Let's first take a look at the variables by utilizing a description method.</p>
# 
# <p>The <b>describe</b> function automatically computes basic statistics for all continuous variables. Any NaN values are automatically skipped in these statistics.</p>
# 
# This will show:
# <ul>
#     <li>the count of that variable</li>
#     <li>the mean</li>
#     <li>the standard deviation (std)</li> 
#     <li>the minimum value</li>
#     <li>the IQR (Interquartile Range: 25%, 50% and 75%)</li>
#     <li>the maximum value</li>
# <ul>
# 

#  We can apply the method "describe" as follows:

# In[26]:


df.describe()


#  The default setting of "describe" skips variables of type object. We can apply the method "describe" on the variables of type 'object' as follows:

# In[27]:


df.describe(include=['object'])


# <h3>Value Counts</h3>

# <p>Value-counts is a good way of understanding how many units of each characteristic/variable we have. We can apply the "value_counts" method on the column 'drive-wheels'. Don’t forget the method "value_counts" only works on Pandas series, not Pandas Dataframes. As a result, we only include one bracket "df['drive-wheels']" not two brackets "df[['drive-wheels']]".</p>

# In[28]:


df['drive-wheels'].value_counts()


# We can convert the series to a Dataframe as follows :

# In[29]:


df['drive-wheels'].value_counts().to_frame()


# Let's repeat the above steps but save the results to the dataframe "drive_wheels_counts" and rename the column  'drive-wheels' to 'value_counts'.

# In[30]:


drive_wheels_counts = df['drive-wheels'].value_counts().to_frame()
drive_wheels_counts.rename(columns={'drive-wheels': 'value_counts'}, inplace=True)
drive_wheels_counts


#  Now let's rename the index to 'drive-wheels':

# In[31]:


drive_wheels_counts.index.name = 'drive-wheels'
drive_wheels_counts


# We can repeat the above process for the variable 'engine-location'.

# In[32]:


# engine-location as variable
engine_loc_counts = df['engine-location'].value_counts().to_frame()
engine_loc_counts.rename(columns={'engine-location': 'value_counts'}, inplace=True)
engine_loc_counts.index.name = 'engine-location'
engine_loc_counts.head(10)


# <p>Examining the value counts of the engine location would not be a good predictor variable for the price. This is because we only have three cars with a rear engine and 198 with an engine in the front, this result is skewed. Thus, we are not able to draw any conclusions about the engine location.</p>

# <h2 id="basic_grouping">4. Basics of Grouping</h2>

# <p>The "groupby" method groups data by different categories. The data is grouped based on one or several variables and analysis is performed on the individual groups.</p>
# 
# <p>For example, let's group by the variable "drive-wheels". We see that there are 3 different categories of drive wheels.</p>

# In[33]:


df['drive-wheels'].unique()


# <p>If we want to know, on average, which type of drive wheel is most valuable, we can group "drive-wheels" and then average them.</p>
# 
# <p>We can select the columns 'drive-wheels', 'body-style' and 'price', then assign it to the variable "df_group_one".</p>

# In[34]:


df_group_one = df[['drive-wheels','body-style','price']]


# We can then calculate the average price for each of the different categories of data.

# In[35]:


# grouping results
df_group_one = df_group_one.groupby(['drive-wheels'],as_index=False).mean()
df_group_one


# <p>From our data, it seems rear-wheel drive vehicles are, on average, the most expensive, while 4-wheel and front-wheel are approximately the same in price.</p>
# 
# <p>You can also group with multiple variables. For example, let's group by both 'drive-wheels' and 'body-style'. This groups the dataframe by the unique combinations 'drive-wheels' and 'body-style'. We can store the results in the variable 'grouped_test1'.</p>

# In[36]:


# grouping results
df_gptest = df[['drive-wheels','body-style','price']]
grouped_test1 = df_gptest.groupby(['drive-wheels','body-style'],as_index=False).mean()
grouped_test1


# <p>This grouped data is much easier to visualize when it is made into a pivot table. A pivot table is like an Excel spreadsheet, with one variable along the column and another along the row. We can convert the dataframe to a pivot table using the method "pivot " to create a pivot table from the groups.</p>
# 
# <p>In this case, we will leave the drive-wheel variable as the rows of the table, and pivot body-style to become the columns of the table:</p>

# In[37]:


grouped_pivot = grouped_test1.pivot(index='drive-wheels',columns='body-style')
grouped_pivot


# <p>Often, we won't have data for some of the pivot cells. We can fill these missing cells with the value 0, but any other value could potentially be used as well. It should be mentioned that missing data is quite a complex subject and is an entire course on its own.</p>

# In[38]:


grouped_pivot = grouped_pivot.fillna(0) #fill missing values with 0
grouped_pivot


# <div class="alert alert-danger alertdanger" style="margin-top: 20px">
# <h1>Question 4:</h1>
# 
# <p>Use the "groupby" function to find the average "price" of each car based on "body-style" ? </p>
# </div>

# In[39]:


# Write your code below and press Shift+Enter to execute 
df_gptest_2 = df[['body-style','price']]
grouped_test_2 = df_gptest_2.groupby(['body-style'],as_index=False).mean()
grouped_test_2


# If you did not import "pyplot" let's do it again. 

# In[40]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# <h4>Variables: Drive Wheels and Body Style vs Price</h4>

# Let's use a heat map to visualize the relationship between Body Style vs Price.

# In[41]:


#use the grouped results
plt.pcolor(grouped_pivot, cmap='RdBu')
plt.colorbar()
plt.show()


# <p>The heatmap plots the target variable (price) proportional to colour with respect to the variables 'drive-wheel' and 'body-style' in the vertical and horizontal axis respectively. This allows us to visualize how the price is related to 'drive-wheel' and 'body-style'.</p>
# 
# <p>The default labels convey no useful information to us. Let's change that:</p>

# In[42]:


fig, ax = plt.subplots()
im = ax.pcolor(grouped_pivot, cmap='RdBu')

#label names
row_labels = grouped_pivot.columns.levels[1]
col_labels = grouped_pivot.index

#move ticks and labels to the center
ax.set_xticks(np.arange(grouped_pivot.shape[1]) + 0.5, minor=False)
ax.set_yticks(np.arange(grouped_pivot.shape[0]) + 0.5, minor=False)

#insert labels
ax.set_xticklabels(row_labels, minor=False)
ax.set_yticklabels(col_labels, minor=False)

#rotate label if too long
plt.xticks(rotation=90)

fig.colorbar(im)
plt.show()


# <p>Visualization is very important in data science, and Python visualization packages provide great freedom. We will go more in-depth in a separate Python Visualizations course.</p>
# 
# <p>The main question we want to answer in this module, is "What are the main characteristics which have the most impact on the car price?".</p>
# 
# <p>To get a better measure of the important characteristics, we look at the correlation of these variables with the car price, in other words: how is the car price dependent on this variable?</p>

# <h2 id="correlation_causation">5. Correlation and Causation</h2>

# <p><b>Correlation</b>: a measure of the extent of interdependence between variables.</p>
# 
# <p><b>Causation</b>: the relationship between cause and effect between two variables.</p>
# 
# <p>It is important to know the difference between these two and that correlation does not imply causation. Determining correlation is much simpler  the determining causation as causation may require independent experimentation.</p>

# <p3>Pearson Correlation</p>
# <p>The Pearson Correlation measures the linear dependence between two variables X and Y.</p>
# <p>The resulting coefficient is a value between -1 and 1 inclusive, where:</p>
# <ul>
#     <li><b>1</b>: Total positive linear correlation.</li>
#     <li><b>0</b>: No linear correlation, the two variables most likely do not affect each other.</li>
#     <li><b>-1</b>: Total negative linear correlation.</li>
# </ul>

# <p>Pearson Correlation is the default method of the function "corr".  Like before we can calculate the Pearson Correlation of the of the 'int64' or 'float64'  variables.</p>

# In[43]:


df.corr()


#  sometimes we would like to know the significant of the correlation estimate. 

# <b>P-value</b>: 
# <p>What is this P-value? The P-value is the probability value that the correlation between these two variables is statistically significant. Normally, we choose a significance level of 0.05, which means that we are 95% confident that the correlation between the variables is significant.</p>
# 
# By convention, when the
# <ul>
#     <li>p-value is $<$ 0.001: we say there is strong evidence that the correlation is significant.</li>
#     <li>the p-value is $<$ 0.05: there is moderate evidence that the correlation is significant.</li>
#     <li>the p-value is $<$ 0.1: there is weak evidence that the correlation is significant.</li>
#     <li>the p-value is $>$ 0.1: there is no evidence that the correlation is significant.</li>
# </ul>

#  We can obtain this information using  "stats" module in the "scipy"  library.

# In[44]:


from scipy import stats


# <h3>Wheel-base vs Price</h3>

# Let's calculate the  Pearson Correlation Coefficient and P-value of 'wheel-base' and 'price'. 

# In[45]:


pearson_coef, p_value = stats.pearsonr(df['wheel-base'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value)  


# <h5>Conclusion:</h5>
# <p>Since the p-value is $<$ 0.001, the correlation between wheel-base and price is statistically significant, although the linear relationship isn't extremely strong (~0.585)</p>

# <h3>Horsepower vs Price</h3>

#  Let's calculate the  Pearson Correlation Coefficient and P-value of 'horsepower' and 'price'.

# In[46]:


pearson_coef, p_value = stats.pearsonr(df['horsepower'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value)  


# <h5>Conclusion:</h5>
# 
# <p>Since the p-value is $<$ 0.001, the correlation between horsepower and price is statistically significant, and the linear relationship is quite strong (~0.809, close to 1)</p>

# <h3>Length vs Price</h3>
# 
# Let's calculate the  Pearson Correlation Coefficient and P-value of 'length' and 'price'.

# In[47]:


pearson_coef, p_value = stats.pearsonr(df['length'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value)  


# <h5>Conclusion:</h5>
# <p>Since the p-value is $<$ 0.001, the correlation between length and price is statistically significant, and the linear relationship is moderately strong (~0.691).</p>

# <h3>Width vs Price</h3>

#  Let's calculate the Pearson Correlation Coefficient and P-value of 'width' and 'price':

# In[48]:


pearson_coef, p_value = stats.pearsonr(df['width'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value ) 


# ##### Conclusion:
# 
# Since the p-value is < 0.001, the correlation between width and price is statistically significant, and the linear relationship is quite strong (~0.751).

# ### Curb-weight vs Price

#  Let's calculate the Pearson Correlation Coefficient and P-value of 'curb-weight' and 'price':

# In[49]:


pearson_coef, p_value = stats.pearsonr(df['curb-weight'], df['price'])
print( "The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value)  


# <h5>Conclusion:</h5>
# <p>Since the p-value is $<$ 0.001, the correlation between curb-weight and price is statistically significant, and the linear relationship is quite strong (~0.834).</p>

# <h3>Engine-size vs Price</h3>
# 
# Let's calculate the Pearson Correlation Coefficient and P-value of 'engine-size' and 'price':

# In[50]:


pearson_coef, p_value = stats.pearsonr(df['engine-size'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value) 


# <h5>Conclusion:</h5>
# 
# <p>Since the p-value is $<$ 0.001, the correlation between engine-size and price is statistically significant, and the linear relationship is very strong (~0.872).</p>

# <h3>Bore vs Price</h3>

#  Let's calculate the  Pearson Correlation Coefficient and P-value of 'bore' and 'price':

# In[51]:


pearson_coef, p_value = stats.pearsonr(df['bore'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =  ", p_value ) 


# <h5>Conclusion:</h5>
# <p>Since the p-value is $<$ 0.001, the correlation between bore and price is statistically significant, but the linear relationship is only moderate (~0.521).</p>

#  We can relate the process for each 'City-mpg'  and 'Highway-mpg':

# <h3>City-mpg vs Price</h3>

# In[52]:


pearson_coef, p_value = stats.pearsonr(df['city-mpg'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value)  


# <h5>Conclusion:</h5>
# <p>Since the p-value is $<$ 0.001, the correlation between city-mpg and price is statistically significant, and the coefficient of ~ -0.687 shows that the relationship is negative and moderately strong.</p>

# <h3>Highway-mpg vs Price</h3>

# In[53]:


pearson_coef, p_value = stats.pearsonr(df['highway-mpg'], df['price'])
print( "The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value ) 


# ##### Conclusion:
# Since the p-value is < 0.001, the correlation between highway-mpg and price is statistically significant, and the coefficient of ~ -0.705 shows that the relationship is negative and moderately strong.

# <h2 id="anova">6. ANOVA</h2>

# <h3>ANOVA: Analysis of Variance</h3>
# <p>The Analysis of Variance  (ANOVA) is a statistical method used to test whether there are significant differences between the means of two or more groups. ANOVA returns two parameters:</p>
# 
# <p><b>F-test score</b>: ANOVA assumes the means of all groups are the same, calculates how much the actual means deviate from the assumption, and reports it as the F-test score. A larger score means there is a larger difference between the means.</p>
# 
# <p><b>P-value</b>:  P-value tells how statistically significant is our calculated score value.</p>
# 
# <p>If our price variable is strongly correlated with the variable we are analyzing, expect ANOVA to return a sizeable F-test score and a small p-value.</p>

# <h3>Drive Wheels</h3>

# <p>Since ANOVA analyzes the difference between different groups of the same variable, the groupby function will come in handy. Because the ANOVA algorithm averages the data automatically, we do not need to take the average before hand.</p>
# 
# <p>Let's see if different types 'drive-wheels' impact  'price', we group the data.</p>

#  Let's see if different types 'drive-wheels' impact  'price', we group the data.

# In[54]:


grouped_test2=df_gptest[['drive-wheels', 'price']].groupby(['drive-wheels'])
grouped_test2.head(2)


# In[55]:


df_gptest


#  We can obtain the values of the method group using the method "get_group".  

# In[56]:


grouped_test2.get_group('4wd')['price']


# we can use the function 'f_oneway' in the module 'stats'  to obtain the <b>F-test score</b> and <b>P-value</b>.

# In[57]:


# ANOVA
f_val, p_val = stats.f_oneway(grouped_test2.get_group('fwd')['price'], grouped_test2.get_group('rwd')['price'], grouped_test2.get_group('4wd')['price'])  
 
print( "ANOVA results: F=", f_val, ", P =", p_val)   


# This is a great result, with a large F test score showing a strong correlation and a P value of almost 0 implying almost certain statistical significance. But does this mean all three tested groups are all this highly correlated? 

# #### Separately: fwd and rwd

# In[58]:


f_val, p_val = stats.f_oneway(grouped_test2.get_group('fwd')['price'], grouped_test2.get_group('rwd')['price'])  
 
print( "ANOVA results: F=", f_val, ", P =", p_val )


#  Let's examine the other groups 

# #### 4wd and rwd

# In[59]:


f_val, p_val = stats.f_oneway(grouped_test2.get_group('4wd')['price'], grouped_test2.get_group('rwd')['price'])  
   
print( "ANOVA results: F=", f_val, ", P =", p_val)   


# <h4>4wd and fwd</h4>

# In[60]:


f_val, p_val = stats.f_oneway(grouped_test2.get_group('4wd')['price'], grouped_test2.get_group('fwd')['price'])  
 
print("ANOVA results: F=", f_val, ", P =", p_val)   


# <h3>Conclusion: Important Variables</h3>

# <p>We now have a better idea of what our data looks like and which variables are important to take into account when predicting the car price. We have narrowed it down to the following variables:</p>
# 
# Continuous numerical variables:
# <ul>
#     <li>Length</li>
#     <li>Width</li>
#     <li>Curb-weight</li>
#     <li>Engine-size</li>
#     <li>Horsepower</li>
#     <li>City-mpg</li>
#     <li>Highway-mpg</li>
#     <li>Wheel-base</li>
#     <li>Bore</li>
# </ul>
#     
# Categorical variables:
# <ul>
#     <li>Drive-wheels</li>
# </ul>
# 
# <p>As we now move into building machine learning models to automate our analysis, feeding the model with variables that meaningfully affect our target variable will improve our model's prediction performance.</p>

# <h1>Thank you for completing this notebook</h1>

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
