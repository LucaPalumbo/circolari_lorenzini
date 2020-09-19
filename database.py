#!/usr/bin/env python
import mysql.connector
from mysql.connector import Error

class dbmanage:
    # Constructor
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(host='localhost', database='LorenziniCircular', user='root', password='manjaro')
        except:
            print("Error while connecting to DB")
            print("DB connection closed")

    # add circular object to database
    def addCircular(self,circular):
        query = "INSERT INTO circular VALUES (%s, %s, %s, %s);"
        datas = (circular.id, circular.name, circular.date, circular.link)
        try:
            self.cursor = self.connection.cursor(prepared=True)
            self.cursor.execute(query, datas)
            print("INSERT executed")
            self.connection.commit()
        except:
            print("Error occurred while trying to executing INSERT query (addCirular)")
            pass
        finally:
            self.cursor.close()

    # check if circular with specific id is in database already
    def checkCircular(self,circular):
        query = "SELECT id, name, data, link FROM circular WHERE id=%s;"
        data = (circular.id ,)
        try:
            self.cursor = self.connection.cursor(prepared=True)
            self.cursor.execute(query, data)
            records = self.cursor.fetchall()
            self.connection.commit()
            print("SELECT executed")
            self.cursor.close()
            if(len(records) != 0 ):
                return True
            else:
                return False
            
        except:
            print("Error occurred while trying to executing SELECT query (checkCircular)")
            self.cursor.close()
        
    # check if chat is in database already 
    def checkChat(self, chat):
        query = "SELECT id, type, title FROM chat WHERE id=%s;"
        data = (chat.id ,)
        try:
            self.cursor = self.connection.cursor(prepared=True)
            self.cursor.execute(query, data)
            records = self.cursor.fetchall()
            self.connection.commit()
            print("SELECT executed")
            self.cursor.close()
            if(len(records) != 0 ):
                return True
            else:
                return False
        except:
            print("Error occurred while trying to executing SELECT query (checkChat)")
            self.cursor.close()

    # add chat to database
    def addChat(self, chat):
        query = "INSERT INTO chat VALUES (%s, %s, %s);"
        datas = (chat.id, chat.type, chat.title)
        try:
            self.cursor = self.connection.cursor(prepared=True)
            self.cursor.execute(query, datas)
            print("INSERT executed")
            self.connection.commit()
        except:
            print("Error occurred while trying to executing INSERT query (addChat)")
            pass
        finally:
            self.cursor.close()
    
    def getChats(self):
        query = "SELECT id, type, title FROM chat"
        try:
            self.cursor = self.connection.cursor(prepared=True)
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            self.connection.commit()
            print("SELECT executed")
            self.cursor.close()
            if(len(records) != 0 ):
                return records
            else:
                return [-1]
        except:
            print("Error occurred while trying to executing SELECT query (checkChat)")
            self.cursor.close()

    #close database connection
    def close(self):   
        if self.connection.is_connected():
            self.connection.close()

