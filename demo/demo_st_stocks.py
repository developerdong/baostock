import baostock as bs
import pandas as pd

# 登陆系统
lg = bs.login()
# 显示登陆返回信息
print('login respond error_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)

# 获取证券基本资料
rs = bs.query_st_stocks()
print('query_st error_code:'+rs.error_code)
print('query_st  error_msg:'+rs.error_msg)

# 打印结果集
st_stocks = []
while (rs.error_code == '0') & rs.next():
    # 获取一条记录，将记录合并在一起
    st_stocks.append(rs.get_row_data())
result = pd.DataFrame(st_stocks, columns=rs.fields)
# 结果集输出到csv文件
result.to_csv("D:/st_stocks.csv", encoding="gbk", index=False)
print(result)

# 登出系统
bs.logout()
