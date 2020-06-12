# coding=sjis

import openpyxl
import yaml

from entity import EntityInfo
from entity import ColumnInfo
from entity import IndexInfo
from entity import RelationInfo
from entity import Entity


class DefBook:
	"""
	エンティティ定義書（エクセルファイル）を読み込んで、各エンティティのデータを格納するクラス
	"""
	book = []
	sheetnames = []
	entities = []

	def __init__(self):

		with open('config.yml', encoding='utf-8') as file:
			config = yaml.safe_load(file)

			self.book = openpyxl.load_workbook(config['book_name'])
			self.sheetnames = self.book.sheetnames
			del self.sheetnames[0:3]

			for n in self.sheetnames:
				entity = Entity(self.book[n])
				self.entities.append(entity)
