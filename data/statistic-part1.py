import pandas as pd
import numpy as np


raw_data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/dataset_statistic.csv",sep=';')

# PANDAS
# print(raw_data.describe())
# print(raw_data.max())
# print(raw_data['Harga'].max())
# print(raw_data['Harga'].min())
# print(raw_data.sum())
# print(raw_data.sum(numeric_only=True))
# print(raw_data[['Harga', 'Pendapatan']].sum())
# print(raw_data[3:5])
# print(raw_data.loc[[1,3,5]])
# print(raw_data[['Jenis Kelamin','Pendapatan']].loc[[1,3,5]])


#NUMPY #quantile #mean #median
# produk_A = raw_data[raw_data['Produk'] == 'A']
# print(produk_A['Pendapatan'].mean())
# print(np.mean(produk_A['Pendapatan']))
# print(produk_A['Pendapatan'].median())
# print(np.median(produk_A['Pendapatan']))
# print(raw_data['Produk'].value_counts())#banyak data yang muncul
# print(raw_data['Pendapatan'].quantile(q = 0.5))
# print(np.quantile(raw_data['Pendapatan'] ,q=0.5))
# print(raw_data[['Pendapatan','Harga']].agg([np.mean,np.median]))
# print(raw_data[['Pendapatan','Harga','Produk']].groupby('Produk').agg([np.mean,np.median]))

# print(raw_data['Produk'].value_counts()/raw_data.shape[0]) #proporsi kategori
# print(raw_data['Pendapatan'].max()-raw_data['Pendapatan'].min())#rentang

#variansi with np and pd
# print(raw_data['Pendapatan'].var())
# print(raw_data['Pendapatan'].var(ddof=0))
# print(np.var(raw_data['Pendapatan']))

#deviasi
# print(raw_data['Pendapatan'].std())
# print(np.std(raw_data['Pendapatan'],ddof=1))

#korelasi
# print(raw_data.corr())
# print(raw_data.corr(method='kendall'))
# print(raw_data.corr(method='spearman'))