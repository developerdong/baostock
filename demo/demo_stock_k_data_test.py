'''
Created on 2019年1月17日

@author: ZYP
'''
import baostock as bs
import pandas as pd



def test_day_data(code, adjust_flag):
    #### 获取历史K线数据 ####
    # 详细指标参数，参见“历史行情指标参数”章节
        
    rs_old = bs.query_history_k_data(code,
    "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,peTTM,pbMRQ,psTTM,pcfNcfTTM,isST",
    start_date='1990-01-01', end_date='2019-01-16', 
    frequency="d", adjustflag=adjust_flag)
#### 打印结果集 ####
    data_list = []
    while (rs_old.error_code == '0') & rs_old.next():
        # 获取一条记录，将记录合并在一起
        data_list.append(rs_old.get_row_data())
    result1 = pd.DataFrame(data_list, columns=rs_old.fields)
    #### 结果集输出到csv文件 ####
#         result1.to_csv("D:/history_k_data_plus.csv", encoding="gbk", index=False)
    
    rs_old_2 = bs.query_history_k_data(code,
        "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,peTTM,pbMRQ,psTTM,pcfNcfTTM,isST",
        start_date='1990-01-01', end_date='2019-01-16', 
         frequency='d', adjustflag=adjust_flag)
    result2 = rs_old_2.get_data();
#         result2.to_csv("D:/history_k_data.csv", encoding="gbk", index=False)

    rs_plus = bs.query_history_k_data_plus(code,
    "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,peTTM,pbMRQ,psTTM,pcfNcfTTM,isST",
    start_date='1990-01-01', end_date='2019-01-16', 
     frequency='d', adjustflag=adjust_flag)
    #### 打印结果集 ####
    data_list = []
    while (rs_plus.error_code == '0') & rs_plus.next():
        # 获取一条记录，将记录合并在一起
        data_list.append(rs_plus.get_row_data())
    result3 = pd.DataFrame(data_list, columns=rs_plus.fields)
    #### 结果集输出到csv文件 ####
#         result3.to_csv("D:/history_k_data_plus.csv", encoding="gbk", index=False)
    
    rs_plus_2 = bs.query_history_k_data_plus(code,
        "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,peTTM,pbMRQ,psTTM,pcfNcfTTM,isST",
        start_date='1990-01-01', end_date='2019-01-16', 
         frequency='d', adjustflag=adjust_flag)
    result4 = rs_plus_2.get_data();
    #### 结果集输出到csv文件 ####
#         result4.to_csv("D:/history_k_data_plus2.csv", encoding="gbk", index=False)

#     print(code + " test finished!")
#     fileopen.write(code + " test finished!")
        
def test_week_month_data(code, frequency_flag, adjust_flag):
    #### 获取历史K线数据 ####
    # 详细指标参数，参见“历史行情指标参数”章节
        
    rs_old = bs.query_history_k_data(code,
    "date,code,open,high,low,close,volume,amount,adjustflag,turn,pctChg",
    start_date='1990-01-01', end_date='2019-01-16', 
    frequency=frequency_flag, adjustflag=adjust_flag)
#     print('query_history_k_data respond error_code:'+rs.error_code)
#     print('query_history_k_data respond  error_msg:'+rs.error_msg)
#### 打印结果集 ####
    data_list = []
    while (rs_old.error_code == '0') & rs_old.next():
        # 获取一条记录，将记录合并在一起
        data_list.append(rs_old.get_row_data())
    result1 = pd.DataFrame(data_list, columns=rs_old.fields)
    #### 结果集输出到csv文件 ####
#         result1.to_csv("D:/history_k_data_plus.csv", encoding="gbk", index=False)
    
    
    rs_old_2 = bs.query_history_k_data(code,
        "date,code,open,high,low,close,volume,amount,adjustflag,turn,pctChg",
        start_date='1990-01-01', end_date='2019-01-16', 
         frequency=frequency_flag, adjustflag=adjust_flag)
    result2 = rs_old_2.get_data();
#         result2.to_csv("D:/history_k_data.csv", encoding="gbk", index=False)
    
    
    
    
    rs_plus = bs.query_history_k_data_plus(code,
    "date,code,open,high,low,close,volume,amount,adjustflag,turn,pctChg",
    start_date='1990-01-01', end_date='2019-01-16', 
     frequency=frequency_flag, adjustflag=adjust_flag)
    #### 打印结果集 ####
    data_list = []
    while (rs_plus.error_code == '0') & rs_plus.next():
        # 获取一条记录，将记录合并在一起
        data_list.append(rs_plus.get_row_data())
    result3 = pd.DataFrame(data_list, columns=rs_plus.fields)
    #### 结果集输出到csv文件 ####
#         result3.to_csv("D:/history_k_data_plus.csv", encoding="gbk", index=False)
    
    
    rs_plus_2 = bs.query_history_k_data_plus(code,
        "date,code,open,high,low,close,volume,amount,adjustflag,turn,pctChg",
        start_date='1990-01-01', end_date='2019-01-16', 
         frequency=frequency_flag, adjustflag=adjust_flag)
#     print('query_history_k_data respond error_code:'+rs.error_code)
#     print('query_history_k_data respond  error_msg:'+rs.error_msg)
    result4 = rs_plus_2.get_data();
    #### 结果集输出到csv文件 ####
#         result4.to_csv("D:/history_k_data_plus2.csv", encoding="gbk", index=False)

#     print(code + " test finished!")
#     fileopen.write(code + " test finished!")

def test_minutes_data(code, frequency_flag, adjust_flag):
    #### 获取历史K线数据 ####
    # 详细指标参数，参见“历史行情指标参数”章节
        
    rs_old = bs.query_history_k_data(code,
    "date,code,open,high,low,close,volume,amount,adjustflag",
    start_date='1990-01-01', end_date='2019-01-16', 
    frequency=frequency_flag, adjustflag=adjust_flag)
#     print('query_history_k_data respond error_code:'+rs.error_code)
#     print('query_history_k_data respond  error_msg:'+rs.error_msg)
#### 打印结果集 ####
    data_list = []
    while (rs_old.error_code == '0') & rs_old.next():
        # 获取一条记录，将记录合并在一起
        data_list.append(rs_old.get_row_data())
    result1 = pd.DataFrame(data_list, columns=rs_old.fields)
    #### 结果集输出到csv文件 ####
#         result1.to_csv("D:/history_k_data_plus.csv", encoding="gbk", index=False)
    
    
    rs_old_2 = bs.query_history_k_data(code,
        "date,code,open,high,low,close,volume,amount,adjustflag",
        start_date='1990-01-01', end_date='2019-01-16', 
         frequency=frequency_flag, adjustflag=adjust_flag)
    result2 = rs_old_2.get_data();
#         result2.to_csv("D:/history_k_data.csv", encoding="gbk", index=False)
    
    
    
    
    rs_plus = bs.query_history_k_data_plus(code,
    "date,code,open,high,low,close,volume,amount,adjustflag",
    start_date='1990-01-01', end_date='2019-01-16', 
     frequency=frequency_flag, adjustflag=adjust_flag)
    #### 打印结果集 ####
    data_list = []
    while (rs_plus.error_code == '0') & rs_plus.next():
        # 获取一条记录，将记录合并在一起
        data_list.append(rs_plus.get_row_data())
    result3 = pd.DataFrame(data_list, columns=rs_plus.fields)
    #### 结果集输出到csv文件 ####
#         result3.to_csv("D:/history_k_data_plus.csv", encoding="gbk", index=False)
    
    
    rs_plus_2 = bs.query_history_k_data_plus(code,
        "date,code,open,high,low,close,volume,amount,adjustflag",
        start_date='1990-01-01', end_date='2019-01-16', 
         frequency=frequency_flag, adjustflag=adjust_flag)
#     print('query_history_k_data respond error_code:'+rs.error_code)
#     print('query_history_k_data respond  error_msg:'+rs.error_msg)
    result4 = rs_plus_2.get_data();
    #### 结果集输出到csv文件 ####
#         result4.to_csv("D:/history_k_data_plus2.csv", encoding="gbk", index=False)
# 
#     print(code + " test finished!")
#     fileopen.write(code + " test finished!")




if __name__ == '__main__':
    #### 登陆系统 ####
    lg = bs.login()
    # 显示登陆返回信息
    print('login respond error_code:'+lg.error_code)
    print('login respond  error_msg:'+lg.error_msg)
    
    #### 获取全部证券 ####
    codes = bs.query_stock_basic()
    codesdf = codes.get_data()
    codesdf.to_csv("D:/history_k_data_codes.csv", encoding="gbk", index=False)
    codeslist = codesdf['code']
    
    fileopen = open("D:/history.logs","a+")
    
    frequency_flag = "m"
#     adjust_flag = "3"
#     fileopen.write(" adjust_flag:"+adjust_flag+"\n")
    for code in codeslist:
        test_day_data(code,"3")
        test_week_month_data(code,"m","3")
        test_week_month_data(code,"w","3")
        test_minutes_data(code,"60","3")
        test_minutes_data(code,"30","3")
        test_minutes_data(code,"15","3")
        test_minutes_data(code,"5","3")

        fileopen.write(code + " 不复权  test finished!\n")
        
        test_day_data(code,"1")
        test_week_month_data(code,"m","1")
        test_week_month_data(code,"w","1")
        test_minutes_data(code,"60","1")
        test_minutes_data(code,"30","1")
        test_minutes_data(code,"15","1")
        test_minutes_data(code,"5","1")

        fileopen.write(code + " 前复权  test finished!\n")
        
        test_day_data(code,"2")
        test_week_month_data(code,"m","2")
        test_week_month_data(code,"w","2")
        test_minutes_data(code,"60","2")
        test_minutes_data(code,"30","2")
        test_minutes_data(code,"15","2")
        test_minutes_data(code,"5","2")
        print(code + " test finished!")
        fileopen.write(code + " 后复权 test finished!\n")
    fileopen.close()
    #### 登出系统 ####
    bs.logout()
