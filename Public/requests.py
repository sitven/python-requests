# -*- coding: utf-8 -*-import jsonimport requestsimport xml.etree.ElementTree as ETfrom xml.etree.ElementTree import Elementfrom branch.log import Logclass requ():    def __init__(self):        self.headers = {            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:51.0) Gecko/20100101 Firefox/51.0"        }    def dict_to_xml(self, tag, d):        # tag为头尾标签，d传入字典        elem = Element(tag)        for key, val in d.items():            child = Element(key)            child.text = str(val)            elem.append(child)        return elem    def xml_to_dict(self, xml_str):        msg = {}        root_elem = ET.fromstring(xml_str)        for ch in root_elem:            msg[ch.tag] = ch.text        return msg    def get(self, url, params):        # get消息        '''        :param url: 请求的url        :param params: 请求带的参数        :return: 返回响应码和text        '''        try:            r = requests.get(url, params=params, headers=self.headers)            r.encoding = 'UTF-8'            response_code = r.status_code            response_text = r.text            Log().info('成功发起GET请求，请求结果code为：%s, 请求结果字段为：%s' % (response_code, response_text))            return response_code, response_text        except Exception as e:            Log().error('get请求出错，出错原因:%s' % e)            return {'code': 1, 'result': 'get请求出错，出错原因:%s' % e}    def post(self, url, params, assertdata):  # post消息        # data = json.dumps(params)        try:            data = json.loads(params)            r =requests.post(url, data, headers=self.headers)            response_code = r.status_code            response_text1 = json.loads(r.text)[assertdata]  # 对返回的指定字段断言，字段名取自Excel的期望2            Log().info('成功发起POST请求，请求结果code为：%s, 请求结果字段为：%s' % (response_code, json.loads(r.text)))            return response_code, response_text1        except Exception as e:            Log().error('post请求出错，出错原因:%s' % e)            return {'code': 1, 'result': 'post请求出错，出错原因:%s' % e}    def delfile(self, url, params):  # 删除的请求        try:            r = requests.delete(url, params=params, headers=self.headers)            response_code = r.status_code            response_text = r.text            Log().info('成功发起DELETE请求，请求结果code为：%s, 请求结果字段为：%s' % (response_code, response_text))            return response_code, response_text        except Exception as e:            Log().error('delete请求出错，出错原因:%s' % e)            return {'code': 1, 'result': 'del请求出错，出错原因:%s' % e}    def putfile(self, url, params, assertdata):                 # put请求        try:            data = json.loads(params)            r = requests.put(url, data)            response_code = r.status_code            response_text1 = json.loads(r.text)[assertdata]     # 对返回的指定字段断言，字段名取自Excel的期望2            Log().info('成功发起PUT请求，请求结果code为：%s, 请求结果字段为：%s' % (response_code, json.loads(r.text)))            return response_code, response_text1        except Exception as e:            Log().error('put请求出错，出错原因:%s' % e)            return {'code': 1, 'result': 'put请求出错，出错原因:%s' % e}