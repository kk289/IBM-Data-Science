#!/usr/bin/env python
# coding: utf-8

# <a href="https://cognitiveclass.ai/">
#     <img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Ad/CCLog.png" width="200" align="center">
# </a>

# <h1>Tuples in Python</h1>

# <p><strong>Welcome!</strong> This notebook will teach you about the tuples in the Python Programming Language. By the end of this lab, you'll know the basics tuple operations in Python, including indexing, slicing and sorting.</p> 

# <div class="alert alert-block alert-info" style="margin-top: 20px">
#     <a href="https://cocl.us/topNotebooksPython101Coursera">
#          <img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Ad/TopAd.png" width="750" align="center">
#     </a>
# </div>

# <h2>Table of Contents</h2>
# <div class="alert alert-block alert-info" style="margin-top: 20px">
#     <ul>
#         <li>
#             <a href="#dataset">About the Dataset</a>
#         </li>
#         <li>
#             <a href="#tuple">Tuples</a>
#             <ul>
#                 <li><a href="index">Indexing</a></li>
#                 <li><a href="slice">Slicing</a></li>
#                 <li><a href="sort">Sorting</a></li>
#             </ul>
#         </li>
#         <li>
#             <a href="#escape">Quiz on Tuples</a>
#         </li>
#     </ul>
#     <p>
#         Estimated time needed: <strong>15 min</strong>
#     </p>
# </div>
# 
# <hr>

# <h2 id="dataset">About the Dataset</h2>

# Imagine you received album recommendations from your friends and compiled all of the recommandations into a table, with specific information about each album.
# 
# The table has one row for each movie and several columns:
# 
# - **artist** - Name of the artist
# - **album** - Name of the album
# - **released_year** - Year the album was released
# - **length_min_sec** - Length of the album (hours,minutes,seconds)
# - **genre** - Genre of the album
# - **music_recording_sales_millions** - Music recording sales (millions in USD) on [SONG://DATABASE](http://www.song-database.com/)
# - **claimed_sales_millions** - Album's claimed sales (millions in USD) on [SONG://DATABASE](http://www.song-database.com/)
# - **date_released** - Date on which the album was released
# - **soundtrack** - Indicates if the album is the movie soundtrack (Y) or (N)
# - **rating_of_friends** - Indicates the rating from your friends from 1 to 10
# <br>
# <br>
# 
# The dataset can be seen below:
# 
# <font size="1">
# <table font-size:xx-small style="width:25%">
#   <tr>
#     <th>Artist</th>
#     <th>Album</th> 
#     <th>Released</th>
#     <th>Length</th>
#     <th>Genre</th> 
#     <th>Music recording sales (millions)</th>
#     <th>Claimed sales (millions)</th>
#     <th>Released</th>
#     <th>Soundtrack</th>
#     <th>Rating (friends)</th>
#   </tr>
#   <tr>
#     <td>Michael Jackson</td>
#     <td>Thriller</td> 
#     <td>1982</td>
#     <td>00:42:19</td>
#     <td>Pop, rock, R&B</td>
#     <td>46</td>
#     <td>65</td>
#     <td>30-Nov-82</td>
#     <td></td>
#     <td>10.0</td>
#   </tr>
#   <tr>
#     <td>AC/DC</td>
#     <td>Back in Black</td> 
#     <td>1980</td>
#     <td>00:42:11</td>
#     <td>Hard rock</td>
#     <td>26.1</td>
#     <td>50</td>
#     <td>25-Jul-80</td>
#     <td></td>
#     <td>8.5</td>
#   </tr>
#     <tr>
#     <td>Pink Floyd</td>
#     <td>The Dark Side of the Moon</td> 
#     <td>1973</td>
#     <td>00:42:49</td>
#     <td>Progressive rock</td>
#     <td>24.2</td>
#     <td>45</td>
#     <td>01-Mar-73</td>
#     <td></td>
#     <td>9.5</td>
#   </tr>
#     <tr>
#     <td>Whitney Houston</td>
#     <td>The Bodyguard</td> 
#     <td>1992</td>
#     <td>00:57:44</td>
#     <td>Soundtrack/R&B, soul, pop</td>
#     <td>26.1</td>
#     <td>50</td>
#     <td>25-Jul-80</td>
#     <td>Y</td>
#     <td>7.0</td>
#   </tr>
#     <tr>
#     <td>Meat Loaf</td>
#     <td>Bat Out of Hell</td> 
#     <td>1977</td>
#     <td>00:46:33</td>
#     <td>Hard rock, progressive rock</td>
#     <td>20.6</td>
#     <td>43</td>
#     <td>21-Oct-77</td>
#     <td></td>
#     <td>7.0</td>
#   </tr>
#     <tr>
#     <td>Eagles</td>
#     <td>Their Greatest Hits (1971-1975)</td> 
#     <td>1976</td>
#     <td>00:43:08</td>
#     <td>Rock, soft rock, folk rock</td>
#     <td>32.2</td>
#     <td>42</td>
#     <td>17-Feb-76</td>
#     <td></td>
#     <td>9.5</td>
#   </tr>
#     <tr>
#     <td>Bee Gees</td>
#     <td>Saturday Night Fever</td> 
#     <td>1977</td>
#     <td>1:15:54</td>
#     <td>Disco</td>
#     <td>20.6</td>
#     <td>40</td>
#     <td>15-Nov-77</td>
#     <td>Y</td>
#     <td>9.0</td>
#   </tr>
#     <tr>
#     <td>Fleetwood Mac</td>
#     <td>Rumours</td> 
#     <td>1977</td>
#     <td>00:40:01</td>
#     <td>Soft rock</td>
#     <td>27.9</td>
#     <td>40</td>
#     <td>04-Feb-77</td>
#     <td></td>
#     <td>9.5</td>
#   </tr>
# </table></font>

# <hr>

# <h2 id="tuple">Tuples</h2>

# In Python, there are different data types: string, integer and float. These data types can all be contained in a tuple as follows:

# <img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%202/Images/TuplesType.png" width="750" align="center" />

# Now, let us create your first tuple with string, integer and float.

# In[2]:


# Create your first tuple

tuple1 = ("disco",10,1.2 )
tuple1


# The type of variable is a **tuple**. 

# In[3]:


# Print the type of the tuple you created

type(tuple1)


# <h3 id="index">Indexing</h3>

#  Each element of a tuple can be accessed via an index. The following table represents the relationship between the index and the items in the tuple. Each element can be obtained by the name of the tuple followed by a square bracket with the index number:

# <img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%202/Images/TuplesIndex.gif" width="750" align="center">

# We can print out each value in the tuple:

# In[4]:


# Print the variable on each index

print(tuple1[0])
print(tuple1[1])
print(tuple1[2])


# We can print out the **type** of each value in the tuple:
# 

# In[5]:


# Print the type of value on each index

print(type(tuple1[0]))
print(type(tuple1[1]))
print(type(tuple1[2]))


# We can also use negative indexing. We use the same table above with corresponding negative values:

# <img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%202/Images/TuplesNeg.png" width="750" align="center">

# We can obtain the last element as follows (this time we will not use the print statement to display the values):

# In[6]:


# Use negative index to get the value of the last element

tuple1[-1]


# We can display the next two elements as follows:

# In[7]:


# Use negative index to get the value of the second last element

tuple1[-2]


# In[8]:


# Use negative index to get the value of the third last element

tuple1[-3]


# <h3 id="concate">Concatenate Tuples</h3>

# We can concatenate or combine tuples by using the **+** sign:

# In[9]:


# Concatenate two tuples

tuple2 = tuple1 + ("hard rock", 10)
tuple2


# We can slice tuples obtaining multiple values as demonstrated by the figure below:

# <img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%202/Images/TuplesSlice.gif" width="750" align="center">

# <h3 id="slice">Slicing</h3>

# We can slice tuples, obtaining new tuples with the corresponding elements: 

# In[10]:


# Slice from index 0 to index 2

tuple2[0:3]


# We can obtain the last two elements of the tuple:

# In[11]:


# Slice from index 3 to index 4

tuple2[3:5]


# We can obtain the length of a tuple using the length command: 

# In[12]:


# Get the length of tuple

len(tuple2)


# This figure shows the number of elements:

# <img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%202/Images/TuplesElement.png" width="750" align="center">

# <h3 id="sort">Sorting</h3>

#  Consider the following tuple:

# In[14]:


# A sample tuple

Ratings = (0, 9, 6, 5, 10, 8, 9, 6, 2)


# We can sort the values in a tuple and save it to a new tuple: 

# In[15]:


# Sort the tuple

RatingsSorted = sorted(Ratings)
RatingsSorted


# <h3 id="nest">Nested Tuple</h3>

# A tuple can contain another tuple as well as other more complex data types. This process is called 'nesting'. Consider the following tuple with several elements: 

# In[16]:


# Create a nest tuple

NestedT =(1, 2, ("pop", "rock") ,(3,4),("disco",(1,2)))


# Each element in the tuple including other tuples can be obtained via an index as shown in the figure:

# <img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%202/Images/TuplesNestOne.png" width="750" align="center">

# In[17]:


# Print element on each index

print("Element 0 of Tuple: ", NestedT[0])
print("Element 1 of Tuple: ", NestedT[1])
print("Element 2 of Tuple: ", NestedT[2])
print("Element 3 of Tuple: ", NestedT[3])
print("Element 4 of Tuple: ", NestedT[4])


# We can use the second index to access other tuples as demonstrated in the figure:

# <img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%202/Images/TuplesNestTwo.png" width="750" align="center">

#  We can access the nested tuples :

# In[18]:


# Print element on each index, including nest indexes

print("Element 2, 0 of Tuple: ",   NestedT[2][0])
print("Element 2, 1 of Tuple: ",   NestedT[2][1])
print("Element 3, 0 of Tuple: ",   NestedT[3][0])
print("Element 3, 1 of Tuple: ",   NestedT[3][1])
print("Element 4, 0 of Tuple: ",   NestedT[4][0])
print("Element 4, 1 of Tuple: ",   NestedT[4][1])


# We can access strings in the second nested tuples using a third index:

# In[19]:


# Print the first element in the second nested tuples

NestedT[2][1][0]


# In[20]:


# Print the second element in the second nested tuples

NestedT[2][1][1]


#  We can use a tree to visualise the process. Each new index corresponds to a deeper level in the tree:

# <img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%202/Images/TuplesNestThree.gif" width="750" align="center">

# Similarly, we can access elements nested deeper in the tree with a fourth index:

# In[21]:


# Print the first element in the second nested tuples

NestedT[4][1][0]


# In[22]:


# Print the second element in the second nested tuples

NestedT[4][1][1]


# The following figure shows the relationship of the tree and the element <code>NestedT[4][1][1]</code>:

# <img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%202/Images/TuplesNestFour.gif" width="750" align="center">

# <h2 id="quiz">Quiz on Tuples</h2>

# Consider the following tuple:

# In[23]:


# sample tuple

genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock",                 "R&B", "progressive rock", "disco") 
genres_tuple


# Find the length of the tuple, <code>genres_tuple</code>:

# In[25]:


# Write your code below and press Shift+Enter to execute
len(genres_tuple)


# <img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%202/Images/TuplesQuiz.png" width="1100" align="center">

# Double-click __here__ for the solution.
# 
# <!-- Your answer is below:
# len(genres_tuple)
# -->

# Access the element, with respect to index 3: 

# In[26]:


# Write your code below and press Shift+Enter to execute
genres_tuple[3]


# Double-click __here__ for the solution.
# 
# <!-- Your answer is below:
# genres_tuple[3]
# -->

# Use slicing to obtain indexes 3, 4 and 5:

# In[29]:


# Write your code below and press Shift+Enter to execute
genres_tuple[3:6]


# Double-click __here__ for the solution.
# 
# <!-- Your answer is below:
# genres_tuple[3:6]
# -->

# Find the first two elements of the tuple <code>genres_tuple</code>:

# In[31]:


# Write your code below and press Shift+Enter to execute
genres_tuple[0:2]


# Double-click __here__ for the solution.
# 
# <!-- Your answer is below:
# genres_tuple[0:2]
# -->

# Find the first index of <code>"disco"</code>:

# In[33]:


# Write your code below and press Shift+Enter to execute
genres_tuple.index("disco")


# Double-click __here__ for the solution.
# 
# <!-- Your answer is below:
# genres_tuple.index("disco")
# -->

# Generate a sorted List from the Tuple <code>C_tuple=(-5, 1, -3)</code>:

# In[41]:


# Write your code below and press Shift+Enter to execute

C_tuple = (-5,1,-3)
C_sorted = sorted(C_tuple)
C_sorted


# Double-click __here__ for the solution.
# 
# <!-- Your answer is below:
# C_tuple = (-5, 1, -3)
# C_list = sorted(C_tuple)
# C_list
# -->

# <hr>
# <h2>The last exercise!</h2>
# <p>Congratulations, you have completed your first lesson and hands-on lab in Python. However, there is one more thing you need to do. The Data Science community encourages sharing work. The best way to share and showcase your work is to share it on GitHub. By sharing your notebook on GitHub you are not only building your reputation with fellow data scientists, but you can also show it off when applying for a job. Even though this was your first piece of work, it is never too early to start building good habits. So, please read and follow <a href="https://cognitiveclass.ai/blog/data-scientists-stand-out-by-sharing-your-notebooks/" target="_blank">this article</a> to learn how to share your work.
# <hr>

# <div class="alert alert-block alert-info" style="margin-top: 20px">
# <h2>Get IBM Watson Studio free of charge!</h2>
#     <p><a href="https://cocl.us/bottemNotebooksPython101Coursera"><img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Ad/BottomAd.png" width="750" align="center"></a></p>
# </div>

# <h3>About the Authors:</h3>  
# <p><a href="https://www.linkedin.com/in/joseph-s-50398b136/" target="_blank">Joseph Santarcangelo</a> is a Data Scientist at IBM, and holds a PhD in Electrical Engineering. His research focused on using Machine Learning, Signal Processing, and Computer Vision to determine how videos impact human cognition. Joseph has been working for IBM since he completed his PhD.</p>

# Other contributors: <a href="www.linkedin.com/in/jiahui-mavis-zhou-a4537814a">Mavis Zhou</a>

# <hr>

# <p>Copyright &copy; 2018 IBM Developer Skills Network. This notebook and its source code are released under the terms of the <a href="https://cognitiveclass.ai/mit-license/">MIT License</a>.</p>
