#Author:命命
from yaml import load
from yaml import warnings
import os

# 获取当前脚本所在文件夹路径
curPath = os.path.dirname(os.path.realpath(__file__))
config_path = os.path.join(curPath, "db.yaml")

class Getyaml():
    def __init__(self, yamlparam, interface):
        self.yamlparam = yamlparam                      # 要获取的字典的key
        self.interface = interface                      #

    def get_data(self):
        with open(config_path, 'rb') as f:
            cont = f.read()                             # 获取yaml文件中的所有信息
        warnings({'YAMLLoadWarning': False})            # 禁用加载器warnings报警
        cf = load(cont)                                 # 将bytes格式转成dict格式
        data = cf.get(self.yamlparam)                   # 获取key为self.yamlparam的value
        return data

    def port_db(self):
        # 所请求的接口属于哪个库
        data = self.get_data()
        b = -1
        for a in list(data.keys()):
            b += 1
            if self.interface in list(data[a]):
                c = list(data.keys())[b]
                return c

# param = "orderdb"
# interface = "http://127.0.0.1:5000/requests/5"
# Getyaml(param, interface).get_data()

url = "http://127.0.0.1:5000/todos"
database = Getyaml(yamlparam="interface_db", interface=url).port_db()