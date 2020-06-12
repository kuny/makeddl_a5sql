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
	�G���e�B�e�B��`���i�G�N�Z���t�@�C���j��ǂݍ���ŁA�e�G���e�B�e�B�̃f�[�^���i�[����N���X
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
