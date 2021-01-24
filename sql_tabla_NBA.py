# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 10:40:55 2021

@author: egzlz
"""

import pymysql

database_host="relational.fit.cvut.cz"
username="guest"
password="relational"
database_name="NBA"

db=pymysql.connect(host=database_host,user=username,password=password,database=database_name) 
cursor=db.cursor() #poder hacer operaciones
#sacar querys fetchone de la primera fila,fethall de todas
cursor.execute("SELECT * FROM Player")
cursor.fetchall()
cursor.execute("SHOW TABLES")
print(cursor.fetchall())

import pandas as pd
query="SHOW TABLES"
df=pd.read_sql(query,db)
#jugadores mas de 5 aisst en partdo
query="""
SELECT PlayerName,Assists


FROM Actions act
JOIN Player pla
ON act.PlayerID=pla.PlayerID
WHERE Assists>5
"""
asistencias5=pd.read_sql(query,db)
query2="""
SELECT SUM(Assists) as totalassists,PlayerName
FROM Actions act
JOIN Player pla
ON act.PlayerID=pla.PlayerID
GROUP BY PlayerName
ORDER BY SUM(Assists) DESC
LIMIT 10
"""
asistenciastop=pd.read_sql(query2,db)
#equipos con mas media de puntos
query3="""
SELECT TeamName,AVG(totalpoints) as avgpoints
FROM(
     SELECT TeamName,GameID,SUM(Points) as totalpoints



    FROM Actions act
    JOIN Team team
    ON act.TeamID=team.TeamID
    GROUP BY TeamName,GameID
    )T   
GROUP BY TeamName
ORDER BY avgpoints DESC
LIMIT 10
"""
#daba fallo y he añadido la T poruqe hay que darle un alias
puntos=pd.read_sql(query3,db)