#coding=utf-8
import os

from basic.readconfig import ReadConfig

# Read configuration file
config_file_path = os.path.split(os.path.realpath(__file__))[0]
read_config = ReadConfig(os.path.join(config_file_path, 'config.ini'))
# Project parameter setting
prj_path = read_config.getValue('projectConfig', 'project_path')
# print(prj_path)
# Log path
log_path = os.path.join(prj_path, 'report', 'log')
# Screenshot file path
img_path = os.path.join(prj_path, 'report', 'image')
#Exception screenshot file path
eximg_path = os.path.join(prj_path, 'report', 'exception_img')
#Test report path
report_path = os.path.join(prj_path, 'report', 'test_report')
#Upload the autoit file path
auto_path = os.path.join(prj_path, 'up_files', 'autoit_pic')
#
yaml_path = os.path.join(prj_path, 'config', 'readyaml')
# Default browser
browser = 'chrome'
# Test data path
data_path = os.path.join(prj_path, '', 'testdata')


project_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
# print(project_path)  # 获取当前项目路径
y_path = os.path.join(project_path, 'config', 'db.yaml')
# print(y_path)    # 获取db.yaml文件路径