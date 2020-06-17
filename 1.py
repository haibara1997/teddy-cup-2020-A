#查看原始数的缺失值情况 输入：原始数据 输出：原始数据的具体缺失信息
daily_data = pd.read_csv('/kaggle/input/teddycup/A题全部数据/日数据.csv',encoding='GBK')
yearly_data =  pd.read_csv('/kaggle/input/teddycup/A题全部数据/年数据.csv',encoding='GBK')
fun_data = pd.read_csv('/kaggle/input/teddycup/A题全部数据/基础数据.csv',encoding='GBK')
print('日数据形状：{}'.format(daily_data.shape))
print('年数据形状:{}'.format(yearly_data.shape))
print('基础数据形状：{}'.format(fun_data.shape))
print(daily_data.columns) #日数据的61个变量
for x in list(yearly_data.columns): #年数据的362个变量
    print(x)
print(fun_data.columns)
#年数据的缺失值情况
#(24262, 362)年数据的shape
print(yearly_data.isnull().any())
print("其中有这么多列是有空缺数据的：")
print(sum(yearly_data.isnull().any()))
#建立一个记录缺失值比例的DataFrame
yearly_null_col_ratio = pd.Series([],name='年数据缺失值比例')
print('年数据分别有以下几列是有空缺值的(每列总共有24262个数据)')
print('有缺失值的列','\t\t\t\t\t','缺失值的数量''\t','缺失值数量占总体的百分比')
tell_if_null = yearly_data.isnull().any()
null_columns = tell_if_null[tell_if_null==1]
i=0#计数器而已
for null_column in null_columns.index:
    num_of_nulls = sum(yearly_data[null_column].isnull())
    print("{:<40}\t{:>10}\t{:>10.2%}".format(null_column,num_of_nulls,(num_of_nulls/24262)))
    yearly_null_col_ratio[i] = num_of_nulls/24262
    i += 1
#日数据的缺失值情况
#(5899132, 61)日数据的shape
print(daily_data.isnull().any())
print("其中有这么多列是有空缺数据的：")
print(sum(daily_data.isnull().any()))
#建立一个记录缺失值比例的DataFrame
daily_null_col_ratio = pd.Series([],name='日数据缺失值比例')
print('日数据分别有以下几列是有空缺值的(每列总共有5899132个数据)')
print('\t有缺失值的列','\t\t','缺失值的数量''\t\t','缺失值数量占总体的百分比')
tell_if_null = daily_data.isnull().any()
null_columns = tell_if_null[tell_if_null==1]
i = 0#计数器而已
for null_column in null_columns.index:
    num_of_nulls = sum(daily_data[null_column].isnull())
    print("{:^20}\t{:^10d}\t{:>10.2%}".format(null_column,num_of_nulls,num_of_nulls/5899132))
    daily_null_col_ratio[i] = num_of_nulls/5899132
    i += 1
#基础数据的缺失值情况
#(3466, 4) 基础数据的shape
print(fun_data.isnull().any())
print("其中有这么多列是有空缺数据的：")
print(sum(fun_data.isnull().any()))
print('基础数据分别有以下几列是有空缺值的(每列总共有5899132个数据)')
print('\t有缺失值的列','\t\t','缺失值的数量''\t\t','缺失值数量占总体的百分比')
tell_if_null = fun_data.isnull().any()
null_columns = tell_if_null[tell_if_null==1]
for null_column in null_columns.index:
    num_of_nulls = sum(fun_data[null_column].isnull())
    print("{:^20}\t{:^10d}\t{:>10.2%}".format(null_column,num_of_nulls,num_of_nulls/3466))

