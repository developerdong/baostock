# -*- coding:utf-8 -*-
from setuptools import setup, find_packages

long_desc = """
BaoStock
===============

* It's easy to use because most of the data returned are pandas DataFrame objects
* We have our own data server, efficient and stable operation
* Free china stock market data
* Friendly to machine learning and data mining

Target Users
--------------

* China Financial Market Analyst
* Financial data analysis enthusiasts
* Quanters who are interested in china stock market

Installation
--------------

    pip install baostock

Upgrade
---------------

    pip install baostock --upgrade

Quick Start
--------------

::

    import baostock as bs
    import pandas as pd

    # 登陆系统
    lg = bs.login()
    # 显示登陆返回信息
    print(lg.error_code)
    print(lg.error_msg)
    # 详细指标参数，参见“历史行情指标参数”章节
    rs = bs.query_history_k_data("sh.601398",
        "date,code,open,high,low,close,volume,amount,adjustflag",
        start_date='2017-01-01', end_date='2017-01-31',
        frequency="d", adjustflag="3")
    print(rs.error_code)
    print(rs.error_msg)
    # 获取具体的信息
    result_list = []
    while (rs.error_code == '0') & rs.next():
        # 分页查询，将每页信息合并在一起
        result_list.append(rs.get_row_data())
    result = pd.DataFrame(result_list, columns=rs.fields)
    result.to_csv("D:/history_k_data.csv", encoding="gbk", index=False)
    print(result)
    # 登出系统
    bs.logout()

return::

              date       code    open    high     low   close preclose     volume
    0   2017-01-03  sh.601398  4.4000  4.4300  4.3900  4.4300   4.4100  104161632   
    1   2017-01-04  sh.601398  4.4200  4.4400  4.4100  4.4300   4.4300  118923425   
    2   2017-01-05  sh.601398  4.4300  4.4500  4.4200  4.4400   4.4300   87356137   
    3   2017-01-06  sh.601398  4.4400  4.4500  4.4300  4.4400   4.4400   87008191   
    4   2017-01-09  sh.601398  4.4500  4.4800  4.4300  4.4600   4.4400  117454094   
    5   2017-01-10  sh.601398  4.4500  4.4700  4.4400  4.4600   4.4600   63663257   
    6   2017-01-11  sh.601398  4.4600  4.4800  4.4500  4.4700   4.4600   52395427   
    7   2017-01-12  sh.601398  4.4600  4.4700  4.4400  4.4700   4.4700   62166279    
    
                 amount adjustflag      turn tradestatus  
    0    460087744.0000          3  0.038634           1  
    1    526408816.0000          3  0.044109           1  
    2    387580736.0000          3  0.032401           1  
    3    386138112.0000          3  0.032272           1  
    4    523539392.0000          3  0.043564           1  
    5    283646224.0000          3  0.023613           1  
    6    233898107.0000          3  0.019434           1  
    7    277258304.0000          3  0.023058           1  

"""


setup(
    name='baostock',
    version='0.8.8',
    description=(
        'A tool for obtaining historical data of China stock market'
    ),
    long_description=long_desc,
    author='baostock',
    author_email='baostock@163.com',
    license='BSD License',
    packages=find_packages(),
    platforms=["all"],
    url='http://www.baostock.com',
    install_requires=[
        'pandas>=0.18.0'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',   # 开发状态
        'Environment :: Console',  # 运行环境
        'License :: OSI Approved :: BSD License',  # BSD协议
        'Operating System :: OS Independent',  # 与平台无关
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],
)
