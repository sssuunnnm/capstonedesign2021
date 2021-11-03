import pandas as pd
import numpy as np
import scipy as sp
from sklearn.metrics.pairwise import cosine_similarity
import operator #%matplotlib inline

furlist = pd.read_csv('furlist.csv')
rating = pd.read_csv('rating.csv')
furlist.head()
rating.rating.replace({-1: np.nan}, regex=True, inplace=True)
rating.head()

rating.groupby("rating").count().iloc[:,:1] / rating.count().user_id

#fur_user = furlist[furlist['type']==]

# 이 중간에 많은 과정이 생략되어있음..

