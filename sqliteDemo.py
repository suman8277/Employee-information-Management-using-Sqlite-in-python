import sqlite3
class MyDatabase():

    def __init__(self, dbname):
        self.db = sqlite3.connect(dbname)
        if self.db != None:
            print('Database create')

    def create_table(self):
        query = "create table if not exists stud (id integer primary key autoincrement ,name varchar,number text not null);"
        self.db.execute(query)
        print('table created successfully')

    def insert_data(self,name,number):
        query = "insert into stud (name , number) values ('{}','{}');".format(name, number)
        self.db.execute(query)
        self.db.commit()

    def delete_data(self,id):
        query="delete from stud where id={};".format(id)
        self.db.execute(query)
        self.db.commit()



    def select_data(self):
        query = "select * from stud"
        rows = self.db.execute(query)
        for row in rows:
            print(row)

    def update_number(self,number,id):
        sql_update_query = f""" Update stud set name={number} where id={id}; """
        self.db.execute(sql_update_query)
        self.db.commit()
        print('record update successfully')

    def update_name(self,name, id):
        sql_update_query = f""" Update stud set name='{name}' where id='{id}';"""
        self.db.execute(sql_update_query)
        self.db.commit()
        print('record update successfully')


    # def updateSqliteTable(self):
    #     # sqliteConnection = sqlite3.connect('studentinfo.db')
    #     # cursor = sqliteConnection.cursor()
    #     # print('connected to sqlite')
    #
    #     sql_update_query = """ Update stud set name='pruthvi' where id='1' """
    #     self.db.execute(sql_update_query)
    #     self.db.commit()
    #     print('record update successfully')

