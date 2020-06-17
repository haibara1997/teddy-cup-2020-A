#建模    输入：标准化以后的数据 输出：最终模型
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression
from catboost import CatBoostClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from xgboost.sklearn import XGBClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.externals import joblib
can = [
'收盘价均值(上一年)','每股送转','基本每股收益','基本每股收益同必增长(%)',
'投资活动产生的现金流量净额占必(%)','总资产相对年初增长(%)',
'经营活动产生的现金流量净额占必(%)(上一年)','股权自由现金流量','每股盈余公积(元/股)(上一年)',
'收盘价峰度','实收资本(或股本)','每股净资产相对年初增长(%)','净资产相对年初增长(%)(上一年)',
'经营活动现金流量净额/净债务','收盘价峰度(上一年)','是否次新股','第二年是否高转送']
can.append('第二年是否高转送')
data1 = pd.read_csv('/kaggle/input/teddy-cup-5-6-afternoon1/加了时序以后可以直接用的数据-5-6上午/标准化版/3_标准化.csv',encoding='GBK')
data1 = data1[can]
x = data1.drop(columns=['第二年是否高转送'])
y = data1['第二年是否高转送']
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=391)
#随机森林
rnd_clf = RandomForestClassifier(bootstrap=True, ccp_alpha=0.0,
                       class_weight={0: 0.5896246764452114,
                                     1: 3.289410348977136},
                       criterion='gini', max_depth=5, max_features='auto',
                       max_leaf_nodes=8, max_samples=None,
                       min_impurity_decrease=0.0, min_impurity_split=None,
                       min_samples_leaf=1, min_samples_split=2,
                       min_weight_fraction_leaf=0.0, n_estimators=446,
                       n_jobs=None, oob_score=False, random_state=None,
                       verbose=0, warm_start=False)
rnd_clf.fit(X_train,y_train)

y_predicted = rnd_clf.predict(X_train)
print(classification_report(y_train,y_predicted,target_names=['0','1']))

y_predicted = rnd_clf.predict(X_test)
print(classification_report(y_test,y_predicted,target_names=['0','1']))
#逻辑回归
log_reg = LogisticRegression(class_weight='balanced',max_iter=10000)
log_reg.fit(X_train,y_train)
y_predicted = log_reg.predict(X_train)
print(classification_report(y_train,y_predicted,target_names=['0','1']))
y_predicted = log_reg.predict(X_test)
print(classification_report(y_test,y_predicted,target_names=['0','1']))
#catboost
# Initialize data
#cat_features = [0,1,2]
#train_data = [["a","b",1,4,5,6],["a","b",4,5,6,7],["c","d",30,40,50,60]]
#train_labels = [1,1,-1]
#test_data = [["a","b",2,4,6,8],["a","d",1,4,50,60]]
# Initialize CatBoostClassifier
model = CatBoostClassifier(
iterations=3000, 
learning_rate=0.1, 
depth=4, loss_function='Logloss',class_weights=[1,5])
# Fit model
model.fit(X_train, y_train)
y_predicted = model.predict(X_train)
print(classification_report(y_train,y_predicted,target_names=['0','1']))
y_predicted = model.predict(X_test)
print(classification_report(y_test,y_predicted,target_names=['0','1']))
#xgboost
clf = XGBClassifier(
silent=0 ,#设置成1则没有运行信息输出，最好是设置为0.是否在运行升级时打印消息。
#nthread=4,# cpu 线程数 默认最大
learning_rate= 0.3, # 如同学习率
min_child_weight=1, 
# 这个参数默认是 1，是每个叶子里面 h 的和至少是多少，对正负样本不均衡时的 0-1 分类而言
#，假设 h 在 0.01 附近，min_child_weight 为 1 意味着叶子节点中最少需要包含 100 个样本。
#这个参数非常影响结果，控制叶子节点中二阶导的和的最小值，该参数值越小，越容易 overfitting。
max_depth=5, # 构建树的深度，越大越容易过拟合
gamma=0,  # 树的叶子节点上作进一步分区所需的最小损失减少,越大越保守，一般0.1、0.2这样子。
subsample=1, # 随机采样训练样本 训练实例的子采样比
max_delta_step=1,#最大增量步长，我们允许每个树的权重估计。
colsample_bytree=1, # 生成树时进行的列采样 
reg_lambda=1,  # 控制模型复杂度的权重值的L2正则化项参数，参数越大，模型越不容易过拟合。
#reg_alpha=0, # L1 正则项参数
#scale_pos_weight=1, #如果取值大于0的话，在类别样本不平衡的情况下有助于快速收敛。平衡正负权重
objective= 'binary:logistic', #多分类的问题 指定学习任务和相应的学习目标
#num_class=10, # 类别数，多分类与 multisoftmax 并用
n_estimators=220, #树的个数
seed=1000, #随机种子
eval_metric= 'auc',
scale_pos_weight=8868/1597
 )

clf.fit(X_train,y_train,eval_metric='auc')
y_predicted = clf.predict(X_train)
print(classification_report(y_train,y_predicted,target_names=['0','1']))
y_predicted = clf.predict(X_test)
print(classification_report(y_test,y_predicted,target_names=['0','1']))
#集成学习
rnd_clf = RandomForestClassifier(bootstrap=True, ccp_alpha=0.0,
                       class_weight={0: 0.5896246764452114,
                                     1: 3.289410348977136},
                       criterion='gini', max_depth=5, max_features='auto',
                       max_leaf_nodes=8, max_samples=None,
                       min_impurity_decrease=0.0, min_impurity_split=None,
                       min_samples_leaf=1, min_samples_split=2,
                       min_weight_fraction_leaf=0.0, n_estimators=446,
                       n_jobs=None, oob_score=False, random_state=None,
                       verbose=0, warm_start=False)

clf = XGBClassifier(
silent=0 ,#设置成1则没有运行信息输出，最好是设置为0.是否在运行升级时打印消息。
#nthread=4,# cpu 线程数 默认最大
learning_rate= 0.3, # 如同学习率
min_child_weight=1, 
# 这个参数默认是 1，是每个叶子里面 h 的和至少是多少，对正负样本不均衡时的 0-1 分类而言
#，假设 h 在 0.01 附近，min_child_weight 为 1 意味着叶子节点中最少需要包含 100 个样本。
#这个参数非常影响结果，控制叶子节点中二阶导的和的最小值，该参数值越小，越容易 overfitting。
max_depth=5, # 构建树的深度，越大越容易过拟合
gamma=0,  # 树的叶子节点上作进一步分区所需的最小损失减少,越大越保守，一般0.1、0.2这样子。
subsample=1, # 随机采样训练样本 训练实例的子采样比
max_delta_step=1,#最大增量步长，我们允许每个树的权重估计。
colsample_bytree=1, # 生成树时进行的列采样 
reg_lambda=1,  # 控制模型复杂度的权重值的L2正则化项参数，参数越大，模型越不容易过拟合。
#reg_alpha=0, # L1 正则项参数
#scale_pos_weight=1, #如果取值大于0的话，在类别样本不平衡的情况下有助于快速收敛。平衡正负权重
objective= 'binary:logistic', #多分类的问题 指定学习任务和相应的学习目标
#num_class=10, # 类别数，多分类与 multisoftmax 并用
n_estimators=220, #树的个数
seed=1000, #随机种子
eval_metric= 'auc',
scale_pos_weight=8868/1597
 )

model = CatBoostClassifier(
iterations=3000, 
learning_rate=0.1, 
depth=4, loss_function='Logloss',class_weights=[1,5])

log_reg = LogisticRegression(class_weight='balanced',max_iter=10000)
# Fit model
model.fit(X_train, y_train)
voting_clf = VotingClassifier(estimators=[('rnd_clf',rnd_clf),('xgclf',clf),('catboost',model),('log_reg',log_reg)],voting='soft',weights=[2,5,2,1])  #rf recall高#,weights=[2,5,3,1.5]
voting_clf.fit(X_train,y_train)
#保存模型
y_predicted = voting_clf.predict(X_train)
print(classification_report(y_train,y_predicted,target_names=['0','1']))
y_predicted = voting_clf.predict(X_test)
print(classification_report(y_test,y_predicted,target_names=['0','1']))
joblib.dump(voting_clf,'teddycup_clf.pkl')