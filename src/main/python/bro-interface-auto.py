# -*- coding:utf-8 -*-
import requests
# 接口：http://bro.flyme.cn/client/getState.do?userId=111894945

# 请求接口：
r = requests.get('http://bro.flyme.cn/client/getState.do?userId=111894945')
r1 =requests.get('http://bro.flyme.cn/client/getState.do',params={'userId':'111894945'})
# 获取实际请求的url并打印：
print(r.url)
print(r1.url)
# 获取json类型返回值并打印：
print(r.json())
print(r1.json())
# 获取json返回值中的某些值并打印
print(r.json()['code'])
print(r.json()['value'])
print(r.json()['value']['state'])
# 获取url的headers并打印：
print(r.headers)
