#coding=utf-8
import os

from basic.readconfig import ReadConfig

# 项目路径参数设置
prj_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

# config配置文件路径
config_file_path = os.path.join(prj_path, "config")
read_config = ReadConfig(os.path.join(config_file_path, 'config.ini'))      # 读取

# Log path
log_path = os.path.join(prj_path, 'report', 'log')
# print(log_path)

# 截图路径
img_path = os.path.join(prj_path, 'report', 'image')
# Exception screenshot file path
eximg_path = os.path.join(prj_path, 'report', 'exception_img')
# 测试报告文件路径
report_path = os.path.join(prj_path, 'report', 'test_report')
# Upload the autoit file path
auto_path = os.path.join(prj_path, 'up_files', 'autoit_pic')
# yaml配置文件路径
yaml_path = os.path.join(prj_path, 'config', 'readyaml')
# Default browser
browser = 'chrome'

# 测试数据路径
data_path = os.path.join(prj_path, '', 'testdata')
