#!/usr/bin/env python
# coding:utf-8

"""
@author:Joey
create:2017-06-13
"""

import xlwt,os,json

def GetReport(jsonStr):
    resultJson = json.loads(jsonStr)
    sqlList = resultJson["result"]
    #生成一个Excel对象
    file = xlwt.Workbook()
    ws = file.add_sheet('Result Sheet')
    #添加title
    ws.write(0, 0, "SQL")
    ws.write(0, 1, "Server")
    ws.write(0, 2, "Client")
    ws.write(0, 3, "runSql")
    beginRow = 0
    #循环将数据插入Excel
    for i in range(0,len(sqlList)):
        sqlResult = sqlList[i]
        clientList = sqlResult["clients"]
        sqlStr = sqlResult["sql"]

        #合并单元格SQL
        ws.write_merge(beginRow + 1,beginRow + len(clientList) , 0, 0, sqlStr)
        #将生产端信息以及客户端信息放入Excel
        for j in range(0,len(clientList)):
            infoObject = clientList[j]
            ws.write(beginRow + j + 1, 1, infoObject["productDb"])
            ws.write(beginRow + j + 1, 2, infoObject["client"])
            ws.write(beginRow + j + 1, 3, infoObject["runsql"])
        beginRow = beginRow + len(clientList)
    file.save(os.path.abspath('.') + "\\"+"Result.xls")




