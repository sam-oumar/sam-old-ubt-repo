import sqlite3


class Connection:
    def __init__(self, dbnames, cursor=""):
        self.dbnames = dbnames
        self.cursor = cursor

    def create_bd(self):
        with sqlite3.connect(self.dbnames) as con:
            self.cursor = con.cursor()

    def exe_statement(self, statement):
        self.cursor(statement)


c = Connection("bd_sam")
c.create_bd()
c.exe_statement("create table db_test(categorie text)")
