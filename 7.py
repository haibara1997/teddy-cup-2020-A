#用前一年的数据预测下一年是否发生转送，即把年数据错位一下 输入年数据 输出处理后的年数据，以及第七年的数据
a_list = []
stock_can = list(yearly_data['股票编号'].drop_duplicates())
x = pd.DataFrame(None,columns = x_columns)
y = pd.Series(None,name='是否高转送')
x_seventh_year = pd.DataFrame(None,columns = x_columns)


for i in stock_can:
    #yearly_data[yearly_data['股票编号']==i]
    if len(yearly_data[yearly_data['股票编号']==i]) == 1:
        pass
    else:
        t_all = yearly_data[yearly_data['股票编号']==i] #temp_all
        t_x = t_all.drop(columns='是否高转送') #temp_all_x #t_x.iloc[-1,:] #x_seventh_year
        
        x_seventh_year = x_seventh_year.append(t_x.iloc[-1,:])

        t_x = t_x.iloc[:-1,:]
        t_y = t_all['是否高转送'][1:]
        x = pd.concat([x,t_x], ignore_index=True) #必须索引了，因为数据错位了，否则没法对齐
        y = pd.concat([y,t_y], ignore_index=True)
        
        #yearly_data[yearly_data['股票编号']==4]['是否高转送']
final_data = pd.concat([x,y],axis=1)
final_data.rename(columns={'是否高转送':'第二年是否高转送'},inplace=True)
final_data
final_data.to_csv('final_data_3.csv', mode='w', header=True, index=False, encoding='GBK')
x_seventh_year.to_csv('final_data_3_7thyear.csv', mode='w', header=True, index=False, encoding='GBK')
