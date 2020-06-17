import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#读取日数据
data_day = pd.read_csv('日数据.csv' , encoding='GBK')
print(data_day.head())

#各变量中缺失值的比例
r=data_day.isnull().sum(axis = 0)/data_day.shape[0]
r1=r[r>=0.37]
r.plot(kind='hist')
plt.xlabel('缺失值占比') 
plt.ylabel('变量个数')

#删除缺失值较多的列 
for i in range(len(r1)):
    data_day.drop(labels = r1.index[i], axis = 1, inplace=True)
    
#按股票编号分组，求出每股各变量的中位数，缺失值用0填充
id_grouped = data_day.groupby(['股票编号','年','月'])
data=pd.DataFrame(np.zeros((291144,40)))
for i in range(0,40):
    a=id_grouped.aggregate({data_day.columns[i]:np.median})
    a.index=range(291144)
    data.iloc[:,i]=a.values

data=data.fillna(0)

#查找缺失值的位置，用每股各变量的中位数填充
dot=np.where(np.isnan(data_day))
x=dot[0]
y=dot[1]
for i in range(len(x)):
    data_day.iloc[x[i],y[i]]=data.iloc[data.loc[data[0] == data_day.iloc[x[i],0]].loc[data[1] == data_day.iloc[x[i],1]].loc[data[2] == data_day.iloc[x[i],2]].index[0],y[i]]
    
data_day.to_csv('out.csv', mode='w', header=True, index=False, encoding='GBK')