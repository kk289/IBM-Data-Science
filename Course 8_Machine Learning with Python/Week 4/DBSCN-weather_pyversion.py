#!/usr/bin/env python
# coding: utf-8

# <a href="https://www.bigdatauniversity.com"><img src = "https://ibm.box.com/shared/static/cw2c7r3o20w9zn8gkecaeyjhgw3xdgbj.png" width = 400, align = "center"></a>
# # <center>Density-Based Clustering</center>

# Most of the traditional clustering techniques, such as k-means, hierarchical and fuzzy clustering, can be used to group data without supervision. 
# 
# However, when applied to tasks with arbitrary shape clusters, or clusters within cluster, the traditional techniques might be unable to achieve good results. That is, elements in the same cluster might not share enough similarity or the performance may be poor.
# Additionally, Density-based Clustering locates regions of high density that are separated from one another by regions of low density. Density, in this context, is defined as the number of points within a specified radius.
# 
# 
# 
# In this section, the main focus will be manipulating the data and properties of DBSCAN and observing the resulting clustering.

# Import the following libraries:
# <ul>
#     <li> <b>numpy as np</b> </li>
#     <li> <b>DBSCAN</b> from <b>sklearn.cluster</b> </li>
#     <li> <b>make_blobs</b> from <b>sklearn.datasets.samples_generator</b> </li>
#     <li> <b>StandardScaler</b> from <b>sklearn.preprocessing</b> </li>
#     <li> <b>matplotlib.pyplot as plt</b> </li>
# </ul> <br>
# Remember <b> %matplotlib inline </b> to display plots

# In[1]:


# Notice: For visualization of map, you need basemap package.
# if you dont have basemap install on your machine, you can use the following line to install it
# !conda install -c conda-forge  basemap==1.1.0  matplotlib==2.2.2  -y
# Notice: you maight have to refresh your page and re-run the notebook after installation


# In[2]:


import numpy as np 
from sklearn.cluster import DBSCAN 
from sklearn.datasets.samples_generator import make_blobs 
from sklearn.preprocessing import StandardScaler 
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')


# ### Data generation
# The function below will generate the data points and requires these inputs:
# <ul>
#     <li> <b>centroidLocation</b>: Coordinates of the centroids that will generate the random data. </li>
#     <ul> <li> Example: input: [[4,3], [2,-1], [-1,4]] </li> </ul>
#     <li> <b>numSamples</b>: The number of data points we want generated, split over the number of centroids (# of centroids defined in centroidLocation) </li>
#     <ul> <li> Example: 1500 </li> </ul>
#     <li> <b>clusterDeviation</b>: The standard deviation between the clusters. The larger the number, the further the spacing. </li>
#     <ul> <li> Example: 0.5 </li> </ul>
# </ul>

# In[3]:


def createDataPoints(centroidLocation, numSamples, clusterDeviation):
    # Create random data and store in feature matrix X and response vector y.
    X, y = make_blobs(n_samples=numSamples, centers=centroidLocation, 
                                cluster_std=clusterDeviation)
    
    # Standardize features by removing the mean and scaling to unit variance
    X = StandardScaler().fit_transform(X)
    return X, y


# Use <b>createDataPoints</b> with the <b>3 inputs</b> and store the output into variables <b>X</b> and <b>y</b>.

# In[4]:


X, y = createDataPoints([[4,3], [2,-1], [-1,4]] , 1500, 0.5)


# ### Modeling
# DBSCAN stands for Density-Based Spatial Clustering of Applications with Noise. This technique is one of the most common clustering algorithms  which works based on density of object.
# The whole idea is that if a particular point belongs to a cluster, it should be near to lots of other points in that cluster.
# 
# It works based on two parameters: Epsilon and Minimum Points  
# __Epsilon__ determine a specified radius that if includes enough number of points within, we call it dense area  
# __minimumSamples__ determine the minimum number of data points we want in a neighborhood to define a cluster.
# 
# 

# In[5]:


epsilon = 0.3
minimumSamples = 7
db = DBSCAN(eps=epsilon, min_samples=minimumSamples).fit(X)
labels = db.labels_
labels


# ### Distinguish outliers
# Lets Replace all elements with 'True' in core_samples_mask that are in the cluster, 'False' if the points are outliers.

# In[6]:


# Firts, create an array of booleans using the labels from db.
core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True
core_samples_mask


# In[7]:


# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
n_clusters_


# In[8]:


# Remove repetition in labels by turning it into a set.
unique_labels = set(labels)
unique_labels


# ### Data visualization

# In[11]:


# Create colors for the clusters.
colors = plt.cm.Spectral(np.linspace(0, 1, len(unique_labels)))


# In[12]:


# Plot the points with colors
for k, col in zip(unique_labels, colors):
    if k == -1:
        # Black used for noise.
        col = 'k'

    class_member_mask = (labels == k)

    # Plot the datapoints that are clustered
    xy = X[class_member_mask & core_samples_mask]
    plt.scatter(xy[:, 0], xy[:, 1],s=50, c=[col], marker=u'o', alpha=0.5)

    # Plot the outliers
    xy = X[class_member_mask & ~core_samples_mask]
    plt.scatter(xy[:, 0], xy[:, 1],s=50, c=[col], marker=u'o', alpha=0.5)


# ## Practice
# To better underestand differences between partitional and density-based clusteitng, try to cluster the above dataset into 3 clusters using k-Means.  
# Notice: do not generate data again, use the same dataset as above.

# In[14]:


from sklearn.cluster import KMeans 
k = 3
k_means3 = KMeans(init = "k-means++", n_clusters = k, n_init = 12)
k_means3.fit(X)
fig = plt.figure(figsize=(6, 4))
ax = fig.add_subplot(1, 1, 1)

for k, col in zip(range(k), colors):
    my_members = (k_means3.labels_ == k)
    plt.scatter(X[my_members, 0], X[my_members, 1],  c=col, marker=u'o', alpha=0.5)
    
plt.show()


# 
# 
# 
# <h1 align=center> Weather Station Clustering using DBSCAN & scikit-learn </h1>
# <hr>
# 
# DBSCAN is specially very good for tasks like class identification on a spatial context. The wonderful attribute of DBSCAN algorithm is that it can find out any arbitrary shape cluster without getting affected by noise. For example, this following example cluster the location of weather stations in Canada.
# <Click 1>
# DBSCAN can be used here, for instance, to find the group of stations which show the same weather condition. As you can see, it not only finds different arbitrary shaped clusters, can find the denser part of data-centered samples by ignoring less-dense areas or noises.
# 
# let's start playing with the data. We will be working according to the following workflow: </font>
# 1. Loading data
# - Overview data
# - Data cleaning
# - Data selection
# - Clusteing

# ### About the dataset
# 
# 		
# <h4 align = "center">
# Environment Canada    
# Monthly Values for July - 2015	
# </h4>
# <html>
# <head>
# <style>
# table {
#     font-family: arial, sans-serif;
#     border-collapse: collapse;
#     width: 100%;
# }
# 
# td, th {
#     border: 1px solid #dddddd;
#     text-align: left;
#     padding: 8px;
# }
# 
# tr:nth-child(even) {
#     background-color: #dddddd;
# }
# </style>
# </head>
# <body>
# 
# <table>
#   <tr>
#     <th>Name in the table</th>
#     <th>Meaning</th>
#   </tr>
#   <tr>
#     <td><font color = "green"><strong>Stn_Name</font></td>
#     <td><font color = "green"><strong>Station Name</font</td>
#   </tr>
#   <tr>
#     <td><font color = "green"><strong>Lat</font></td>
#     <td><font color = "green"><strong>Latitude (North+, degrees)</font></td>
#   </tr>
#   <tr>
#     <td><font color = "green"><strong>Long</font></td>
#     <td><font color = "green"><strong>Longitude (West - , degrees)</font></td>
#   </tr>
#   <tr>
#     <td>Prov</td>
#     <td>Province</td>
#   </tr>
#   <tr>
#     <td>Tm</td>
#     <td>Mean Temperature (°C)</td>
#   </tr>
#   <tr>
#     <td>DwTm</td>
#     <td>Days without Valid Mean Temperature</td>
#   </tr>
#   <tr>
#     <td>D</td>
#     <td>Mean Temperature difference from Normal (1981-2010) (°C)</td>
#   </tr>
#   <tr>
#     <td><font color = "black">Tx</font></td>
#     <td><font color = "black">Highest Monthly Maximum Temperature (°C)</font></td>
#   </tr>
#   <tr>
#     <td>DwTx</td>
#     <td>Days without Valid Maximum Temperature</td>
#   </tr>
#   <tr>
#     <td><font color = "black">Tn</font></td>
#     <td><font color = "black">Lowest Monthly Minimum Temperature (°C)</font></td>
#   </tr>
#   <tr>
#     <td>DwTn</td>
#     <td>Days without Valid Minimum Temperature</td>
#   </tr>
#   <tr>
#     <td>S</td>
#     <td>Snowfall (cm)</td>
#   </tr>
#   <tr>
#     <td>DwS</td>
#     <td>Days without Valid Snowfall</td>
#   </tr>
#   <tr>
#     <td>S%N</td>
#     <td>Percent of Normal (1981-2010) Snowfall</td>
#   </tr>
#   <tr>
#     <td><font color = "green"><strong>P</font></td>
#     <td><font color = "green"><strong>Total Precipitation (mm)</font></td>
#   </tr>
#   <tr>
#     <td>DwP</td>
#     <td>Days without Valid Precipitation</td>
#   </tr>
#   <tr>
#     <td>P%N</td>
#     <td>Percent of Normal (1981-2010) Precipitation</td>
#   </tr>
#   <tr>
#     <td>S_G</td>
#     <td>Snow on the ground at the end of the month (cm)</td>
#   </tr>
#   <tr>
#     <td>Pd</td>
#     <td>Number of days with Precipitation 1.0 mm or more</td>
#   </tr>
#   <tr>
#     <td>BS</td>
#     <td>Bright Sunshine (hours)</td>
#   </tr>
#   <tr>
#     <td>DwBS</td>
#     <td>Days without Valid Bright Sunshine</td>
#   </tr>
#   <tr>
#     <td>BS%</td>
#     <td>Percent of Normal (1981-2010) Bright Sunshine</td>
#   </tr>
#   <tr>
#     <td>HDD</td>
#     <td>Degree Days below 18 °C</td>
#   </tr>
#   <tr>
#     <td>CDD</td>
#     <td>Degree Days above 18 °C</td>
#   </tr>
#   <tr>
#     <td>Stn_No</td>
#     <td>Climate station identifier (first 3 digits indicate   drainage basin, last 4 characters are for sorting alphabetically).</td>
#   </tr>
#   <tr>
#     <td>NA</td>
#     <td>Not Available</td>
#   </tr>
# 
# 
# </table>
# 
# </body>
# </html>
# 
#  

# ### 1-Download data
# To download the data, we will use **`!wget`**. To download the data, we will use `!wget` to download it from IBM Object Storage.  
# __Did you know?__ When it comes to Machine Learning, you will likely be working with large datasets. As a business, where can you host your data? IBM is offering a unique opportunity for businesses, with 10 Tb of IBM Cloud Object Storage: [Sign up now for free](http://cocl.us/ML0101EN-IBM-Offer-CC)

# In[15]:


get_ipython().system('wget -O weather-stations20140101-20141231.csv https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/ML0101ENv3/labs/weather-stations20140101-20141231.csv')


# ### 2- Load the dataset
# We will import the .csv then we creates the columns for year, month and day.

# In[ ]:


import csv
import pandas as pd
import numpy as np

filename='weather-stations20140101-20141231.csv'

#Read csv
pdf = pd.read_csv(filename)
pdf.head(5)


# ### 3-Cleaning
# Lets remove rows that dont have any value in the __Tm__ field.

# In[ ]:


pdf = pdf[pd.notnull(pdf["Tm"])]
pdf = pdf.reset_index(drop=True)
pdf.head(5)


# ### 4-Visualization
# Visualization of stations on map using basemap package. The matplotlib basemap toolkit is a library for plotting 2D data on maps in Python. Basemap does not do any plotting on it’s own, but provides the facilities to transform coordinates to a map projections. 
# 
# Please notice that the size of each data points represents the average of maximum temperature for each station in a year. 

# In[ ]:


from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from pylab import rcParams
get_ipython().run_line_magic('matplotlib', 'inline')
rcParams['figure.figsize'] = (14,10)

llon=-140
ulon=-50
llat=40
ulat=65

pdf = pdf[(pdf['Long'] > llon) & (pdf['Long'] < ulon) & (pdf['Lat'] > llat) &(pdf['Lat'] < ulat)]

my_map = Basemap(projection='merc',
            resolution = 'l', area_thresh = 1000.0,
            llcrnrlon=llon, llcrnrlat=llat, #min longitude (llcrnrlon) and latitude (llcrnrlat)
            urcrnrlon=ulon, urcrnrlat=ulat) #max longitude (urcrnrlon) and latitude (urcrnrlat)

my_map.drawcoastlines()
my_map.drawcountries()
# my_map.drawmapboundary()
my_map.fillcontinents(color = 'white', alpha = 0.3)
my_map.shadedrelief()

# To collect data based on stations        

xs,ys = my_map(np.asarray(pdf.Long), np.asarray(pdf.Lat))
pdf['xm']= xs.tolist()
pdf['ym'] =ys.tolist()

#Visualization1
for index,row in pdf.iterrows():
#   x,y = my_map(row.Long, row.Lat)
   my_map.plot(row.xm, row.ym,markerfacecolor =([1,0,0]),  marker='o', markersize= 5, alpha = 0.75)

#plt.text(x,y,stn)
plt.show()


# ### 5- Clustering of stations based on their location i.e. Lat & Lon
# 
# __DBSCAN__ form sklearn library can runs DBSCAN clustering from vector array or distance matrix. In our case, we pass it the Numpy array Clus_dataSet to find core samples of high density and expands clusters from them. 

# In[ ]:


from sklearn.cluster import DBSCAN
import sklearn.utils
from sklearn.preprocessing import StandardScaler
sklearn.utils.check_random_state(1000)
Clus_dataSet = pdf[['xm','ym']]
Clus_dataSet = np.nan_to_num(Clus_dataSet)
Clus_dataSet = StandardScaler().fit_transform(Clus_dataSet)

# Compute DBSCAN
db = DBSCAN(eps=0.15, min_samples=10).fit(Clus_dataSet)
core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True
labels = db.labels_
pdf["Clus_Db"]=labels

realClusterNum=len(set(labels)) - (1 if -1 in labels else 0)
clusterNum = len(set(labels)) 


# A sample of clusters
pdf[["Stn_Name","Tx","Tm","Clus_Db"]].head(5)


# As you can see for outliers, the cluster label is -1

# In[ ]:


set(labels)


# ### 6- Visualization of clusters based on location
# Now, we can visualize the clusters using basemap:

# In[ ]:


from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from pylab import rcParams
get_ipython().run_line_magic('matplotlib', 'inline')
rcParams['figure.figsize'] = (14,10)

my_map = Basemap(projection='merc',
            resolution = 'l', area_thresh = 1000.0,
            llcrnrlon=llon, llcrnrlat=llat, #min longitude (llcrnrlon) and latitude (llcrnrlat)
            urcrnrlon=ulon, urcrnrlat=ulat) #max longitude (urcrnrlon) and latitude (urcrnrlat)

my_map.drawcoastlines()
my_map.drawcountries()
#my_map.drawmapboundary()
my_map.fillcontinents(color = 'white', alpha = 0.3)
my_map.shadedrelief()

# To create a color map
colors = plt.get_cmap('jet')(np.linspace(0.0, 1.0, clusterNum))



#Visualization1
for clust_number in set(labels):
    c=(([0.4,0.4,0.4]) if clust_number == -1 else colors[np.int(clust_number)])
    clust_set = pdf[pdf.Clus_Db == clust_number]                    
    my_map.scatter(clust_set.xm, clust_set.ym, color =c,  marker='o', s= 20, alpha = 0.85)
    if clust_number != -1:
        cenx=np.mean(clust_set.xm) 
        ceny=np.mean(clust_set.ym) 
        plt.text(cenx,ceny,str(clust_number), fontsize=25, color='red',)
        print ("Cluster "+str(clust_number)+', Avg Temp: '+ str(np.mean(clust_set.Tm)))


# ### 7- Clustering of stations based on their location, mean, max, and min Temperature
# In this section we re-run DBSCAN, but this time on a 5-dimensional dataset:

# In[ ]:


from sklearn.cluster import DBSCAN
import sklearn.utils
from sklearn.preprocessing import StandardScaler
sklearn.utils.check_random_state(1000)
Clus_dataSet = pdf[['xm','ym','Tx','Tm','Tn']]
Clus_dataSet = np.nan_to_num(Clus_dataSet)
Clus_dataSet = StandardScaler().fit_transform(Clus_dataSet)

# Compute DBSCAN
db = DBSCAN(eps=0.3, min_samples=10).fit(Clus_dataSet)
core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True
labels = db.labels_
pdf["Clus_Db"]=labels

realClusterNum=len(set(labels)) - (1 if -1 in labels else 0)
clusterNum = len(set(labels)) 


# A sample of clusters
pdf[["Stn_Name","Tx","Tm","Clus_Db"]].head(5)


# ### 8- Visualization of clusters based on location and Temperture
# 

# In[ ]:


from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from pylab import rcParams
get_ipython().run_line_magic('matplotlib', 'inline')
rcParams['figure.figsize'] = (14,10)

my_map = Basemap(projection='merc',
            resolution = 'l', area_thresh = 1000.0,
            llcrnrlon=llon, llcrnrlat=llat, #min longitude (llcrnrlon) and latitude (llcrnrlat)
            urcrnrlon=ulon, urcrnrlat=ulat) #max longitude (urcrnrlon) and latitude (urcrnrlat)

my_map.drawcoastlines()
my_map.drawcountries()
#my_map.drawmapboundary()
my_map.fillcontinents(color = 'white', alpha = 0.3)
my_map.shadedrelief()

# To create a color map
colors = plt.get_cmap('jet')(np.linspace(0.0, 1.0, clusterNum))



#Visualization1
for clust_number in set(labels):
    c=(([0.4,0.4,0.4]) if clust_number == -1 else colors[np.int(clust_number)])
    clust_set = pdf[pdf.Clus_Db == clust_number]                    
    my_map.scatter(clust_set.xm, clust_set.ym, color =c,  marker='o', s= 20, alpha = 0.85)
    if clust_number != -1:
        cenx=np.mean(clust_set.xm) 
        ceny=np.mean(clust_set.ym) 
        plt.text(cenx,ceny,str(clust_number), fontsize=25, color='red',)
        print ("Cluster "+str(clust_number)+', Avg Temp: '+ str(np.mean(clust_set.Tm)))


# ## Want to learn more?
# 
# IBM SPSS Modeler is a comprehensive analytics platform that has many machine learning algorithms. It has been designed to bring predictive intelligence to decisions made by individuals, by groups, by systems – by your enterprise as a whole. A free trial is available through this course, available here: [SPSS Modeler](http://cocl.us/ML0101EN-SPSSModeler).
# 
# Also, you can use Watson Studio to run these notebooks faster with bigger datasets. Watson Studio is IBM's leading cloud solution for data scientists, built by data scientists. With Jupyter notebooks, RStudio, Apache Spark and popular libraries pre-packaged in the cloud, Watson Studio enables data scientists to collaborate on their projects without having to install anything. Join the fast-growing community of Watson Studio users today with a free account at [Watson Studio](https://cocl.us/ML0101EN_DSX)
# 
# ### Thanks for completing this lesson!
# 
# Notebook created by: <a href = "https://ca.linkedin.com/in/saeedaghabozorgi">Saeed Aghabozorgi</a>
# 
# <hr>
# Copyright &copy; 2018 [Cognitive Class](https://cocl.us/DX0108EN_CC). This notebook and its source code are released under the terms of the [MIT License](https://bigdatauniversity.com/mit-license/).​
