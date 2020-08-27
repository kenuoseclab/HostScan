# -*- encoding: utf-8 -*-
'''
@Author : aydcyhr
@Contact : aydcyhr@gmail.com
'''

#import pandas as pd
import xlrd as xl
import csv
import os

def to_xls(path):
	xls_file = xl.open_workbook(path)
	xls_sheet = xls_file.sheets()[0]
	col_value = xls_sheet.col_values(0)
	return col_value

def to_csv(path):
	csv_file = csv.reader(open(path,'r',encoding='utf-8'))
	csvdata = []
	for i in csv_file:
		csvdata.append(i)
	return csvdata

def to_txt(path):
	global ipcontent
	txtdata = open(path,'r')
	data = txtdata.readlines()
	txt_file = []
	for i in data:
		list1 = i.strip()
		txt_file.append(list1)
	return txt_file

def importfile(path):
	if "/" in path:
		houzhui =path.split(".")
		if houzhui[-1] =="txt":
			return to_txt(path)
		elif houzhui[-1] =="xls" or houzhui[-1] =="xlsx":
			return to_xls(path)
		elif houzhui[-1] == "csv":
			return to_csv(path)
		else:
			print("目前仅支持导入 xls , xlsx , csv , txt")
			exit()
	elif "\\" in path:
		houzhui =path.split(".")
		if houzhui[-1] =="txt":
			return to_txt(path)
		elif houzhui[-1] =="xls" or houzhui[-1] =="xlsx":
			return to_xls(path)
		elif houzhui[-1] == "csv":
			return to_csv(path)
		else:
			print("本程序目前仅支持导入 xls , xlsx , csv , txt")
			exit()
	else:
		print("请填写文件的绝对路径")
		exit()