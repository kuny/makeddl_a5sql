# coding=sjis

from defbook import EntityInfo
from defbook import ColumnInfo
from defbook import DefBook

import yaml
import os
import time

from progressbar import ProgressBar
import progressbar

class MakeDDL:
    """
    DDL言語を出力するクラス
    コンストラクタに開いたファイル引数で代入して、各処理（メソッド）を実行する。
    各処理はメソッドチェーンとして使用できる。
    """
    def __init__(self, f):
        self.f = f
        self.book = DefBook()

    def create_table(self):
        """
        CREATE TABLE文を書き出すメソッド
        """

        widgets = ['Create Table        : ', progressbar.Percentage(), ' (', progressbar.Counter(), ' of ', str(len(self.book.entities)) + ') ', progressbar.Bar(), ' ', progressbar.Timer(), ' ', progressbar.ETA(), ' ', ]
        
        pbar = ProgressBar(maxval=len(self.book.entities), widgets=widgets).start()
        s = 0
        for entity in self.book.entities:

            self.f.write("create table " + entity.entity_info.logical_entity_name + "(\n")
            i = 0

            for column in entity.column_infos:
                
                if i == 0:
                    self.f.write("  [" + column.physical_name + "] " + column.data_type + "\n")
                    i = i + 1
                else:
                    self.f.write("  , [" + column.physical_name + "] " + column.data_type + "\n")
                    #self.f.write("  , [" + column.physical_name + "] " + column.physical_name + "\n")
                    #self.f.write("  , [" + column.data_type + "] " + column.data_type + "\n")

            self.f.write("  , constraint [" + entity.entity_info.logical_entity_name + "_PKC] primary key (")
            i = 0
            for column in entity.column_infos:
                if column.not_null == "(PK)" or column.not_null == "Yes (PK)":
                    if i == 0:
                        self.f.write("[" + column.physical_name + "]")
                        i = i + 1
                    else:
                        self.f.write(",[" + column.physical_name + "]")
                #bar.update(p)
                #bar.finish()
                #p = p + 1

            self.f.write(")\n")
            self.f.write(") ;\n\n")
            
            s = s + 1
            time.sleep(0.1)
            pbar.update(s)

        return self

    def index(self):
        return self

    def foreign_key(self):
        """
        ALTER TABLE文(FOREIGN KEY)を書き出すメソッド
        """
        widgets = ['Alter Table (FK)    : ', progressbar.Percentage(), ' (', progressbar.Counter(), ' of ', str(len(self.book.entities)) + ') ', progressbar.Bar(), ' ', progressbar.Timer(), ' ', progressbar.ETA(), ' ', ]
        
        pbar = ProgressBar(maxval=len(self.book.entities), widgets=widgets).start()
        s = 0
        for entity in self.book.entities:
            i = 1

            for fk in entity.fk_relation_infos:

                self.f.write("alter table " + entity.entity_info.logical_entity_name + "\n")
                self.f.write("  add constraint " + entity.entity_info.logical_entity_name + "_FK" + str(i) + " foreign key (");
                j = 0
                for a in fk.column_name.split(","):
                    if j == 0:
                        self.f.write("[" + a + "]")
                        j = 1
                    else:
                        self.f.write(",[" + a + "]")

                self.f.write(") references " + fk.ref_entity_name + "(")
                j = 0
                for b in fk.ref_column_name.split(","):
                    if j == 0:
                        self.f.write("[" + b + "]")
                        j = 1
                    else:
                        self.f.write(",[" + b + "]")

                self.f.write(");\n\n")
                i = i + 1
            s = s + 1
            time.sleep(0.1)
            pbar.update(s)
        return self

    def description(self):
        """
        備考を設定するスクリプトを書き出すメソッド
        """
        widgets = ['Description         : ', progressbar.Percentage(), ' (', progressbar.Counter(), ' of ', str(len(self.book.entities)) + ') ', progressbar.Bar(), ' ', progressbar.Timer(), ' ', progressbar.ETA(), ' ', ]
        
        pbar = ProgressBar(maxval=len(self.book.entities), widgets=widgets).start()
        s = 0
        for entity in self.book.entities:

            if entity.entity_info.remark is None or entity.entity_info.remark == "":
                self.f.write("EXECUTE sp_addextendedproperty N'MS_Description', N'" + entity.entity_info.logical_entity_name + "', N'SCHEMA', N'dbo', N'TABLE', N'" + entity.entity_info.logical_entity_name + "', NULL, NULL;\n")
            else:
                self.f.write("EXECUTE sp_addextendedproperty N'MS_Description', N'" + entity.entity_info.logical_entity_name + ":" + entity.entity_info.remark + "', N'SCHEMA', N'dbo', N'TABLE', N'" + entity.entity_info.logical_entity_name + "', NULL, NULL;\n")

            for column in entity.column_infos:

                if column.remark is None or column.remark == "":
                    self.f.write("EXECUTE sp_addextendedproperty N'MS_Description', N'" + column.physical_name + "', N'SCHEMA', N'dbo', N'TABLE', N'" + entity.entity_info.logical_entity_name + "', N'COLUMN', N'" + column.physical_name + "';\n")
                else:
                    
                    self.f.write("EXECUTE sp_addextendedproperty N'MS_Description', N'" + column.physical_name + ":" + column.remark +"', N'SCHEMA', N'dbo', N'TABLE', N'" + entity.entity_info.logical_entity_name + "', N'COLUMN', N'" + column.physical_name + "';\n")

            self.f.write("\n")
            s = s + 1
            time.sleep(0.1)
            pbar.update(s)
        return self


if __name__ == '__main__':

    with open('config.yml', encoding='utf-8') as file:
        config = yaml.safe_load(file)

        if os.path.exists(config["output"]):
            os.remove(config["output"])

        with open(config["output"], mode='w') as f:
            MakeDDL(f) \
            .create_table() \
            .index() \
            .foreign_key() \
            .description()
