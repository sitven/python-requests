# -*- coding: utf-8 -*-
from branch.log import Log
logger = Log()

def assert_in(asserqiwang, fanhuijson):
    if len(asserqiwang.split('=')) > 1:
        data = asserqiwang.split('&')
        result = dict([(item.split('=')) for item in data])
        value1 = ([(str(fanhuijson[key])) for key in result.keys()])
        value2 = ([(str(value)) for value in result.values()])
        if value1 == value2:
            return {'code': 0, "result": 'pass'}
        else:
            return {'code': 1, 'result': 'fail'}
    else:
        Log().info('填写测试预期值')
        return {"code": 2, 'result': '填写测试预期值'}

# 处理excel表中期望值，转换为字典
def assertre(asserqingwang):
    """
    数据处理方法，通过'='进行分隔将字符串转换成字典格式
    :param asserqingwang: 传参str：code=201
    :return:返回字典
    """
    if len(asserqingwang.split('=')) > 1:                    # 对传入的asserqingwang值根据'='进行切片 大于1则执行代码
        data = asserqingwang.split('&')                      # 将参数“code=400”转换成 ['code=400']
        result = dict([(item.split('=')) for item in data])  # 通过dict方法将[['code=4001']] => {'code': '4001'}
        return result                                        # 返回字典
    else:
        Log().info('填写测试预期值')
        raise {"code": 1, 'result': '填写测试预期值'}

if __name__ =="__main__":
    from branch.get_excel import makedata
    data_test = makedata()
    print(data_test[0]['expect1'])
    print(data_test[0]['expect1'].split('='))
