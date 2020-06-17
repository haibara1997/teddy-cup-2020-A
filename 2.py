import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#读取年数据
data_year = pd.read_csv('年数据.csv' , encoding='GBK')
print(data_year.head())

#删除未上市年份的整行数据
data_year=data_year.dropna(thresh=4)
data_year.index=range(22552)

#删除方差为零的整列数据
data_year.drop(labels = '会计区间', axis = 1, inplace=True)
data_year.drop(labels = '合并标志，1-合并，2-母公司', axis = 1, inplace=True)
data_year.drop(labels = '会计准则', axis = 1, inplace=True)
data_year.drop(labels = '货币代码', axis = 1, inplace=True)

df = data_year.iloc[:,0:353]
#各变量中缺失值的比例
r=df.isnull().sum(axis = 0)/df.shape[0]
r1=r[r>=0.2]

r.plot(kind='hist')
plt.xlabel('缺失值占比') 
plt.ylabel('变量个数') 

#删除缺失值较多的列 
for i in range(len(r1)):
    df.drop(labels = r1.index[i], axis = 1, inplace=True)

#按股票编号分组，求出每股各变量的中位数
id_grouped = df.groupby(['股票编号'])
med=pd.DataFrame(np.zeros((3466,216)))
for i in range(216):
    a=id_grouped.aggregate({df.columns[i]:np.median})
    med.iloc[:,i]=id_grouped.aggregate({df.columns[i]:np.median})
    a.index=range(3466)
    med.iloc[:,i]=a.values

med1=med.dropna()

med0=med.replace(to_replace=0,value = np.nan)
med2=data0.dropna()

med=med.fillna(0)

#查找缺失值的位置，用每股各变量的中位数填充
dot=np.where(np.isnan(df))
x=dot[0]
y=dot[1]
for i in range(len(x)):
    df.iloc[x[i],y[i]]=med.iloc[df.iloc[x[i],0]-1,y[i]]
    
data_year.iloc[:,0:216]=df
data_year.drop(data_year.iloc[:,216:353].columns, axis = 1, inplace=True)
data_year.to_csv('out.csv', mode='w', header=True, index=False, encoding='GBK') 

list1=[]
for i in med1[0]:
    list1.extend(df.loc[year['股票编号']==i].index.tolist())

data_year1=data_year.loc[list1,:]
data_year1.to_csv('out1.csv', mode='w', header=True, index=False, encoding='GBK')

list2=[]
for i in med2[0]:
    list2.extend(df.loc[year['股票编号']==i].index.tolist())

data_year2=data_year.loc[list2,:]
data_year2.to_csv('out2.csv', mode='w', header=True, index=False, encoding='GBK')

 








