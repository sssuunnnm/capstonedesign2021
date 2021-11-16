import pandas as pd
import numpy as np
import scipy as sp
from sklearn.metrics.pairwise import cosine_similarity
import operator

furlist = pd.read_csv('test.csv')
rating = pd.read_csv('rating.csv')

furlist.head()

rating.rating.replace({-1: np.nan}, regex=True, inplace=True)
rating.head()
#rating data = nan
rating.groupby("rating").count().iloc[:,:1] / rating.count().user_id
furlist_1=furlist[furlist['type']=='square']
furlist_1.head()
merged = rating.merge(furlist_1,left_on = 'tag', right_on = 'tag',suffixes=['_user', ''])
merged.rename(columns = {'rating_user':'user_rating'}, inplace =True)
merged.head()

merged = merged[['user_id','name','user_rating']]
merged.head()

piv = merged.pivot_table(index=['user_id'], columns=['name'], values='user_rating')
print(piv.shape)
piv.head()

piv_norm = piv.apply(lambda x: (x-np.mean(x))/(np.max(x)-np.min(x)), axis=1)
piv_norm.fillna(0, inplace=True)
piv_norm = piv_norm.T
piv_norm = piv_norm.loc[:, (piv_norm != 0).any(axis=0)]
piv_sparse = sp.sparse.csr_matrix(piv_norm.values)

piv = merged.pivot_table(index=['user_id'], columns=['name'], values='user_rating')
print(piv.shape)
piv.head()


print("코사인유사도")
item_similarity = cosine_similarity(piv_sparse)
user_similarity = cosine_similarity(piv_sparse.T)
print("성공")

item_sim_df = pd.DataFrame(item_similarity, index = piv_norm.index, columns = piv_norm.index)
user_sim_df = pd.DataFrame(user_similarity, index = piv_norm.columns, columns = piv_norm.columns)

item_sim_df.head()
user_sim_df.head()

