#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# # Load Dataset

# In[2]:


import pandas as pd
import numpy as np
df=pd.read_csv("C:\\Users\\sruthi.m\\Downloads\\Mall_Customers.csv")
df.head()


# # Univariate Analysis Visualization

# In[3]:


import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


plt.plot(df['Spending Score (1-100)'])
plt.show()


# In[5]:


plt.hist(df['Spending Score (1-100)'])


# In[6]:


data=np.array(df['Spending Score (1-100)'])
plt.plot(data,linestyle = 'dotted')


# In[7]:


sns.boxplot(df['Spending Score (1-100)'])


# In[8]:


sns.countplot(df['Spending Score (1-100)'])


# In[11]:


sns.countplot(df['Gender'])


# In[12]:


df['Spending Score (1-100)'].plot(kind='density')


# # Bivariate Analysis Visualization

# In[13]:


sns.stripplot(x=df['Annual Income (k$)'],y=df['Spending Score (1-100)'])


# In[14]:


lt.xlabel("Spending Score (1-100)")
plt.ylabel("Age")plt.scatter(df['Spending Score (1-100)'],df['Age'],color='blue')
p


# In[15]:


sns.stripplot(x=df['Spending Score (1-100)'],y=df['Age'])


# In[16]:


sns.violinplot(x ='Annual Income (k$)', y ='Spending Score (1-100)', data = df)


# # Multivariate Analysis Visualization

# In[17]:


sns.pairplot(df)


# In[18]:


sns.heatmap(df.corr(),annot=True)


# # Descriptive Statistics

# In[19]:


df.shape


# In[2]:


import pandas as pd
import numpy as np
df=pd.read_csv("C:\\Users\\sruthi.m\\Downloads\\Mall_Customers.csv")
df.head()
df.info()


# In[3]:


df.isnull().sum()


# In[4]:


df.describe()


# In[5]:


df.mean()


# In[6]:


df['Age'].mean()


# In[7]:


df.mode()


# In[8]:


df.median()


# In[10]:


df['Gender'].value_counts()


# # Handle Missing Values

# In[3]:


import pandas as pd
import numpy as np
df=pd.read_csv("C:\\Users\\sruthi.m\\Downloads\\Mall_Customers.csv")
df.head()
df.isna().sum()


# # Handling Outliers

# In[5]:


import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
sns.boxplot(df['Spending Score (1-100)'])


# In[6]:


Q1 = df['Spending Score (1-100)'].quantile(0.25)
Q3 = df['Spending Score (1-100)'].quantile(0.75)
IQR = Q3 - Q1
whisker_width = 1.5
lower_whisker = Q1 -(whisker_width*IQR)
upper_whisker = Q3 +(whisker_width*IQR)
df['Spending Score (1-100)']=np.where(df['Spending Score (1-100)']>upper_whisker,upper_whisker,np.where(df['Spending Score (1-100)']<lower_whisker,lower_whisker,df['Spending Score (1-100)']))
sns.boxplot(df['Spending Score (1-100)'])


# # Categorical Variable and Encoding

# In[7]:


numeric_data = df.select_dtypes(include=[np.number]) 
categorical_data = df.select_dtypes(exclude=[np.number]) 
print("Number of numerical variables: ", numeric_data.shape[1]) 
print("Number of categorical variables: ", categorical_data.shape[1])


# In[8]:


print("Number of categorical variables: ", categorical_data.shape[1]) 
Categorical_variables = list(categorical_data.columns)
Categorical_variables


# In[10]:


df['Gender'].value_counts()


# In[7]:


import pandas as pd
import numpy as np
df=pd.read_csv("C:\\Users\\sruthi.m\\Downloads\\Mall_Customers.csv")
df.head()
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
label = le.fit_transform(df['Gender'])
df["Gender"] = label


# In[9]:


df['Gender'].value_counts()


# In[10]:


df.head()


# # Independent and Dependent Variables

# In[12]:


X = df.drop("Spending Score (1-100)",axis=1)
Y = df['Spending Score (1-100)']


# In[13]:


X[:5]


# In[14]:


Y[:5]


# # Scale Independent Variables

# In[17]:


X


# In[18]:


from sklearn.preprocessing import StandardScaler
object= StandardScaler()
scale = object.fit_transform(X) 
print(scale)


# In[19]:


X_scaled=pd.DataFrame(scale,columns=X.columns)
X_scaled


# # KMeans Clustering Algorithm
# 

# # Train and Test Split

# In[20]:


from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans

# split the dataset
X_train, X_test, Y_train, Y_test = train_test_split(X_scaled, Y, test_size=0.20, random_state=0)
X_train.shape


# In[21]:


X_test.shape


# In[22]:


Y_train.shape


# In[23]:


Y_test.shape


# #  Build the Model

# In[24]:


x = df.iloc[:,[3,4]].values


# In[25]:


#training the K-means model on a dataset  
kmeans = KMeans(n_clusters=5, init='k-means++', random_state= 42)  
y_predict= kmeans.fit_predict(x)


# In[28]:



#visulaizing the clusters 
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
plt.scatter(x[y_predict == 0, 0], x[y_predict == 0, 1], s = 100, c = 'teal', label = 'Cluster 1') #for first cluster  
plt.scatter(x[y_predict == 1, 0], x[y_predict == 1, 1], s = 100, c = 'orange', label = 'Cluster 2') #for second cluster  
plt.scatter(x[y_predict== 2, 0], x[y_predict == 2, 1], s = 100, c = 'turquoise', label = 'Cluster 3') #for third cluster  
plt.scatter(x[y_predict == 3, 0], x[y_predict == 3, 1], s = 100, c = 'cyan', label = 'Cluster 4') #for fourth cluster  
plt.scatter(x[y_predict == 4, 0], x[y_predict == 4, 1], s = 100, c = 'indigo', label = 'Cluster 5') #for fifth cluster  
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroid')   
plt.title('Clusters of customers')  
plt.xlabel('Annual Income (k$)')  
plt.ylabel('Spending Score (1-100)')  
plt.legend()  
plt.show()


# In[ ]:



