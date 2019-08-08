# -*- coding: utf-8 -*-

import os
import xlrd
from basic.log import Log
from config import globalparam

log_path = globalparam.log_path
file_path = globalparam.data_path


# 获取xlsx文件的数据并保存到列表中
def datacel(filrpath):
    try:
        file = xlrd.open_workbook(filrpath)         # 打开xls文件
        me = file.sheets()[0]                       # 获取第一个表的信息
        nrows = me.nrows                            # 获取该sheet中的有效行数
        listid = []                                 # 用例ID
        listname = []                               # 用例名称
        listkey = []                                # key(需要key可以在这里增加key)
        listconeent = []                            # 参数
        listparam_place = []                        # 传参地址
        listurl = []                                # 请求的url
        listfangshi = []                            # 请求方式
        listqiwang1 = []                            # 期望值1
        listqiwang2 = []                            # 期望值2
        for i in range(1, nrows):                       # 对sheet中的有效测试数据的总行数进行遍历
            listid.append(me.cell(i, 0).value)              # 根据坐标返回对应的单元格对象
            listname.append(me.cell(i, 1).value)
            listkey.append(me.cell(i, 2).value)
            listconeent.append(me.cell(i, 3).value)
            listparam_place.append(me.cell(i, 4).value)
            listurl.append(me.cell(i, 5).value)
            listfangshi.append((me.cell(i, 6).value))
            listqiwang1.append((me.cell(i, 7).value))
            listqiwang2.append((me.cell(i, 8).value))
        return listid, listname, listkey, listconeent, listparam_place, \
               listurl, listfangshi, listqiwang1, listname, listqiwang2
    except:
        Log().error('打开测试用例失败，原因是:%s' % Exception)

# 根据
def data(aa):
    '''
    :param aa: 传入文件名
    :return:   返回数据文件中测试数据字典组成的list
    '''
    path = file_path + "/" + "case{0}.xlsx".format(aa)      # 拼接测试数据文件路径
    listid, listname, listkey, listconeent, listparam_place, listurl, \
    listfangshi, listqiwang1, listname, listqiwang2 = datacel(path)
    # 获取测试数据列组成的列表
    make_data1 = []
    try:
        for i in range(len(listid)):
            make_data1.append({'url': listurl[i], 'listname': listname[i], 'key': listkey[i], 'coneent': listconeent[i],
                               'param_place': listparam_place[i], 'fangshi': listfangshi[i], 'expect1': listqiwang1[i],
                               'expect2': listqiwang2[i]})
        return make_data1
    except:
        Log().error('打开测试用例失败，原因是:%s' % Exception)

# 获取testdata目录下xlsx文件数量
def makedata():
    '''
    :return: 返回整合后的测试用例
    '''
    count = 0
    make_data = []
    for root, dirs, files in os.walk(file_path):
        # for root, dirs, files in os.walk(file_path)返回三元组
        # root: 文件夹的本身的地址；
        # dirs: 返回当前文件夹下所有目录list；
        # files: 返回当前文件夹下所有文件list'''
        for each in files:
            count += 1
    for aa in range(count):
    # 用例整合
        aa += 1
        for bb in data(aa):                 # 将不同xlsx文件内的测试数据追加到make_data列表中
            make_data.append(bb)
    return make_data

if __name__ == "__main__":
    print(file_path)
    print(makedata())