#给每列加上上一年的同样的自变量(共251个) (因变量) 时序因子的加入 输入上一步处理后的年数据 输出加上时序特征以后的年数据
yearly_data = pd.read_csv('/kaggle/input/teddycup55/final_data_1.csv',encoding='GBK')
#drop掉三列日期
yearly_data.drop(columns=['高转送预案公告日','高转送股权登记日','高转送除权日'],inplace=True)
yearly_data.info()
#创建一个新建列名的列表，即都是含有（上一年）的list
new_variables_list = []
for x_column in x_columns2:
    new_variables_list.append(str(x_column+'(上一年)'))
   
#初始化新加的变量
for new_variable in new_variables_list:
    yearly_data[new_variable] = 0.0

yearly_data.shape #251-3+251-3+1 = 497
#开始填上一年的数据
for i in range(len(yearly_data)):
    t_year = yearly_data.iloc[i,:]['年份（年末）']
    t_stock = yearly_data.iloc[i,:]['股票编号']
    if len(yearly_data[(yearly_data['年份（年末）']==t_year-1) & (yearly_data['股票编号']==t_stock)]) == 0:
        pass
    else:
        index_current = (yearly_data[new_variables_list][(yearly_data['年份（年末）']==t_year) & (yearly_data['股票编号']==t_stock)].index)[0]
        #yearly_data[new_variables_list][(yearly_data['年份（年末）']==t_year) & (yearly_data['股票编号']==t_stock)] = yearly_data[x_columns][(yearly_data['年份（年末）']==t_year-1) & (yearly_data['股票编号']==t_stock)]
        yearly_data.iloc[index_current,249:] = list(yearly_data.iloc[index_current-1,:248])
#删除每组序列数据的第一个
stock_can = yearly_data['股票编号'].drop_duplicates()
wanted_delete_index_can = []
for i in list(stock_can):
    t = yearly_data[(yearly_data['股票编号']==i)].iloc[0,:].name
    wanted_delete_index_can.append(t)
yearly_data.drop(index=wanted_delete_index_can,inplace=True)
yearly_data.to_csv('final_data_1_5-5(2).csv', mode='w', header=True, index=False, encoding='GBK')
#给7th_year的数据加上前一年的时间序列特征
yearly_data1 = pd.read_csv('/kaggle/input/teddycup55/final_data_1.csv',encoding='GBK')
yearly_data2 = pd.read_csv('/kaggle/input/teddycup55/final_data_1_7thyear.csv',encoding='GBK')
#drop掉三列日期
yearly_data1.drop(columns=['高转送预案公告日','高转送股权登记日','高转送除权日'],inplace=True)
yearly_data2.drop(columns=['高转送预案公告日','高转送股权登记日','高转送除权日'],inplace=True)
#创建一个新建列名的列表，即都是含有（上一年）的list
new_variables_list = []
for x_column in x_columns2:
    new_variables_list.append(str(x_column+'(上一年)'))
   
#初始化新加的变量
for new_variable in new_variables_list:
    yearly_data2[new_variable] = 0.0

yearly_data2.shape #251-3+251-3+1 = 497 #497-1=496 减去那个因变量
#开始填上一年的数据
for i in range(len(yearly_data2)):
    t_stock_id = yearly_data2.iloc[i,0]
    yearly_data2.iloc[i,248:] = (yearly_data1[(yearly_data1['股票编号']==t_stock_id) & (yearly_data1['年份（年末）']==6)].drop(columns=['第二年是否高转送'])).values.reshape(-1,)
yearly_data2.to_csv('final_data_1_5-5_7thyear(2).csv', mode='w', header=True, index=False, encoding='GBK')
