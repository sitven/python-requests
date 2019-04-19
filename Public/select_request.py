# -*- coding: utf-8 -*-
from Public.requests import requ
from branch.log import Log
from branch.operate_db import Operate_db
from config.readyaml import Getyaml

reques = requ()

class TestApi(object):
	def __init__(self, url, key, connent, fangshi, param_place, assertdata):
		'''
		:param url: 请求的url
		:param key: 带的key
		:param connent: 带的参数
		:param fangshi: 请求方式
		:param param_place: 传参地址(database or None)
		:param assertdata: 期望值2
		'''
		self.url = url						# 请求的url
		self.key = key						# 带的key
		self.connent = connent  				# 带的参数
		self.fangshi = fangshi	        			# 请求方式
		self.param_place = param_place	                	# 传参地址(database or None)
		self.assertdata = assertdata		                # 期望值2

	# 获取请求需要的参数
	def get_param(self):
		'''
		:return: 返回请求参数
		'''
		if self.param_place != 'database':		# 非database传参直接返回excel文件中的参数中的
			return self.connent
		else:
			# 获取数据库名
			self.database = Getyaml(yamlparam="interface_db", interface=self.url).port_db()
			# 通过excel文件中的url匹配yaml文件中key为"interface_db"对应的value来匹配对应获得database名称
			Log().info('当前接口涉及数据库：%s' % self.database)
			# 执行数据库操作
			post_data = Operate_db(self.database, self.url).Perform()		# 传参数据库名和url
			Log().info('数据格式为：%s' % post_data)
			return post_data

	# 根据传参方式，判断执行对应请求
	def testapi(self):
		if self.fangshi == 'POST':
			# self.parem = {'key': self.key, 'info': self.connent}
			self.response = reques.post(self.url, self.get_param(), self.assertdata)
		elif self.fangshi == "GET":
			self.parem = {'key': self.key, 'info': self.connent}
			self.response = reques.get(self.url, self.get_param())
		elif self.fangshi == "PUT":
			# self.parem = {'key': self.key, 'info': self.connent}
			self.response = reques.putfile(self.url, self.get_param(), self.assertdata)
		elif self.fangshi == "DELETE":
			self.parem = {'key': self.key, 'info': self.connent}
			self.response = reques.delfile(self.url, self.get_param())
		return self.response

# def getJson(self):
# 	json_data = self.testapi()
# 	return json_data
