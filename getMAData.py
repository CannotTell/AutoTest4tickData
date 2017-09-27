#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 9/2/2017 11:49 AM
# @Author  : JZK
# @File    : getMAData.py

import Check_Data
import datetime

tdc = Check_Data.tick_data_check()

sourceFileName = 'C:\\Users\\zhukai.jiang\\Desktop\\600848_MA.xlsx'
genFileName = 'C:\\Users\\zhukai.jiang\\Desktop\\DownloadStock\\600848;1个月;MA5,60_New.xlsx'

sourceData = tdc.get_Data(sourceFileName)
genData = tdc.get_Data(genFileName)


print(sourceData)

m = datetime.timedelta(minutes=1)
ll = []
for k, i in enumerate(sourceData):
    temp = []
    strDate = i[0].strip()
    d = datetime.datetime.strptime(strDate, '%Y/%m/%d-%H:%M')
    temp.append(d.strftime('%Y/%m/%d-%H:%M'))
    temp.append(i[1])
    ll.append(temp)
    if d.strftime('%Y/%m/%d-%H:%M').split('-')[1] != '15:00':
        avanage = (sourceData[k + 1][1] - i[1]) / 5
        p = i[1]
        for j in range(4):
            temp2 = []
            d = d + m
            p = p + avanage
            temp2.append(d.strftime('%Y/%m/%d-%H:%M'))
            temp2.append(p)
            ll.append(temp2)
    # c = d + m
    # print(d)
    # print(c)

for x in ll:
    print(x)
# ll = []
# for i in sourceData:
#     t = []
#     strs = i[0].strip().split('-')
#     t.append(i[0].strip())
#     t.append(i[6])
#     t.append(i[7])
#     for k, v in enumerate(genData):
#         price = 0
#         singel = -1
#         if type(v[1]) is datetime.datetime:
#             date = v[1].strftime("%Y/%m/%d")
#             time = v[2].strftime("%H:%M")
#             if date == strs[0] and time == strs[1]:
#                 if v[4] is not None:
#                     price = v[4]
#                     singel = 1
#                 else:
#                     singel = 0
#                     if v[3] is not None:
#                         price = v[3]
#                     else:
#                         price = v[5]
#                 t.append(price)
#                 t.append(singel)
#                 del genData[k]
#                 break
#             else:
#                 continue
#         else:
#             del genData[k]
#         # t.append(None)
#         # t.append(None)
#     # t.append(i[0].strip())
#     # t.append(i[6])
#     # t.append(i[7])
#     if len(t) == 5:
#         ll.append(t)
#     else:
#         t.append('')
#         t.append('')
#         ll.append(t)
#
#
# # for y in genData:
# #     print(y)
# #
# # print(len(genData))
#
# for o in genData:
#     tempList = []
#     price = 0
#     single = -1
#     tempList.append('{}-{}'.format(o[1].strftime("%Y/%m/%d"), o[2].strftime("%H:%M")))
#     tempList.append('')
#     tempList.append('')
#     if o[4] is not None:
#         price = o[4]
#         singel = 1
#     else:
#         singel = 0
#         if o[3] is not None:
#             price = o[3]
#         else:
#             price = o[5]
#     tempList.append(price)
#     tempList.append(singel)
#     ll.append(tempList)
#
#
#
# for x in ll:
#     d = x[0].replace('-', ' ')
#     datetime_object = datetime.datetime.strptime(d, '%Y/%m/%d %H:%M')
#     x[0] = datetime_object
#     #print(x)
# ll = sorted(ll)
# for xx in ll:
#     print(xx)
#
#
# for k, v in enumerate(ll):
#     if a[1] == '':
#         if ()
# print(ll)
#
# print (genData)
# print(len(ll))
# for i in genData:
#     if (type(i[1]) is datetime.datetime):
#         date = i[1].strftime("%Y/%m/%d")
#         time = i[2].strftime("%H:%M")
#
# for d in sourceData:
#     if type(d[1]) is datetime.datetime:
#         # print(d[2].strftime("%H:%M")[-1])
#         if d[2].strftime("%H:%M")[-1] != '0' and d[2].strftime("%H:%M")[-1] != '5':
#             print(d)
# print(sourceData)
# ll = []
# for i in range(4, len(sourceData) - 1):
#     # print(sourceData[i])
#     t = []
#     t.append(sourceData[i][0].strip())
#     t.append(sourceData[i][6] if sourceData[i][6] != '           ' else '')
#     t.append(sourceData[i][7])
#     ll.append(t)
#
# print(ll)

