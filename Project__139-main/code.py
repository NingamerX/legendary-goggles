!pip install kaggle


from google.colab import files
files.upload()

!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/

!chmod 600 ~/.kaggle/kaggle.json

!kaggle datasets download -d gspmoreira/articles-sharing-reading-from-cit-deskdrop

!ls

!unzip articles-sharing-reading-from-cit-deskdrop.zip

!ls

import pandas as pd 
import numpy as np 

df1=pd.read_csv('shared_articles.csv')
df2=pd.read_csv('users_interactions.csv')


df1.head()

df2.head()



df1 = df1[df1['eventType'] == 'CONTENT SHARED']
df1.head()

df2.shape

df1.shape

df1 = df1.sort_values(['total_events'], ascending=[False])

df1.head()

#This code doesn't work in visual code studio it's meant for google colab but I wanted to write it in visual code