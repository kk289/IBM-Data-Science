#!/usr/bin/env python
# coding: utf-8

# <a href="https://cognitiveclass.ai/">
#     <img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Ad/CCLog.png" width="200" align="center">
# </a>

# <h1>Dictionaries in Python</h1>

# <p><strong>Welcome!</strong> This notebook will teach you about the dictionaries in the Python Programming Language. By the end of this lab, you'll know the basics dictionary operations in Python, including what it is, and the operations on it.</p>

# <div class="alert alert-block alert-info" style="margin-top: 20px">
#     <a href="http://cocl.us/topNotebooksPython101Coursera">
#          <img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Ad/TopAd.png" width="750" align="center">
#     </a>
# </div>

# <h2>Table of Contents</h2>
# <div class="alert alert-block alert-info" style="margin-top: 20px">
#     <ul>
#         <li>
#             <a href="#dic">Dictionaries</a>
#             <ul>
#                 <li><a href="content">What are Dictionaries?</a></li>
#                 <li><a href="key">Keys</a></li>
#             </ul>
#         </li>
#         <li>
#             <a href="#quiz">Quiz on Dictionaries</a>
#         </li>
#     </ul>
#     <p>
#         Estimated time needed: <strong>20 min</strong>
#     </p>
# </div>
# 
# <hr>

# <h2 id="Dic">Dictionaries</h2>

# <h3 id="content">What are Dictionaries?</h3>

# A dictionary consists of keys and values. It is helpful to compare a dictionary to a list. Instead of the numerical indexes such as a list, dictionaries have keys. These keys are the keys that are used to access values within a dictionary.

# <img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%202/Images/DictsList.png" width="650" />

# An example of a Dictionary <code>Dict</code>:

# In[1]:


# Create the dictionary

Dict = {"key1": 1, "key2": "2", "key3": [3, 3, 3], "key4": (4, 4, 4), ('key5'): 5, (0, 1): 6}
Dict


# The keys can be strings:

# In[2]:


# Access to the value by the key

Dict["key1"]


# Keys can also be any immutable object such as a tuple: 

# In[3]:


# Access to the value by the key

Dict[(0, 1)]


#  Each key is separated from its value by a colon "<code>:</code>".  Commas separate the items, and the whole dictionary is enclosed in curly braces. An empty dictionary without any items is written with just two curly braces, like this  "<code>{}</code>".

# In[4]:


# Create a sample dictionary

release_year_dict = {"Thriller": "1982", "Back in Black": "1980",                     "The Dark Side of the Moon": "1973", "The Bodyguard": "1992",                     "Bat Out of Hell": "1977", "Their Greatest Hits (1971-1975)": "1976",                     "Saturday Night Fever": "1977", "Rumours": "1977"}
release_year_dict


# In summary, like a list, a dictionary holds a sequence of elements. Each element is represented by a key and its corresponding value. Dictionaries are created with two curly braces containing keys and values separated by a colon. For every key, there can only be one single value, however,  multiple keys can hold the same value. Keys can only be strings, numbers, or tuples, but values can be any data type.

# It is helpful to visualize the dictionary as a table, as in the following image. The first column represents the keys, the second column represents the values.

# <img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%202/Images/DictsStructure.png" width="650" />

# <h3 id="key">Keys</h3>

# You can retrieve the values based on the names:

# In[5]:


# Get value by keys

release_year_dict['Thriller'] 


# This corresponds to: 
# 

# <img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%202/Images/DictsKeyOne.png" width="500" />

# Similarly for <b>The Bodyguard</b>

# In[6]:


# Get value by key

release_year_dict['The Bodyguard'] 


# <img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%202/Images/DictsKeyTwo.png" width="500" />

# Now let you retrieve the keys of the dictionary using the method <code>release_year_dict()</code>:

# In[7]:


# Get all the keys in dictionary

release_year_dict.keys() 


# You can retrieve the values using the method  <code>values()</code>:

# In[8]:


# Get all the values in dictionary

release_year_dict.values() 


# We can add an entry:

# In[9]:


# Append value with key into dictionary

release_year_dict['Graduation'] = '2007'
release_year_dict


# We can delete an entry:   

# In[10]:


# Delete entries by key

del(release_year_dict['Thriller'])
del(release_year_dict['Graduation'])
release_year_dict


#  We can verify if an element is in the dictionary: 

# In[11]:


# Verify the key is in the dictionary

'The Bodyguard' in release_year_dict


# <hr>

# <h2 id="quiz">Quiz on Dictionaries</h2>

# <b>You will need this dictionary for the next two questions:</b>

# In[12]:


# Question sample dictionary

soundtrack_dic = {"The Bodyguard":"1992", "Saturday Night Fever":"1977"}
soundtrack_dic 


# a) In the dictionary <code>soundtrack_dict</code> what are the keys ?

# In[16]:


# Write your code below and press Shift+Enter to execute
soundtrack_dic.keys()


# Double-click __here__ for the solution.
# 
# <!-- Your answer is below:
# soundtrack_dic.keys() # The Keys "The Bodyguard" and "Saturday Night Fever" 
# -->

# b) In the dictionary <code>soundtrack_dict</code> what are the values ?

# In[17]:


# Write your code below and press Shift+Enter to execute
soundtrack_dic.values()


# Double-click __here__ for the solution.
# 
# <!-- Your answer is below:
# soundtrack_dic.values() # The values are "1992" and "1977"
# -->

# <hr>

# <b>You will need this dictionary for the following questions:</b>

# The Albums <b>Back in Black</b>, <b>The Bodyguard</b> and <b>Thriller</b> have the following music recording sales in millions 50, 50 and 65 respectively:

# a) Create a dictionary <code>album_sales_dict</code> where the keys are the album name and the sales in millions are the values. 

# In[23]:


# Write your code below and press Shift+Enter to executes
album_sales_dict = {"Back in Black": "50", "The Bodyguard":"50", "Thriller":"65"}
album_sales_dict


# Double-click __here__ for the solution.
# 
# <!-- Your answer is below:
# album_sales_dict = {"The Bodyguard":50, "Back in Black":50, "Thriller":65}
# -->

# b) Use the dictionary to find the total sales of <b>Thriller</b>:

# In[27]:


# Write your code below and press Shift+Enter to execute
album_sales_dict["Thriller"]


# Double-click __here__ for the solution.
# 
# <!-- Your answer is below:
# album_sales_dict["Thriller"]
# -->

# c) Find the names of the albums from the dictionary using the method <code>keys</code>:

# In[28]:


# Write your code below and press Shift+Enter to execute
album_sales_dict.keys()


# Double-click __here__ for the solution.
# 
# <!-- Your answer is below:
# album_sales_dict.keys()
# -->

# d) Find the names of the recording sales from the dictionary using the method <code>values</code>:

# In[29]:


# Write your code below and press Shift+Enter to execute
album_sales_dict.values()


# Double-click __here__ for the solution.
# 
# <!-- Your answer is below:
# album_sales_dict.values()
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
