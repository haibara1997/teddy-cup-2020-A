#用保存的模型进行预测 输入第七年的数据 输出第八年预测那些股票可能发生高转送
#加载模型
model = joblib.load('/kaggle/input/11111111111111111111111/teddycup_clf.pkl')
can=[
'收盘价均值(上一年)',
'每股送转',
'基本每股收益',
'基本每股收益同必增长(%)' ,
'投资活动产生的现金流量净额占必(%)', #不在
'总资产相对年初增长(%)' , #不在
'经营活动产生的现金流量净额占必(%)(上一年)',
'股权自由现金流量' ,#不在
'每股盈余公积(元/股)(上一年)' ,
'收盘价峰度' , #不在
'实收资本(或股本)' ,
'实收资本(或股本)(上一年)' ,
'每股净资产相对年初增长(%)' ,#不在
'净资产相对年初增长(%)(上一年)' , #不在
'经营活动现金流量净额/净债务' , #不在
'收盘价峰度(上一年)',
'是否次新股',
'稀释每股收益',
'每股净资产(元/股)',
'每股资本公积(元/股)',
'每股未分配利润(元/股)',
'每股未分配利润(元/股)(上一年)',
'每股净资产(元/股)',
'每股营业收入(元/股)'
]
can.append('第二年是否高转送')
my_data = pd.DataFrame([X_train,y_train],) 
del can[-1]
#验证模型是否可用
y_train_predicted = model.predict(X_train[can])
y_test_predicted = model.predict(X_test[can])
print(classification_report(y_train,y_train_predicted,target_names=['0','1']))
print(classification_report(y_test,y_test_predicted,target_names=['0','1']))
#预测第八年
test_8th_year = pd.read_csv('/kaggle/input/teddy-cup-5-6-afternoon1/加了时序以后可以直接用的数据-5-6上午/未标准化版/3_7th_未标准化.csv',encoding='GBK')
year_8_predicted = model.predict(test_8th_year[can])
predict_8th = pd.DataFrame([test_8th_year['股票编号'],year_8_predicted],index=['股票编号','是否发生了高转送'])
predict_8th = predict_8th.T
result = predict_8th['股票编号'][predict_8th['是否发生了高转送']==1]
result.to_csv('第8年预测会发生高转送的股票.csv',mode='w', header=True, index=False, encoding='GBK')