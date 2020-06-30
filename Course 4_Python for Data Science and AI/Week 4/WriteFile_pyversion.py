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

# <h1>Write and Save Files in Python</h1>

# <p><strong>Welcome!</strong> This notebook will teach you about write the text to file in the Python Programming Language. By the end of this lab, you'll know how to write to file and copy the file.</p>

# <h2>Table of Contents</h2>
# <div class="alert alert-block alert-info" style="margin-top: 20px">
#     <ul>
#         <li><a href="write">Writing Files</a></li>
#         <li><a href="copy">Copy a File</a></li>
#     </ul>
#     <p>
#         Estimated time needed: <strong>15 min</strong>
#     </p>
# </div>
# 
# <hr>

# <h2 id="write">Writing Files</h2>

#  We can open a file object using the method <code>write()</code> to save the text file to a list. To write the mode, argument must be set to write <b>w</b>. Let’s write a file <b>Example2.txt</b> with the line: <b>“This is line A”</b>

# In[ ]:


# Write line to file

with open('/resources/data/Example2.txt', 'w') as writefile:
    writefile.write("This is line A")


#  We can read the file to see if it worked:

# In[ ]:


# Read file

with open('/resources/data/Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())


# We can write multiple lines:

# In[ ]:


# Write lines to file

with open('/resources/data/Example2.txt', 'w') as writefile:
    writefile.write("This is line A\n")
    writefile.write("This is line B\n")


# The method <code>.write()</code> works similar to the method <code>.readline()</code>, except instead of reading a new line it writes a new line. The process is illustrated in the figure , the different colour coding of the grid represents a new line added to the file after each method call.

# <img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%204/Images/WriteLine.png" width="500" />

# You can check the file to see if your results are correct 

# In[ ]:


# Check whether write to file

with open('/resources/data/Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())


#  By setting the mode argument to append **a**  you can append a new line as follows:

# In[ ]:


# Write a new line to text file

with open('/resources/data/Example2.txt', 'a') as testwritefile:
    testwritefile.write("This is line C\n")


#  You can verify the file has changed by running the following cell:

# In[ ]:


# Verify if the new line is in the text file

with open('/resources/data/Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())


#  We write a list to a <b>.txt</b> file  as follows:

# In[ ]:


# Sample list of text

Lines = ["This is line A\n", "This is line B\n", "This is line C\n"]
Lines


# In[ ]:


# Write the strings in the list to text file

with open('Example2.txt', 'w') as writefile:
    for line in Lines:
        print(line)
        writefile.write(line)


#  We can verify the file is written by reading it and printing out the values:  

# In[ ]:


# Verify if writing to file is successfully executed

with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())


# We can again append to the file by changing the second parameter to <b>a</b>. This adds the code:

# In[ ]:


# Append the line to the file

with open('Example2.txt', 'a') as testwritefile:
    testwritefile.write("This is line D\n")


# We can see the results of appending the file: 

# In[ ]:


# Verify if the appending is successfully executed

with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())


# <hr>

# <h2 id="copy">Copy a File</h2> 

# Let's copy the file <b>Example2.txt</b> to the file <b>Example3.txt</b>:

# In[ ]:


# Copy file to another

with open('Example2.txt','r') as readfile:
    with open('Example3.txt','w') as writefile:
          for line in readfile:
                writefile.write(line)


# We can read the file to see if everything works:

# In[ ]:


# Verify if the copy is successfully executed

with open('Example3.txt','r') as testwritefile:
    print(testwritefile.read())


#  After reading files, we can also write data into files and save them in different file formats like **.txt, .csv, .xls (for excel files) etc**. Let's take a look at some examples.

# Now go to the directory to ensure the <b>.txt</b> file exists and contains the summary data that we wrote.

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
