#!/usr/bin/env python
import mysql.connector
from mysql.connector import Error
import secrets
from date_parser import dateParser
from circular import Circular

class dbmanage:
    # Constructor
    def __init__(self):
        try:
           self.connection = mysql.connector.connect(host='localhost', database='Lorenzini', user='ubuntu', password=secrets.DB_PASSWORD)
        except:
            self.connection = None
            print("Error while connecting to DB")
            print("DB connection closed")

    #check id dbmanage is open correctly
    def isConnected(self):
        if(self.connection == None):
            return False
        return True

    # add circular object to database
    def addCircular(self,circular):
        query = "INSERT INTO Circolare VALUES (%s, %s, %s, %s);"
        datas = (circular.id, circular.name, dateParser(circular.date), circular.link)
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
        query = "SELECT * FROM Circolare WHERE id=%s;"
        data = (circular.id ,)
        try:
            self.cursor = self.connection.cursor(prepared=True)
            self.cursor.execute(query, data)
            records = self.cursor.fetchall()
            self.connection.commit()
            self.cursor.close()
            if(len(records) != 0 ):
                return True
            else:
                return False
            
        except:
            print("Error occurred while trying to executing SELECT query (checkCircular)")
            self.cursor.close()

    # get circular using id
    def getCircularFromId(self, circular_id):
        query = "SELECT * FROM Circolare WHERE id=%s;"
        data = (circular_id,)
        try:
            self.cursor = self.connection.cursor(prepared=True)
            self.cursor.execute(query, data)
            record = self.cursor.fetchall()
            self.connection.commit()
            self.cursor.close()
            if(len(record) != 0 ):
                id_ = record[0][0]
                name = record[0][1]
                date = record[0][2]
                link = record[0][3]
                circular = Circular(id_,name,date,link)
                return circular
            else:
                return False
        except:
            print("Error occurred while trying to executing SELECT query (getCircularFromId)")
            self.cursor.close()

    # check if chat is in database already 
    def checkChat(self, chat):
        query = "SELECT * FROM Chat WHERE id=%s;"
        data = (chat.id ,)
        try:
            self.cursor = self.connection.cursor(prepared=True)
            self.cursor.execute(query, data)
            records = self.cursor.fetchall()
            self.connection.commit()
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
        query = "INSERT INTO Chat VALUES (%s, %s, %s);"
        datas = (chat.id, chat.type, chat.title)
        try:
            self.cursor = self.connection.cursor(prepared=True)
            self.cursor.execute(query, datas)
            self.connection.commit()
        except:
            print("Error occurred while trying to executing INSERT query (addChat)")
            pass
        finally:
            self.cursor.close()
    
    def getChats(self):
        query = "SELECT * FROM Chat"
        try:
            self.cursor = self.connection.cursor(prepared=True)
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            self.connection.commit()
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
        if self.connection!= None and self.connection.is_connected():
            self.connection.close()

