##I collect data on how well the post reach after a week. 
##KThat helps in understanding how Instagram’s algorithm is working
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import sklearn 
import seaborn as sns
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator

##First lets read the dataset 

data = pd.read_csv('Instagram.csv',encoding='latin1')

# print(data.head(n=1).T)
# print("\n")
## Before starting, we should look at if there is null values in dataset

data.isnull().sum()

# ### Seems like there is one null row 

# data = data.dropna()
# ####Lets check again

# print(data.isnull().sum())
# # Now we can look at dataset
# print("\n")
# print(data.info())


# plt.figure(figsize=(10,8))
# plt.style.use('fivethirtyeight')
# plt.title('Impression distribution from Home')
# # sns.displot(data['From Home'])
# sns.histplot(data['From Home'],kde=True,stat='density')
# # plt.savefig('Impression distribution from Home')
# plt.show()