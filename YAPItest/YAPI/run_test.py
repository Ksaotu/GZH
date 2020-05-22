'''
@Time  : 2020/4/14 16:05
@Author: fengzhj
@doc   : 运行接口自动化测试集合
'''
from yapi import YapiTest

yapi = YapiTest()
yapi.yapi_test([542])
yapi.send()