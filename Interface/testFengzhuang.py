# -*- coding: utf-8 -*-
# @Time    : 2017/6/4 20:36
# @Author  : lileilei
# @Site    : 
# @File    : testFengzhuang.py
# @Software: PyCharm
from Interface.test_requests import reques,json

reques=reques()
class TestApi(object):
	def __init__(self,url,key,connent,fangshi):
		self.url=url
		self.key=key
		self.connent=connent
		self.fangshi=fangshi
		self.resp = ""
		self.resStr = ""
	def testapi(self):
		if self.fangshi=='POST':
			# global data
			self.parem =  self.connent
			page = self.key
			# if len(self.parem) > 0:
			data = json.loads(self.parem)
			data["page"] = page
			p =  json.dumps(data)
			response=reques.post(self.url,p)
			self.resp = response
			self.resStr = json.dumps(response)
		elif self.fangshi=="GET":
			self.parem = {'key': self.key, 'info': self.connent}
			response = reques.post(self.url, self.parem)
		return response
	# def getcode(self):
	# 	code=self.resp['code']
	# 	return code
	def getJson(self):
		json_data = self.testapi()
		return json_data