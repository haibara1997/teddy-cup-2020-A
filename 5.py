#计算日数据几列变量一年期间的均值、方差、极差、峰度，并将这些特征根据股票编号和年份并到年数据里面去
#输入年数据，日数据，输出加好日数据的特征的年数据
#给年数据添加几个特征，并全都初始化为0
yearly_data['收盘价均值'] = 0.0
yearly_data['收盘价极差'] = 0.0
yearly_data['收盘价方差'] = 0.0
yearly_data['收盘价峰度'] = 0.0
yearly_data['成交量均值'] = 0.0
yearly_data['成交量极差'] = 0.0
yearly_data['成交量方差'] = 0.0
yearly_data['成交量峰度'] = 0.0
yearly_data['成交金额均值'] = 0.0
yearly_data['成交金额极差'] = 0.0
yearly_data['成交金额方差'] = 0.0
yearly_data['成交金额峰度'] = 0.0
#日数据的特征提取出来，并到年数据上面去
stock_id_cans = range(1,3467) #[1,2,...,3466]
year_id_cans = range(1,8) #[1,2,3,4,5,6,7]

#按照规定的股票编号和规定的年份提取出了我要的一组数据
for i in stock_id_cans:
    for j in year_id_cans:
        if len(yearly_data[(yearly_data['股票编号']==i) & (yearly_data['年份（年末）']==j)]) == 0:
            pass
        else:
            a_series_data = partial_daily_data[(partial_daily_data['股票编号']==i) & (partial_daily_data['年']==j)]

            yearly_data['收盘价均值'][(yearly_data['股票编号']==i) & (yearly_data['年份（年末）']==j)] = a_series_data['收盘价'].mean()
            yearly_data['收盘价极差'][(yearly_data['股票编号']==i) & (yearly_data['年份（年末）']==j)] = max(a_series_data['收盘价']) - min(a_series_data['收盘价'])
            yearly_data['收盘价方差'][(yearly_data['股票编号']==i) & (yearly_data['年份（年末）']==j)] = a_series_data['收盘价'].var()
            yearly_data['收盘价峰度'][(yearly_data['股票编号']==i) & (yearly_data['年份（年末）']==j)] = a_series_data['收盘价'].kurt()

            yearly_data['成交量均值'][(yearly_data['股票编号']==i) & (yearly_data['年份（年末）']==j)] = a_series_data['成交量'].mean()
            yearly_data['成交量极差'][(yearly_data['股票编号']==i) & (yearly_data['年份（年末）']==j)] = max(a_series_data['成交量']) - min(a_series_data['成交量'])
            yearly_data['成交量方差'][(yearly_data['股票编号']==i) & (yearly_data['年份（年末）']==j)] = a_series_data['成交量'].var()
            yearly_data['成交量峰度'][(yearly_data['股票编号']==i) & (yearly_data['年份（年末）']==j)] = a_series_data['成交量'].kurt()

            yearly_data['成交金额均值'][(yearly_data['股票编号']==i) & (yearly_data['年份（年末）']==j)] = a_series_data['成交金额'].mean()
            yearly_data['成交金额极差'][(yearly_data['股票编号']==i) & (yearly_data['年份（年末）']==j)] = max(a_series_data['成交金额']) - min(a_series_data['成交金额'])
            yearly_data['成交金额方差'][(yearly_data['股票编号']==i) & (yearly_data['年份（年末）']==j)] = a_series_data['成交金额'].var()
            yearly_data['成交金额峰度'][(yearly_data['股票编号']==i) & (yearly_data['年份（年末）']==j)] = a_series_data['成交金额'].kurt()
        
        #shou_pan_jia_the_mean = a_series_data['收盘价'].mean()
        #yearly_data[(yearly_data['股票编号']==1) & (yearly_data['年份（年末）']==1)] #['收盘价的均值']
        
        #t = yearly_data.copy()
        #t[(t['股票编号']==1) & (t['年份（年末）']==1)]['收盘价均值'] = 14.45
        #t['收盘价均值'] = 0
        #t.shape