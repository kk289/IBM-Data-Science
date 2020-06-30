#!/usr/bin/env python
# coding: utf-8

# <div class="alert alert-block alert-info" style="margin-top: 20px">
#     <a href="https://cocl.us/topNotebooksPython101Coursera">
#          <img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Ad/TopAd.png" width="750" align="center">
#     </a>
# </div>

# <a href="https://cognitiveclass.ai/">
#     <img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Ad/CCLog.png" width="200" align="center">
# </a>

# <h1>1D <code>Numpy</code> in Python</h1>

# <p><strong>Welcome!</strong> This notebook will teach you about using <code>Numpy</code> in the Python Programming Language. By the end of this lab, you'll know what <code>Numpy</code> is and the <code>Numpy</code> operations.</p>

# <h2>Table of Contents</h2>
# <div class="alert alert-block alert-info" style="margin-top: 20px">
#     <ul>
#         <li><a href="pre">Preparation</a></li>
#         <li>
#             <a href="numpy">What is Numpy?</a>
#             <ul>
#                 <li><a href="type">Type</a></li>
#                 <li><a href="val">Assign Value</a></li>
#                 <li><a href="slice">Slicing</a></li>
#                 <li><a href="list">Assign Value with List</a></li>
#                 <li><a href="other">Other Attributes</a></li>
#             </ul>
#         </li>
#         <li>
#             <a href="op">Numpy Array Operations</a>
#             <ul>
#                 <li><a href="add">Array Addition</a></li>
#                 <li><a href="multi">Array Multiplication</a></li>
#                 <li><a href="prod">Product of Two Numpy Arrays</a></li>
#                 <li><a href="dot">Dot Product</a></li>
#                 <li><a href="cons">Adding Constant to a Numpy Array</a></li>
#             </ul>
#         </li>
#         <li><a href="math">Mathematical Functions</a></li>
#         <li><a href="lin">Linspace</a></li>
#     </ul>
#     <p>
#         Estimated time needed: <strong>30 min</strong>
#     </p>
# </div>
# 
# <hr>

# <h2 id="pre">Preparation</h2>

# In[1]:


# Import the libraries

import time 
import sys
import numpy as np 

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# Plotting functions

def Plotvec1(u, z, v):
    
    ax = plt.axes()
    ax.arrow(0, 0, *u, head_width=0.05, color='r', head_length=0.1)
    plt.text(*(u + 0.1), 'u')
    
    ax.arrow(0, 0, *v, head_width=0.05, color='b', head_length=0.1)
    plt.text(*(v + 0.1), 'v')
    ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
    plt.text(*(z + 0.1), 'z')
    plt.ylim(-2, 2)
    plt.xlim(-2, 2)

def Plotvec2(a,b):
    ax = plt.axes()
    ax.arrow(0, 0, *a, head_width=0.05, color ='r', head_length=0.1)
    plt.text(*(a + 0.1), 'a')
    ax.arrow(0, 0, *b, head_width=0.05, color ='b', head_length=0.1)
    plt.text(*(b + 0.1), 'b')
    plt.ylim(-2, 2)
    plt.xlim(-2, 2)


# Create a Python List as follows:

# In[3]:


# Create a python list

a = ["0", 1, "two", "3", 4]


# We can access the data via an index:

# <img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%205/Images/NumOneList.png" width="660" />

# We can access each element using a square bracket as follows: 

# In[4]:


# Print each element

print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])


# <hr>

# <h2 id="numpy">What is Numpy?</h2>

# A numpy array is similar to a list. It's usually fixed in size and each element is of the same type. We can cast a list to a numpy array by first importing numpy: 

# In[5]:


# import numpy library

import numpy as np 


#  We then cast the list as follows:

# In[6]:


# Create a numpy array

a = np.array([0, 1, 2, 3, 4])
a


# Each element is of the same type, in this case integers: 

# <img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%205/Images/NumOneNp.png" width="500" />

#  As with lists, we can access each element via a square bracket:

# In[7]:


# Print each element

print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])


# <h3 id="type">Type</h3>

# If we check the type of the array we get <b>numpy.ndarray</b>:

# In[8]:


# Check the type of the array

type(a)


# As numpy arrays contain data of the same type, we can use the attribute "dtype" to obtain the Data-type of the array’s elements. In this case a 64-bit integer: 
# 

# In[9]:


# Check the type of the values stored in numpy array

a.dtype


# We can create a numpy array with real numbers:

# In[10]:


# Create a numpy array

b = np.array([3.1, 11.02, 6.2, 213.2, 5.2])


# When we check the type of the array we get <b>numpy.ndarray</b>:

# In[11]:


# Check the type of array

type(b)


# If we examine the attribute <code>dtype</code> we see float 64, as the elements are not integers: 

# In[12]:


# Check the value type

b.dtype


# <h3 id="val">Assign value</h3>

# We can change the value of the array, consider the array <code>c</code>:

# In[13]:


# Create numpy array

c = np.array([20, 1, 2, 3, 4])
c


# We can change the first element of the array to 100 as follows:

# In[14]:


# Assign the first element to 100

c[0] = 100
c


# We can change the 5th element of the array to 0 as follows:

# In[15]:


# Assign the 5th element to 0

c[4] = 0
c


# <h3 id="slice">Slicing</h3>

# Like lists, we can slice the numpy array, and we can select the elements from 1 to 3 and assign it to a new numpy array <code>d</code> as follows:

# In[16]:


# Slicing the numpy array

d = c[1:4]
d


# We can assign the corresponding indexes to  new values as follows: 

# In[17]:


# Set the fourth element and fifth element to 300 and 400

c[3:5] = 300, 400
c


# <h3 id="list">Assign Value with List</h3>

# Similarly, we can use a list to select a specific index.
# The list ' select ' contains several values:
# 

# In[18]:


# Create the index list

select = [0, 2, 3]


# We can use the list as an argument in the brackets. The output is the elements corresponding to the particular index:

# In[19]:


# Use List to select elements

d = c[select]
d


# We can assign the specified elements to a new value. For example, we can assign the values to 100 000 as follows:

# In[20]:


# Assign the specified elements to new value

c[select] = 100000
c


# <h3 id="other">Other Attributes</h3>

# Let's review some basic array attributes using the array <code>a</code>:

# In[21]:


# Create a numpy array

a = np.array([0, 1, 2, 3, 4])
a


# The attribute <code>size</code> is the number of elements in the array:

# In[22]:


# Get the size of numpy array

a.size


# The next two attributes will make more sense when we get to higher dimensions but let's review them. The attribute <code>ndim</code> represents the number of array dimensions or the rank of the array, in this case, one:

# In[24]:


# Get the number of dimensions of numpy array

a.ndim


# The attribute <code>shape</code> is a tuple of integers indicating the size of the array in each dimension:

# In[25]:


# Get the shape/size of numpy array

a.shape


# In[27]:


# Create a numpy array

a = np.array([1, -1, 1, -1])


# In[28]:


# Get the mean of numpy array

mean = a.mean()
mean


# In[29]:


# Get the standard deviation of numpy array

standard_deviation=a.std()
standard_deviation


# In[30]:


# Create a numpy array

b = np.array([-1, 2, 3, 4, 5])
b


# In[31]:


# Get the biggest value in the numpy array

max_b = b.max()
max_b


# In[32]:


# Get the smallest value in the numpy array

min_b = b.min()
min_b


# <hr>

# <h2 id="op">Numpy Array Operations</h2>

# <h3 id="add">Array Addition</h3>

# Consider the numpy array <code>u</code>:

# In[33]:


u = np.array([1, 0])
u


# Consider the numpy array <code>v</code>:

# In[34]:


v = np.array([0, 1])
v


# We can add the two arrays and assign it to z:

# In[35]:


# Numpy Array Addition

z = u + v
z


#  The operation is equivalent to vector addition:

# In[36]:


# Plot numpy arrays

Plotvec1(u, z, v)


# <h3 id="multi">Array Multiplication</h3>

# Consider the vector numpy array <code>y</code>:

# In[37]:


# Create a numpy array

y = np.array([1, 2])
y


# We can multiply every element in the array by 2:

# In[38]:


# Numpy Array Multiplication

z = 2 * y
z


#  This is equivalent to multiplying a vector by a scaler: 

# <h3 id="prod">Product of Two Numpy Arrays</h3>

# Consider the following array <code>u</code>:

# In[39]:


# Create a numpy array

u = np.array([1, 2])
u


# Consider the following array <code>v</code>:

# In[40]:


# Create a numpy array

v = np.array([3, 2])
v


#  The product of the two numpy arrays <code>u</code> and <code>v</code> is given by:

# In[41]:


# Calculate the production of two numpy arrays

z = u * v
z


# <h3 id="dot">Dot Product</h3>

# The dot product of the two numpy arrays <code>u</code> and <code>v</code> is given by:

# In[42]:


# Calculate the dot product

np.dot(u, v)


# <h3 id="cons">Adding Constant to a Numpy Array</h3>

# Consider the following array: 

# In[43]:


# Create a constant to numpy array

u = np.array([1, 2, 3, -1]) 
u


# Adding the constant 1 to each element in the array:

# In[44]:


# Add the constant to array

u + 1


#  The process is summarised in the following animation:

# <img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%205/Images/NumOneAdd.gif" width="500" />

# <hr>

# <h2 id="math">Mathematical Functions</h2>

#  We can access the value of pie in numpy as follows :

# In[45]:


# The value of pie

np.pi


#  We can create the following numpy array in Radians:

# In[46]:


# Create the numpy array in radians

x = np.array([0, np.pi/2 , np.pi])


# We can apply the function <code>sin</code> to the array <code>x</code> and assign the values to the array <code>y</code>; this applies the sine function to each element in the array:  

# In[47]:


# Calculate the sin of each elements

y = np.sin(x)
y


# <hr>

# <h2 id="lin">Linspace</h2>

#  A useful function for plotting mathematical functions is "linespace".   Linespace returns evenly spaced numbers over a specified interval. We specify the starting point of the sequence and the ending point of the sequence. The parameter "num" indicates the Number of samples to generate, in this case 5:

# In[48]:


# Makeup a numpy array within [-2, 2] and 5 elements

np.linspace(-2, 2, num=5)


# If we change the parameter <code>num</code> to 9, we get 9 evenly spaced numbers over the interval from -2 to 2: 

# In[49]:


# Makeup a numpy array within [-2, 2] and 9 elements

np.linspace(-2, 2, num=9)


# We can use the function line space to generate 100 evenly spaced samples from the interval 0 to 2π: 

# In[50]:


# Makeup a numpy array within [0, 2π] and 100 elements 

x = np.linspace(0, 2*np.pi, num=100)


# We can apply the sine function to each element in the array <code>x</code> and assign it to the array <code>y</code>: 

# In[51]:


# Calculate the sine of x list

y = np.sin(x)


# In[52]:


# Plot the result

plt.plot(x, y)


# <hr>

# <h2 id="quiz">Quiz on 1D Numpy Array</h2>

# Implement the following vector subtraction in numpy: u-v

# In[54]:


# Write your code below and press Shift+Enter to execute

u = np.array([1, 0])
v = np.array([0, 1])
u - v


# Double-click __here__ for the solution.
# 
# <!-- Your answer is below:
# u - v
# -->

# <hr>

# Multiply the numpy array z with -2:

# In[55]:


# Write your code below and press Shift+Enter to execute

z = np.array([2, 4])
z * (-2)


# Double-click __here__ for the solution.
# 
# <!-- Your answer is below:
# -2 * z
# -->

# <hr>

# Consider the list <code>[1, 2, 3, 4, 5]</code> and <code>[1, 0, 1, 0, 1]</code>, and cast both lists to a numpy array then multiply them together:

# In[58]:


# Write your code below and press Shift+Enter to execute
u = np.array([1,2,3,4,5])
v = np.array([1,0,1,0,1])
u*v


# Double-click __here__ for the solution.
# 
# <!-- Your answer is below:
# a = np.array([1, 2, 3, 4, 5])
# b = np.array([1, 0, 1, 0, 1])
# a * b
# -->

# <hr>

# Convert the list <code>[-1, 1]</code> and <code>[1, 1]</code> to numpy arrays <code>a</code> and <code>b</code>.  Then, plot the arrays as vectors using the fuction <code>Plotvec2</code> and find the dot product:

# In[60]:


# Write your code below and press Shift+Enter to execute
a = np.array([-1,1])
b = np.array([1,1])
Plotvec2(a,b)
np.dot(a,b)


# Double-click __here__ for the solution.
# 
# <!-- Your answer is below:
# a = np.array([-1, 1])
# b = np.array([1, 1])
# Plotvec2(a, b)
# print("The dot product is", np.dot(a,b))
# -->

# <hr>

# Convert the list <code>[1, 0]</code> and <code>[0, 1]</code> to numpy arrays <code>a</code> and <code>b</code>. Then, plot the arrays as vectors using the function <code>Plotvec2</code> and find the dot product:

# In[61]:


# Write your code below and press Shift+Enter to execute
a = np.array([1,0])
b = np.array([0,1])
Plotvec2(a,b)
np.dot(a,b)


# Double-click __here__ for the solution.
# 
# <!-- 
# a = np.array([1, 0])
# b = np.array([0, 1])
# Plotvec2(a, b)
# print("The dot product is", np.dot(a, b))
#  -->

# <hr>

# Convert the list <code>[1, 1]</code> and <code>[0, 1]</code> to numpy arrays <code>a</code> and <code>b</code>. Then plot the arrays as vectors using the fuction <code>Plotvec2</code> and find the dot product:

# In[62]:


# Write your code below and press Shift+Enter to execute
a = np.array([1,1])
b = np.array([0,1])
Plotvec2(a,b)
np.dot(a,b)


# Double-click __here__ for the solution.
# 
# <!-- 
# a = np.array([1, 1])
# b = np.array([0, 1])
# Plotvec2(a, b)
# print("The dot product is", np.dot(a, b))
# print("The dot product is", np.dot(a, b))
#  -->

# <hr>

# Why are the results of the dot product for <code>[-1, 1]</code> and <code>[1, 1]</code> and the dot product for <code>[1, 0]</code> and <code>[0, 1]</code> zero, but not zero for the dot product for <code>[1, 1]</code> and <code>[0, 1]</code>? <p><i>Hint: Study the corresponding figures, pay attention to the direction the arrows are pointing to.</i></p>

#         Write your code below and press Shift+Enter to execute
# 4,5 are perpendicular so does it zero.

# Double-click __here__ for the solution.
# 
# <!-- 
# The vectors used for question 4 and 5 are perpendicular. As a result, the dot product is zero. 
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
