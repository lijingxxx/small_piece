
# -*- coding: utf-8 -*-

import xlrd

# file = r"/Users/chenming/ljx_workspace/python/src/main/resource/imei.xlsx"  # 打开指定路径中的文件

#file = r"/Users/chenming/ljx_workspace/python/src/main/resource/result_sql_20180810141622_2018_08_10.xlsx"

file = r"E:\workspace\small_piece\src\main\resource\result_sql_20180810141622_2018_08_10.xlsx"

imei = xlrd.open_workbook(file)  # 实例化
sheet0 = imei.sheet_by_index(0)  # 获得第一页

col0 = sheet0.col_values(0)  # 获取第一列的值
col1 = sheet0.col_values(1)
col2 = sheet0.col_values(2)
col3 = sheet0.col_values(3)
app = []

for i in range(1, len(col0)):
    if col0[i] in col1 and col0[i] in col2 and col0[i] in col3:
        app.append(col0[i])

print(app)
