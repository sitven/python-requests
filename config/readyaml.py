from yaml import load
from yaml import warnings
import os

# 获取当前脚本所在文件夹路径
curPath = os.path.dirname(os.path.realpath(__file__))
config_path = os.path.join(curPath, "db.yaml")

class Getyaml():
    def __init__(self, yamlparam, interface):
        self.yamlparam = yamlparam                      # 传参yaml的key获取value
        self.interface = interface

    def get_data(self):
        # 通过yamlparam参数获取yaml文件对应的value
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
        for a in list(data.keys()):                   # list(data.keys()) 获取data字典中的所有可以组建成list
            b += 1
            if self.interface in list(data[a]):
                c = list(data.keys())[b]
                return c

# param = "orderdb"
# interface = "http://127.0.0.1:5000/requests/5"
# Getyaml(param, interface).get_data()
if __name__ == "__main__":
    with open(config_path, 'rb') as f:
        cont = f.read()                             # 获取yaml文件中的所有信息
    warnings({'YAMLLoadWarning': False})            # 禁用加载器warnings报警
    cf = load(cont)                                 # 将bytes格式转成dict格式
    data = cf.get("interface_db")                   # 获取key为self.yamlparam的value
    print(data)
    b = -1
    print(list(data.keys()))
    for a in list(data.keys()):
        b += 1
        if 'http://127.0.0.1:5000/todos' in list(data[a]):
            c = list(data.keys())[b]
            print(c)