#日数据 输入：原来的日数据 输出：加好是否高转送标签以后的日数据，需要观察发生高转送股票的日数据的特点
import matplotlib.pyplot as plt
plt.bar(daily_null_col_ratio,height=1)
plt.title('daily_null_col_ratio')
daily_null_col_ratio.plot.barh(title='daily_null_col_ratio')
yearly_null_col_ratio.hist()
yearly_null_col_ratio.plot.barh(title='yearly_null_col_ratio')

reference_for_daily_data = yearly_data[['股票编号','年份（年末）','是否高转送']]
print(reference_for_daily_data)
#创造一列空的数据，用来判断日数据是否高送转
daily_data_if_gsz = pd.Series(np.zeros(daily_data.shape[0]),name='是否高送转')
#将这列数据并进日数据
daily_data = pd.concat([daily_data,daily_data_if_gsz],axis=1)
i=0#计数器
while i< reference_for_daily_data.shape[0]:
    #reference_for_daily_data[['股票编号','年份（年末）']][reference_for_daily_data['股票编号']==1]
    t = reference_for_daily_data[['股票编号','年份（年末）','是否高转送']].iloc[i,:]
    if t[2] == 0:
        pass
    else:
        #selected_cols = daily_data[['股票编号','年','是否高送转']][(daily_data['股票编号']==t[0]) & (daily_data['年']==t[1])]
        #daily_data[(daily_data['股票编号']==t[0]) & (daily_data['年']==t[1])]['是否高送转'] = 1 #[['股票编号','年','是否高送转']]
        target_indexs = daily_data[(daily_data['股票编号']==t[0]) & (daily_data['年']==t[1])]['是否高送转'].index
        daily_data.iloc[target_indexs,-1] = 1
    i += 1
daily_data['是否高送转'].sum()/daily_data.shape[0]
#验证是否加标签成功
daily_data[(daily_data['股票编号']==2) & (daily_data['年']==7)]['是否高送转']
daily_data[(daily_data['股票编号']==41) & (daily_data['年']==7)]['是否高送转']
#经验证，加标签成功
#输出加好标签的日数据
daily_data.to_csv('加好标签的日数据.csv', mode='w', header=True, index=False, encoding='GBK')
test_df = pd.DataFrame([1,2,3,4,5])
test_df.to_csv('test_df.csv')