#将基础数据的特征根据不同行业和是否是次新股，并到年数据里面去 输入年数据，基础数据，输出加好基础数据标签的年数据
#收集次新股的股票编号
ci_xin_gu_can = [] #只是股票的编号，不是索引编号
i = 0
while i<len(fun_data['所属概念板块']):
    try:
        string = fun_data['所属概念板块'][i]
        t = string.find('次新股')
        if t!=-1:
            ci_xin_gu_can.append(i+1)
    except:
        pass
    i += 1

#给年数据添加一列专门用来描述是不是次新股
yearly_data['是否次新股'] = 0

for one_ci_xin_gu in  ci_xin_gu_can:
    yearly_data['是否次新股'][(yearly_data['股票编号']==one_ci_xin_gu)] = 1
#(2)把行业这个独热变量加到年数据里面去
#找出一共有多少种行业，然后
all_professions = list(fun_data['所属行业'].drop_duplicates())
for one_profession in all_professions:
    yearly_data[str(one_profession)] = 0
i = 0 #计数器而已
while i < len(fun_data):
    stock_id,profession = fun_data.iloc[i,[0,2]]
    yearly_data[profession][(yearly_data['股票编号']==stock_id)] = 1
    i += 1
list(yearly_data.columns)
yearly_data.to_csv('加上日数据和基础数据信息的年数据.csv', mode='w', header=True, index=False, encoding='GBK')