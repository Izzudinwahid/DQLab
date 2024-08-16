from scipy import stats
import numpy as np
import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

#VISUALISASI DATA dengan PANDAS & MATPLOTLIB  
#=========================SCATTER
raw_data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/dataset_statistic.csv", sep=';')

# plt.clf()
# plt.figure()
# raw_data.plot.scatter(x='Pendapatan',y='Total')
# plt.title('plot.scatter dari pandas',size = 14)
# plt.tight_layout()
# plt.show()

# plt.scatter(x='Pendapatan',y='Total',data=raw_data)
# plt.title('plt.scatter dari matplotlib', size=14)
# plt.tight_layout()
# plt.show()

# plt.scatter(x='Pendapatan', y='Total',data=raw_data)
# plt.xlabel('Pendapatan')
# plt.ylabel('Total')
# plt.title('menggunakan matplotlib',size = 14)
# plt.tight_layout()
# plt.show()

#================HISTOGRAM
# plt.clf()
# # plt.figure()
# #with pandas
# raw_data.hist(column='Pendapatan')
# plt.title('HISTOGRAM dengan PANDAS',size=14)
# plt.tight_layout()
# plt.show()

# # plt.figure()
# plt.hist(x='Pendapatan',data=raw_data)
# plt.xlabel('Pendapatan')
# plt.title('HISTOGRAM dengan MATPLOTLIB',size=14)
# plt.tight_layout()
# plt.show()

#BOXPLOT
# plt.clf()
# plt.figure()
# raw_data.boxplot(column='Pendapatan')
# plt.title('.boxplot dari pandas',size=14)
# plt.tight_layout()
# plt.show()

# plt.clf()
# plt.figure()
# plt.boxplot(x='Pendapatan',data=raw_data)
# plt.xlabel('Pendapatan')
# plt.title('pyplot.boxplot dari matplotlib.pyplot',size = 14)
# plt.tight_layout()
# plt.show()

#BARPLOT
# class_freq = raw_data['Produk'].value_counts()

# plt.figure()
# class_freq.plot.bar()
# plt.title('.bar dari pandas',size=14)
# plt.tight_layout()
# plt.show()

# plt.figure()
# plt.bar(x=class_freq.index,height=class_freq.values)
# plt.title('plt.bar dari matplotlib.pyplot',size=14)
# plt.tight_layout()
# plt.show()


#PIECHART
# plt.clf()
# class_freq=raw_data['Produk'].value_counts()
# plt.pie(class_freq.values,labels=class_freq.index)
# plt.title('plt.pie dari matplotlib.pyplot', size=14)
# plt.tight_layout()
# plt.show()

# class_freq.plot.pie()
# plt.title('plot.pie dari pandas', size=14)
# plt.tight_layout()
# plt.show()


#===============TRANSFORMASI DATA
# plt.clf()
# plt.figure()
# raw_data.hist()
# plt.title('Histogram seluruh kolom', size=14)
# plt.tight_layout()
# plt.show()

# plt.figure()
# raw_data['Pendapatan'].hist()
# plt.title('Histogram pendapatan',size = 14)
# plt.tight_layout()
# plt.show()

# plt.figure()
# np.power(raw_data['Pendapatan'],1/5).hist()
# plt.title('Histogram pendapatan - transformasi menggunakan akar lima', size=14)
# plt.tight_layout()
# plt.show()    


# membuat qqplot pendapatan - transformasi menggunakan akar lima
# pendapatan_akar_lima = np.power(raw_data['Pendapatan'],1/5)
# plt.figure()
# stats.probplot(pendapatan_akar_lima,plot=plt)
# plt.title('qqplot pendapatan - transformasi menggunakan akar lima', size=14)
# plt.tight_layout()
# plt.show()

# plt.figure()
# stats.probplot(raw_data['Pendapatan'],plot=plt)
# plt.title('qqplot pendapatan', size=14)
# plt.tight_layout()
# plt.show()

#===============TRASNFORMASI BOX-COX
# plt.clf()
# hasil, _ = stats.boxcox(raw_data['Pendapatan'])

# #HISTOGRAM
# # plt.figure()
# plt.hist(hasil)
# plt.title('Histogram', size=14)
# plt.tight_layout()
# plt.show()

# #QQPLOT
# plt.figure()
# stats.probplot(hasil,plot=plt)
# plt.title('qqplot', size=14)
# plt.tight_layout()
# plt.show()


# #Transformasi kategori kedalam angka
# print(raw_data['Produk'])

# data_dummy_produk = pd.get_dummies(raw_data['Produk'])
# print(data_dummy_produk)

#QUIZ 2
# hasil1= np.power(raw_data['Pendapatan'],1/5)
# print(stats.skew(hasil1))

# hasil2, _=stats.boxcox(raw_data['Pendapatan'])
# print(stats.skew(hasil2))

## ==================MATRIKS KORELASI
# plt.clf()

# #mengatur ukuran gambar/plot
# plt.rcParams['figure.dpi'] = 100

# plt.figure()
# plt.matshow(raw_data.corr())
# plt.title('Plot correlation matriks dengan .matshow', size=14)
# plt.tight_layout()
# plt.show()

# plt.clf()
# sns.heatmap(raw_data.corr(),annot=True)
# plt.title('Plot correlation matriks dengan sns.heatmap', size=14)
# plt.tight_layout()
# plt.show()

# #==================GROUPED BOXPLOT
# plt.clf()

# # plt.figure()
# # # boxplot biasa tanpa pengelompokkan
# # raw_data.boxplot(rot=90)
# # plt.title('Boxplot tanpa pengelompokkan', size=14)
# # plt.tight_layout()
# # plt.show()

# plt.figure()
# # box plot dengan pengelompokkan dilakukan oleh kolom 'Produk'
# raw_data.boxplot(by='Produk')
# plt.tight_layout()
# plt.show()

# #===========GROUPED HISTOGRAM

# plt.figure()
# raw_data[raw_data['Produk'] == 'A'].hist()
# plt.tight_layout()
# plt.show()

# #=========HEX BIN PLOT

# plt.clf()
# plt.figure()
# raw_data.plot.hexbin(x = 'Pendapatan', y='Total',gridsize=25, rot = 90)
# plt.tight_layout()
# plt.show()

# #===========SCATTER MATRIX PLOT
# plt.clf()
# _, ax = plt.subplots(1,1,figsize = (10,10))
# scatter_matrix(raw_data, ax=ax)
# plt.show()

# #============mengubah diagonal dari scatter matrix menjadi density plot
# plt.clf()
# _, ax = plt.subplots(1,1,figsize = (10,10))
# scatter_matrix(raw_data,diagonal='kde',ax=ax)
# plt.show()

# #===================PENGENALAN PEMODELAN REGRESI LINIER
# nilai_Y = raw_data[['Total']]
# #variable bebas dengan intercept(X)
# nilai_X = sm.add_constant(raw_data[['Pendapatan']])
# # nilai_X = raw_data[['Pendapatan']]
# model_regresi = sm.OLS(endog = nilai_Y,exog = nilai_X).fit()
# print(model_regresi.summary())