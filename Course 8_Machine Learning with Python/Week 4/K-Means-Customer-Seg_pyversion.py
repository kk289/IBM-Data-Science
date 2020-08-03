#!/usr/bin/env python
# coding: utf-8

# <a href="https://www.bigdatauniversity.com"><img src="https://ibm.box.com/shared/static/cw2c7r3o20w9zn8gkecaeyjhgw3xdgbj.png" width="400" align="center"></a>
# 
# <h1><center>K-Means Clustering</center></h1>

# ## Introduction
# 
# There are many models for **clustering** out there. In this notebook, we will be presenting the model that is considered one of the simplest models amongst them. Despite its simplicity, the **K-means** is vastly used for clustering in many data science applications, especially useful if you need to quickly discover insights from **unlabeled data**. In this notebook, you will learn how to use k-Means for customer segmentation.
# 
# Some real-world applications of k-means:
# - Customer segmentation
# - Understand what the visitors of a website are trying to accomplish
# - Pattern recognition
# - Machine learning
# - Data compression
# 
# 
# In this notebook we practice k-means clustering with 2 examples:
# - k-means on a random generated dataset
# - Using k-means for customer segmentation

# <h1>Table of contents</h1>
# 
# <div class="alert alert-block alert-info" style="margin-top: 20px">
#     <ul>
#         <li><a href="#random_generated_dataset">k-Means on a randomly generated dataset</a></li>
#             <ol>
#                 <li><a href="#setting_up_K_means">Setting up K-Means</a></li>
#                 <li><a href="#creating_visual_plot">Creating the Visual Plot</a></li>
#             </ol>
#         <li><a href="#customer_segmentation_K_means">Customer Segmentation with K-Means</a></li>
#             <ol>
#                 <li><a href="#pre_processing">Pre-processing</a></li>
#                 <li><a href="#modeling">Modeling</a></li>
#                 <li><a href="#insights">Insights</a></li>
#             </ol>
#     </ul>
# </div>
# <br>
# <hr>

# ### Import libraries
# Lets first import the required libraries.
# Also run <b> %matplotlib inline </b> since we will be plotting in this section.

# In[2]:


import random 
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans 
from sklearn.datasets.samples_generator import make_blobs 
get_ipython().run_line_magic('matplotlib', 'inline')


# <h1 id="random_generated_dataset">k-Means on a randomly generated dataset</h1>
# Lets create our own dataset for this lab!
# 

# First we need to set up a random seed. Use <b>numpy's random.seed()</b> function, where the seed will be set to <b>0</b>

# In[3]:


np.random.seed(0)


# Next we will be making <i> random clusters </i> of points by using the <b> make_blobs </b> class. The <b> make_blobs </b> class can take in many inputs, but we will be using these specific ones. <br> <br>
# <b> <u> Input </u> </b>
# <ul>
#     <li> <b>n_samples</b>: The total number of points equally divided among clusters. </li>
#     <ul> <li> Value will be: 5000 </li> </ul>
#     <li> <b>centers</b>: The number of centers to generate, or the fixed center locations. </li>
#     <ul> <li> Value will be: [[4, 4], [-2, -1], [2, -3],[1,1]] </li> </ul>
#     <li> <b>cluster_std</b>: The standard deviation of the clusters. </li>
#     <ul> <li> Value will be: 0.9 </li> </ul>
# </ul>
# <br>
# <b> <u> Output </u> </b>
# <ul>
#     <li> <b>X</b>: Array of shape [n_samples, n_features]. (Feature Matrix)</li>
#     <ul> <li> The generated samples. </li> </ul> 
#     <li> <b>y</b>: Array of shape [n_samples]. (Response Vector)</li>
#     <ul> <li> The integer labels for cluster membership of each sample. </li> </ul>
# </ul>
# 

# In[4]:


X, y = make_blobs(n_samples=5000, centers=[[4,4], [-2, -1], [2, -3], [1, 1]], cluster_std=0.9)


# Display the scatter plot of the randomly generated data.

# In[5]:


plt.scatter(X[:, 0], X[:, 1], marker='.')


# <h2 id="setting_up_K_means">Setting up K-Means</h2>
# Now that we have our random data, let's set up our K-Means Clustering.

# The KMeans class has many parameters that can be used, but we will be using these three:
# <ul>
#     <li> <b>init</b>: Initialization method of the centroids. </li>
#     <ul>
#         <li> Value will be: "k-means++" </li>
#         <li> k-means++: Selects initial cluster centers for k-mean clustering in a smart way to speed up convergence.</li>
#     </ul>
#     <li> <b>n_clusters</b>: The number of clusters to form as well as the number of centroids to generate. </li>
#     <ul> <li> Value will be: 4 (since we have 4 centers)</li> </ul>
#     <li> <b>n_init</b>: Number of time the k-means algorithm will be run with different centroid seeds. The final results will be the best output of n_init consecutive runs in terms of inertia. </li>
#     <ul> <li> Value will be: 12 </li> </ul>
# </ul>
# 
# Initialize KMeans with these parameters, where the output parameter is called <b>k_means</b>.

# In[6]:


k_means = KMeans(init = "k-means++", n_clusters = 4, n_init = 12)


# Now let's fit the KMeans model with the feature matrix we created above, <b> X </b>

# In[7]:


k_means.fit(X)


# Now let's grab the labels for each point in the model using KMeans' <b> .labels\_ </b> attribute and save it as <b> k_means_labels </b> 

# In[8]:


k_means_labels = k_means.labels_
k_means_labels


# We will also get the coordinates of the cluster centers using KMeans' <b> .cluster&#95;centers&#95; </b> and save it as <b> k_means_cluster_centers </b>

# In[9]:


k_means_cluster_centers = k_means.cluster_centers_
k_means_cluster_centers


# <h2 id="creating_visual_plot">Creating the Visual Plot</h2>
# So now that we have the random data generated and the KMeans model initialized, let's plot them and see what it looks like!

# Please read through the code and comments to understand how to plot the model.

# In[10]:


# Initialize the plot with the specified dimensions.
fig = plt.figure(figsize=(6, 4))

# Colors uses a color map, which will produce an array of colors based on
# the number of labels there are. We use set(k_means_labels) to get the
# unique labels.
colors = plt.cm.Spectral(np.linspace(0, 1, len(set(k_means_labels))))

# Create a plot
ax = fig.add_subplot(1, 1, 1)

# For loop that plots the data points and centroids.
# k will range from 0-3, which will match the possible clusters that each
# data point is in.
for k, col in zip(range(len([[4,4], [-2, -1], [2, -3], [1, 1]])), colors):

    # Create a list of all data points, where the data poitns that are 
    # in the cluster (ex. cluster 0) are labeled as true, else they are
    # labeled as false.
    my_members = (k_means_labels == k)
    
    # Define the centroid, or cluster center.
    cluster_center = k_means_cluster_centers[k]
    
    # Plots the datapoints with color col.
    ax.plot(X[my_members, 0], X[my_members, 1], 'w', markerfacecolor=col, marker='.')
    
    # Plots the centroids with specified color, but with a darker outline
    ax.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,  markeredgecolor='k', markersize=6)

# Title of the plot
ax.set_title('KMeans')

# Remove x-axis ticks
ax.set_xticks(())

# Remove y-axis ticks
ax.set_yticks(())

# Show the plot
plt.show()


# ## Practice
# Try to cluster the above dataset into 3 clusters.  
# Notice: do not generate data again, use the same dataset as above.

# In[12]:


k_means3 = KMeans(init = "k-means++", n_clusters = 3, n_init = 12)
k_means3.fit(X)
fig = plt.figure(figsize=(6, 4))
colors = plt.cm.Spectral(np.linspace(0, 1, len(set(k_means3.labels_))))
ax = fig.add_subplot(1, 1, 1)
for k, col in zip(range(len(k_means3.cluster_centers_)), colors):
    my_members = (k_means3.labels_ == k)
    cluster_center = k_means3.cluster_centers_[k]
    ax.plot(X[my_members, 0], X[my_members, 1], 'w', markerfacecolor=col, marker='.')
    ax.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,  markeredgecolor='k', markersize=6)
plt.show()


# <h1 id="customer_segmentation_K_means">Customer Segmentation with K-Means</h1>
# Imagine that you have a customer dataset, and you need to apply customer segmentation on this historical data.
# Customer segmentation is the practice of partitioning a customer base into groups of individuals that have similar characteristics. It is a significant strategy as a business can target these specific groups of customers and effectively allocate marketing resources. For example, one group might contain customers who are high-profit and low-risk, that is, more likely to purchase products, or subscribe for a service. A business task is to retaining those customers. Another group might include customers from non-profit organizations. And so on.
# 
# Lets download the dataset. To download the data, we will use **`!wget`** to download it from IBM Object Storage.  
# __Did you know?__ When it comes to Machine Learning, you will likely be working with large datasets. As a business, where can you host your data? IBM is offering a unique opportunity for businesses, with 10 Tb of IBM Cloud Object Storage: [Sign up now for free](http://cocl.us/ML0101EN-IBM-Offer-CC)

# In[14]:


get_ipython().system('wget -O Cust_Segmentation.csv https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/ML0101ENv3/labs/Cust_Segmentation.csv')


# In[15]:


import pandas as pd
cust_df = pd.read_csv("Cust_Segmentation.csv")
cust_df.head()


# ### Load Data From CSV File  
# Before you can work with the data, you must use the URL to get the Cust_Segmentation.csv.

# <h2 id="pre_processing">Pre-processing</h2

# As you can see, __Address__ in this dataset is a categorical variable. k-means algorithm isn't directly applicable to categorical variables because Euclidean distance function isn't really meaningful for discrete variables. So, lets drop this feature and run clustering.

# In[ ]:


df = cust_df.drop('Address', axis=1)
df.head()


# #### Normalizing over the standard deviation
# Now let's normalize the dataset. But why do we need normalization in the first place? Normalization is a statistical method that helps mathematical-based algorithms to interpret features with different magnitudes and distributions equally. We use __StandardScaler()__ to normalize our dataset.

# In[ ]:


from sklearn.preprocessing import StandardScaler
X = df.values[:,1:]
X = np.nan_to_num(X)
Clus_dataSet = StandardScaler().fit_transform(X)
Clus_dataSet


# <h2 id="modeling">Modeling</h2>

# In our example (if we didn't have access to the k-means algorithm), it would be the same as guessing that each customer group would have certain age, income, education, etc, with multiple tests and experiments. However, using the K-means clustering we can do all this process much easier.
# 
# Lets apply k-means on our dataset, and take look at cluster labels.

# In[ ]:


clusterNum = 3
k_means = KMeans(init = "k-means++", n_clusters = clusterNum, n_init = 12)
k_means.fit(X)
labels = k_means.labels_
print(labels)


# <h2 id="insights">Insights</h2>
# We assign the labels to each row in dataframe.

# In[ ]:


df["Clus_km"] = labels
df.head(5)


# We can easily check the centroid values by averaging the features in each cluster.

# In[ ]:


df.groupby('Clus_km').mean()


# Now, lets look at the distribution of customers based on their age and income:

# In[ ]:


area = np.pi * ( X[:, 1])**2  
plt.scatter(X[:, 0], X[:, 3], s=area, c=labels.astype(np.float), alpha=0.5)
plt.xlabel('Age', fontsize=18)
plt.ylabel('Income', fontsize=16)

plt.show()


# In[ ]:


from mpl_toolkits.mplot3d import Axes3D 
fig = plt.figure(1, figsize=(8, 6))
plt.clf()
ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)

plt.cla()
# plt.ylabel('Age', fontsize=18)
# plt.xlabel('Income', fontsize=16)
# plt.zlabel('Education', fontsize=16)
ax.set_xlabel('Education')
ax.set_ylabel('Age')
ax.set_zlabel('Income')

ax.scatter(X[:, 1], X[:, 0], X[:, 3], c= labels.astype(np.float))


# k-means will partition your customers into mutually exclusive groups, for example, into 3 clusters. The customers in each cluster are similar to each other demographically.
# Now we can create a profile for each group, considering the common characteristics of each cluster. 
# For example, the 3 clusters can be:
# 
# - AFFLUENT, EDUCATED AND OLD AGED
# - MIDDLE AGED AND MIDDLE INCOME
# - YOUNG AND LOW INCOME

# <h2>Want to learn more?</h2>
# 
# IBM SPSS Modeler is a comprehensive analytics platform that has many machine learning algorithms. It has been designed to bring predictive intelligence to decisions made by individuals, by groups, by systems – by your enterprise as a whole. A free trial is available through this course, available here: <a href="http://cocl.us/ML0101EN-SPSSModeler">SPSS Modeler</a>
# 
# Also, you can use Watson Studio to run these notebooks faster with bigger datasets. Watson Studio is IBM's leading cloud solution for data scientists, built by data scientists. With Jupyter notebooks, RStudio, Apache Spark and popular libraries pre-packaged in the cloud, Watson Studio enables data scientists to collaborate on their projects without having to install anything. Join the fast-growing community of Watson Studio users today with a free account at <a href="https://cocl.us/ML0101EN_DSX">Watson Studio</a>
# 
# <h3>Thanks for completing this lesson!</h3>
# 
# <h4>Author:  <a href="https://ca.linkedin.com/in/saeedaghabozorgi">Saeed Aghabozorgi</a></h4>
# <p><a href="https://ca.linkedin.com/in/saeedaghabozorgi">Saeed Aghabozorgi</a>, PhD is a Data Scientist in IBM with a track record of developing enterprise level applications that substantially increases clients’ ability to turn data into actionable knowledge. He is a researcher in data mining field and expert in developing advanced analytic methods like machine learning and statistical modelling on large datasets.</p>
# 
# <hr>
# 
# <p>Copyright &copy; 2018 <a href="https://cocl.us/DX0108EN_CC">Cognitive Class</a>. This notebook and its source code are released under the terms of the <a href="https://bigdatauniversity.com/mit-license/">MIT License</a>.</p>
