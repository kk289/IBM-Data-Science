#!/usr/bin/env python
# coding: utf-8

# 

# <a href="https://cognitiveclass.ai/">
#     <img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Ad/CCLog.png" width="200" align="center">
# </a>

# <h1>Loops in Python</h1>

# <p><strong>Welcome!</strong> This notebook will teach you about the loops in the Python Programming Language. By the end of this lab, you'll know how to use the loop statements in Python, including for loop, and while loop.</p>

# <div class="alert alert-block alert-info" style="margin-top: 20px">
#     <a href="https://cocl.us/topNotebooksPython101Coursera">
#          <img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Ad/TopAd.png" width="750" align="center">
#     </a>
# </div>

# <h2>Table of Contents</h2>
# <div class="alert alert-block alert-info" style="margin-top: 20px">
#     <ul>
#         <li>
#             <a href="#loop">Loops</a>
#             <ul>
#                 <li><a href="range">Range</a></li>
#                 <li><a href="for">What is <code>for</code> loop?</a></li>
#                 <li><a href="while">What is <code>while</code> loop?</a></li>
#             </ul>
#         </li>
#         <li>
#             <a href="#quiz">Quiz on Loops</a>
#         </li>
#     </ul>
#     <p>
#         Estimated time needed: <strong>20 min</strong>
#     </p>
# </div>
# 
# <hr>

# <h2 id="loop">Loops</h2>

# <h3 id="range">Range</h3>

# Sometimes, you might want to repeat a given operation many times. Repeated executions like this are performed by <b>loops</b>. We will look at two types of loops, <code>for</code> loops and <code>while</code> loops.
# 
# Before we discuss loops lets discuss the <code>range</code> object. It is helpful to think of the range object as an ordered list. For now, let's look at the simplest case. If we would like to generate a sequence that contains three elements ordered from 0 to 2 we simply use the following command:

# In[1]:


# Use the range

range(3)


# <img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%203/Images/LoopsRange.png" width="300" />

# <h3 id="for">What is <code>for</code> loop?</h3>

# The <code>for</code> loop enables you to execute a code block multiple times. For example, you would use this if you would like to print out every element in a list.    
# Let's try to use a <code>for</code> loop to print all the years presented in the list <code>dates</code>:

# This can be done as follows:

# In[2]:


# For loop example

dates = [1982,1980,1973]
N = len(dates)

for i in range(N):
    print(dates[i])     


# The code in the indent is executed <code>N</code> times, each time the value of <code>i</code> is increased by 1 for every execution. The statement executed is to <code>print</code> out the value in the list at index <code>i</code> as shown here:

# <img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%203/Images/LoopsForRange.gif" width="800" />

# In this example we can print out a sequence of numbers from 0 to 7:

# In[3]:


# Example of for loop

for i in range(0, 8):
    print(i)


# In Python we can directly access the elements in the list as follows: 

# In[4]:


# Exmaple of for loop, loop through list

for year in dates:  
    print(year)   


# For each iteration, the value of the variable <code>years</code> behaves like the value of <code>dates[i]</code> in the  first example:

# <img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%203/Images/LoopsForList.gif" width="800">

# We can change the elements in a list:

# In[5]:


# Use for loop to change the elements in list

squares = ['red', 'yellow', 'green', 'purple', 'blue']

for i in range(0, 5):
    print("Before square ", i, 'is',  squares[i])
    squares[i] = 'weight'
    print("After square ", i, 'is',  squares[i])


#  We can access the index and the elements of a list as follows: 

# In[6]:


# Loop through the list and iterate on both index and element value

squares=['red', 'yellow', 'green', 'purple', 'blue']

for i, square in enumerate(squares):
    print(i, square)


# <h3 id="while">What is <code>while</code> loop?</h3>

# As you can see, the <code>for</code> loop is used for a controlled flow of repetition. However, what if we don't know when we want to stop the loop? What if we want to keep executing a code block until a certain condition is met? The <code>while</code> loop exists as a tool for repeated execution based on a condition. The code block will keep being executed until the given logical condition returns a **False** boolean value.
# 

# Let’s say we would like to iterate through list <code>dates</code> and stop at the year 1973, then print out the number of iterations. This can be done with the following block of code:

# In[7]:


# While Loop Example

dates = [1982, 1980, 1973, 2000]

i = 0
year = 0

while(year != 1973):
    year = dates[i]
    i = i + 1
    print(year)

print("It took ", i ,"repetitions to get out of loop.")


# A while loop iterates merely until the condition in the argument is not  met, as shown in the following figure:

# <img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%203/Images/LoopsWhile.gif" width="650" />

# <hr>

# <h2 id="quiz">Quiz on Loops</h2>

# Write a <code>for</code> loop the prints out all the element between <b>-5</b> and <b>5</b> using the range function.

# In[9]:


# Write your code below and press Shift+Enter to execute

for i in range(-5,6):
    print(i)


# Double-click __here__ for the solution.
# <!-- 
# for i in range(-5, 6):
#     print(i)
# -->

# Print the elements of the following list:
# <code>Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']</code>
# Make sure you follow Python conventions.

# In[15]:


# Write your code below and press Shift+Enter to execute
Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']

for Genres in Genres:
    print(Genres)
    


# Double-click __here__ for the solution.
# <!-- 
# Genres = ['rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
# for Genre in Genres:
#     print(Genre)
# -->

# <hr>

# Write a for loop that prints out the following list: <code>squares=['red', 'yellow', 'green', 'purple', 'blue']</code>

# In[16]:


# Write your code below and press Shift+Enter to execute
squares=['red', 'yellow', 'green', 'purple', 'blue']

i = len(squares)
for i, squares in enumerate(squares):
    print(squares)


# Double-click __here__ for the solution.
# <!-- 
# squares=['red', 'yellow', 'green', 'purple', 'blue']
# for square in squares:
#     print(square)
#  -->

# <hr>

# Write a while loop to display the values of the Rating of an album playlist stored in the list <code>PlayListRatings</code>. If the score is less than 6, exit the loop. The list <code>PlayListRatings</code> is given by: <code>PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]</code>

# In[ ]:


# Write your code below and press Shift+Enter to execute
PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i = 1
rating = PlayListRatings[0]

while rating >= 6:
    print(rating)
    rating = PlayListRatings[i]
    i = i + 1
print(rating)    
    


# Double-click __here__ for the solution.
# <!-- 
# PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
# i = 1
# Rating = PlayListRatings[0]
# while(Rating >= 6):
#     print(Rating)
#     Rating = PlayListRatings[i]
#     i = i + 1
#  -->

# <hr>

# Write a while loop to copy the strings <code>'orange'</code> of the list <code>squares</code> to the list <code>new_squares</code>. Stop and exit the loop if the value on the list is not <code>'orange'</code>:

# In[23]:


# Write your code below and press Shift+Enter to execute

squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i = 0

while squares[i] == 'orange':
    new_squares.append(squares[i])
    i = i + 1
print(new_squares)   


# Double-click __here__ for the solution.
# <!-- 
# squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
# new_squares = []
# i = 0
# while(squares[i] == 'orange'):
#     new_squares.append(squares[i])
#     i = i + 1
# print (new_squares)
#  -->

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

# Other contributors: <a href="www.linkedin.com/in/jiahui-mavis-zhou-a4537814a">Mavis Zhou</a>, <a href="https://www.linkedin.com/in/reevejamesd/">James Reeve</a>

# <hr>

# <p>Copyright &copy; 2018 IBM Developer Skills Network. This notebook and its source code are released under the terms of the <a href="https://cognitiveclass.ai/mit-license/">MIT License</a>.</p>
