# coding=sjis

import openpyxl

class EntityInfo:

	system_name = ""
	subsystem_name = ""
	schema_name = ""
	logical_entity_name = ""
	physical_entity_name = ""
	author = ""
	created_date = ""
	update_date = ""
	tag = ""
	remark = ""

class ColumnInfo:

	no = 0
	logical_name = ""
	physical_name = ""
	data_type = ""
	not_null = ""
	default_value = ""
	remark = ""

class IndexInfo:

	no = 0
	index_name = ""
	column_name = ""
	unique = ""
	remark = ""

class RelationInfo:

	no = 0
	verb_phrase = ""
	column_name = ""
	ref_entity_name = ""
	ref_column_name = ""


class Entity:
	"""
	各エンティティのデータを格納するクラス
	"""
	def __init__(self, sheet):
		self.entity_info = EntityInfo()
		# set entity information
		self.entity_info.system_name = sheet["C2"].value
		self.entity_info.subsystem_name = sheet["C3"].value
		self.entity_info.schema_name = sheet["C4"].value
		self.entity_info.logical_entity_name = sheet["C5"].value
		self.entity_info.physical_entity_name = sheet["C6"].value
		self.entity_info.author = sheet["F2"].value
		self.entity_info.created_date = sheet["F3"].value
		self.entity_info.update_date = sheet["F4"].value
		self.entity_info.tag = sheet["F5"].value
		self.entity_info.remark = sheet["B8"].value

		row_index = 14

		# set column information
		self.column_infos = []
		while True:
			if sheet["A" + str(row_index)].value is None:
				row_index = row_index + 3
				break
			else:
				columninfo = ColumnInfo()
				columninfo.no = sheet["A" + str(row_index)].value
				columninfo.logical_name = sheet["B" + str(row_index)].value
				columninfo.physical_name = sheet["C" + str(row_index)].value
				columninfo.data_type = sheet["D" + str(row_index)].value
				columninfo.not_null = sheet["E" + str(row_index)].value
				columninfo.default_value = sheet["F" + str(row_index)].value
				columninfo.remark = sheet["G" + str(row_index)].value
				self.column_infos.append(columninfo)
				row_index = row_index + 1

		# set index information
		self.index_infos = []
		while True:
			if sheet["A" + str(row_index)].value is None:
				row_index = row_index + 3
				break
			else:
				indexinfo = IndexInfo()
				indexinfo.no = sheet["A" + str(row_index)].value
				indexinfo.index_name = sheet["B" + str(row_index)].value
				indexinfo.column_name = sheet["C" + str(row_index)].value
				indexinfo.unique = sheet["F" + str(row_index)].value
				indexinfo.remark = sheet["G" + str(row_index)].value
				self.index_infos.append(indexinfo)
				row_index = row_index + 1

		# set FK relation information
		self.fk_relation_infos = []
		while True:
			if sheet["A" + str(row_index)].value is None:
				row_index = row_index + 3
				break
			else:
				fkrealtioninfo = RelationInfo()
				fkrealtioninfo.no = sheet["A" + str(row_index)].value
				fkrealtioninfo.verb_phrase = sheet["B" + str(row_index)].value
				fkrealtioninfo.column_name = sheet["C" + str(row_index)].value
				fkrealtioninfo.ref_entity_name = sheet["E" + str(row_index)].value
				fkrealtioninfo.ref_column_name = sheet["G" + str(row_index)].value
				self.fk_relation_infos.append(fkrealtioninfo)
				row_index = row_index + 1

		# set PK ralation information
		self.pk_relation_infos = []
		while True:
			if sheet["A" + str(row_index)].value is None:
				break
			else:
				pkrealtioninfo = RelationInfo()
				pkrealtioninfo.no = sheet["A" + str(row_index)].value
				pkrealtioninfo.verb_phrase = sheet["B" + str(row_index)].value
				pkrealtioninfo.column_name = sheet["C" + str(row_index)].value
				pkrealtioninfo.ref_entity_name = sheet["E" + str(row_index)].value
				pkrealtioninfo.ref_column_name = sheet["G" + str(row_index)].value
				self.pk_relation_infos.append(pkrealtioninfo)
				row_index = row_index + 1
