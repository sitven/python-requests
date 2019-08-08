# coding=utf-8

import os
import pymysql
from basic.log import Log
from config.readyaml import Getyaml

# 获取当前脚本所在文件夹路径
curPath = os.path.dirname(os.path.realpath(__file__))
config_path = os.path.join(curPath, "db.yaml")

class Operate_db():
    def __init__(self, getdb, interface_url):       # 传参数据库信息的key和请求的url
        self.getdb = getdb
        self.interface_url = interface_url

    # 连接数据库
    def connect_db(self):
        self.getdb1 = Getyaml(yamlparam=self.getdb, interface='interface').get_data()
        # 通过传参的数据库信息key获取数据库信息
        db1 = pymysql.connect(self.getdb1[0], self.getdb1[1], self.getdb1[2], self.getdb1[3], charset='utf8')
        # 连接远程数据库
        return db1

    # 获取sql语句
    def get_sql(self):
        self.sql = Getyaml(yamlparam="interface_sql", interface='interface').get_data()
        for key, value in self.sql.items():
            if key == self.interface_url:
                return value

    # 执行sql语句
    def Perform(self):
        # 使用cursor()方法获取操作游标
        self.db = self.connect_db()
        self.cursor = self.db.cursor()
        sql = self.get_sql()
        version = self.db.server_version
        Log().info('成功登录数据库：%s，版本为：%s，执行SQL：%s' % (self.getdb, version, sql))
        if "SELECT" in sql or "select" in sql:
            # 执行查询语句
            try:
                self.cursor.execute(sql)
                results = self.cursor.fetchall()                # 获取查询结果
                Log().info('查询结果：%s' % results[0][0])
                return results[0][0]
            except:
                Log().info("Error: unable to fetch data")
                raise
        elif "UPDATE" in sql or "update" in sql:
            # 执行update语句
            try:
                self.cursor.execute(sql)                        # 执行sql语句
                self.db.commit()
                Log().info("更新成功")
            except:
                self.db.rollback()                              # 数据更新失败，进行回滚
                Log().info("Error：Has been rolled back")
                raise
        self.db.close()

interface_url = "http://127.0.0.1:5000/todos/todo2"
getdb = "orderdb"
Operate_db(getdb, interface_url).Perform()
