# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 11:44:12 2021

@author: egzlz
"""

import sqlite3
import pandas as pd

conn=sqlite3.connect("my_database.sqlite") #se crea base de datos
cursor=conn.cursor()
cursor.execute("DROP TABLE IF EXISTS SCHOOL")
cursor.execute('''CREATE TABLE SCHOOL
(ID INT PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
AGE INT NOT NULL,
CITY CHAR(50),
MARKS INT
);
''')
cursor.execute("INSERT INTO SCHOOL (ID,NAME,AGE,CITY,MARKS) VALUES (1,'LUIS',24,'MADRID',8)")     
cursor.execute("INSERT INTO SCHOOL (ID,NAME,AGE,CITY,MARKS) VALUES (2,'ANA',34,'BILBAO',9)")
cursor.execute("INSERT INTO SCHOOL (ID,NAME,AGE,CITY,MARKS) VALUES (3,'PEDRO',19,'SANTANDER',10)")
cursor.execute("INSERT INTO SCHOOL (ID,NAME,AGE,CITY,MARKS) VALUES (4,'MARTA',22,'MADRID',6)")
conn.commit()
a=pd.read_sql("SELECT* FROM SCHOOL",conn)