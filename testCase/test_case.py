# -*- coding: utf-8 -*-
# @Time    : 2017/6/4 20:15
# @Author  : lileilei
# @File    : test_case.py
from  Interface.testFengzhuang import TestApi
from  Public.get_excel import datacel
from  Public.tsest_log import log_re
listid,listkey,listconeent,listurl,listfangshi,listqiwang,listname=datacel()
from Public.panduan import assert_in
title='测试日志'
log_can=log_re(title)
def testinterface():
    list_pass = 0
    list_fail = 0
    list_json = []
    listrelust=[]
    listjson = []
    listres = []
    for i in range(len(listurl)):
        for n in range(1,int(listkey[i])+1):
            print(int(listkey[i]))
            api = TestApi(url=listurl[i], key=n, connent=listconeent[i], fangshi=listfangshi[i])
            # apicode = api.getcode()
            apijson = api.getJson()
            log_can.info_log(
                'inputdata> 参数:%s, url:%s ,返回:%s,预期:%s' % (listconeent[i], listurl[i], apijson, listqiwang[i]))
            assert_re = assert_in(asserqiwang=listqiwang[i], fanhuijson=apijson)
            if assert_re == 'pass':
                listjson.append(apijson)
                listres.append('pass')
                list_pass += 1
            else:
                list_fail += 1
                listres.append('fail')
                listjson.append(apijson)
    # list_json.append(listjson)
    # listrelust.append(listres)
    return  listres,list_fail,list_pass,listjson