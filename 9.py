#标准化 输入上一步得到的数据 输出标准化以后的数据
#用0来填每股送转的两列nan(每股送转、 每股送转(上一年) )
file_list = [final_data_1_7thyear,final_data_2_7thyear,final_data_3_7thyear,final_data_1,final_data_2,final_data_3]
for file in files_list:
    drop_columns1 = list(file.iloc[:,[248,249]].columns) #股票编号(上一年) 年份(年末)(上一年)
    drop_columns2 = list(file.iloc[:,-19:].columns) #是否是次新股(上一年) 房地产业(上一年) 制造业(上一年) ...... 教育(上一年)
    file.fillna(0,inplace=True)
final_data_1_7thyear.iloc[:,-19:]
#drop掉多余的几列
files_list_7th = [final_data_1_7thyear,final_data_2_7thyear,final_data_3_7thyear]
files_list     = [final_data_1,final_data_2,final_data_3]
#drop掉7th的数据
final_data_3_7thyear.iloc[:,[248,249]] #股票编号(上一年) 年份（年末）(上一年)
final_data_3_7thyear.iloc[:,-19:] #是否是次新股(上一年) 房地产业(上一年) 制造业(上一年) ...... 教育(上一年)
for file in files_list_7th:
    drop_columns1 = list(file.iloc[:,[248,249]].columns) #股票编号(上一年) 年份(年末)(上一年)
    drop_columns2 = list(file.iloc[:,-19:].columns) #是否是次新股(上一年) 房地产业(上一年) 制造业(上一年) ...... 教育(上一年)
    file.drop(columns=drop_columns1+drop_columns2,inplace=True)
#再drop掉剩下的数据
final_data_3.iloc[:,[249,250]] #股票编号(上一年) 年份（年末）(上一年)
final_data_3.iloc[:,-19:]
for file in files_list:
    drop_columns1 = list(file.iloc[:,[249,250]].columns) #股票编号(上一年) 年份(年末)(上一年)
    drop_columns2 = list(file.iloc[:,-19:].columns) #是否是次新股(上一年) 房地产业(上一年) 制造业(上一年) ...... 教育(上一年)
    file.drop(columns=drop_columns1+drop_columns2,inplace=True)
final_data_1_7thyear.to_csv('1_7th_未标准化.csv', mode='w', header=True, index=False, encoding='GBK')
final_data_2_7thyear.to_csv('2_7th_未标准化.csv', mode='w', header=True, index=False, encoding='GBK')
final_data_3_7thyear.to_csv('3_7th_未标准化.csv', mode='w', header=True, index=False, encoding='GBK')
final_data_1.to_csv('1_未标准化.csv', mode='w', header=True, index=False, encoding='GBK')
final_data_2.to_csv('2_未标准化.csv', mode='w', header=True, index=False, encoding='GBK')
final_data_3.to_csv('3_未标准化.csv', mode='w', header=True, index=False, encoding='GBK')
#标准化
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
files_list_7th = [final_data_1_7thyear,final_data_2_7thyear,final_data_3_7thyear]
files_list     = [final_data_1,final_data_2,final_data_3]
#先标准化前六年的data
for file in files_list:
    std1 = StandardScaler()
    file.iloc[:,2:229] = std1.fit_transform(file.iloc[:,2:229])
    std2 = StandardScaler()
    file.iloc[:,249:] = std2.fit_transform(file.iloc[:,249:])
#标准化第七年的data
for file in files_list_7th:
    std1 = StandardScaler()
    file.iloc[:,2:229] = std1.fit_transform(file.iloc[:,2:229])
    std2 = StandardScaler()
    file.iloc[:,248:] = std2.fit_transform(file.iloc[:,248:])

final_data_1_7thyear.to_csv('1_7th_标准化.csv', mode='w', header=True, index=False, encoding='GBK')
final_data_2_7thyear.to_csv('2_7th_标准化.csv', mode='w', header=True, index=False, encoding='GBK')
final_data_3_7thyear.to_csv('3_7th_标准化.csv', mode='w', header=True, index=False, encoding='GBK')
final_data_1.to_csv('1_标准化.csv', mode='w', header=True, index=False, encoding='GBK')
final_data_2.to_csv('2_标准化.csv', mode='w', header=True, index=False, encoding='GBK')
final_data_3.to_csv('3_标准化.csv', mode='w', header=True, index=False, encoding='GBK')