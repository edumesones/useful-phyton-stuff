# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 12:12:37 2021

@author: egzlz
"""

import os
os.chdir(r"C:\Users\egzlz\OneDrive\Escritorio\MASTER\modulo2")
import json
import pandas as pd


f=open("data.json","r")
fichero=f.read()
info=json.loads(fichero)
for item in info:
    """
    son diccionarios para conseguir el valor hacerlo por su key y en corchetes
    """
    print("\r")
    print("nombre",item["nm"])
    print("Partido",item["pp"])
    print("Año",item["tm"])

id1=[]
presidente=[]
nombre=[]
partido=[]
tiempo=[]
for item in info:
    id1.append(item["id"])
    presidente.append(item["president"])
    nombre.append(item["nm"])
    partido.append(item["pp"])
    tiempo.append(item["tm"])
df=pd.DataFrame({"id_presidente":id1,"presidente":presidente,"nombre":nombre,"partido":partido,"tiempo":tiempo,"años":tiempo})
df.to_excel("listas_presidentes.xlsx",index=False)
"""
recomendacion ver json codebeautify para representar json como arbol,json viewer,cuando haya muchas concatenaciones àr asaber como llegar
a los archivos
"""
a=open("data2.json","r")
paso1=a.read()
cargado=json.loads(paso1)
a=cargado["person"]["children"][0]["children"][1]["name"] #me llega  a harry,visto en codebeatify