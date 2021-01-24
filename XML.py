# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 12:17:57 2021

@author: egzlz
"""

"""
no tiene porque estar identado
"""
import os
os.chdir(r"C:\Users\egzlz\OneDrive\Escritorio\MASTER\modulo2")
import xml.etree.ElementTree as ET

tree=ET.parse("cd_catalog.xml")
raiz=tree.getroot()
for elem in raiz.iter():
    print(elem.tag)
for hijo in raiz:
    print(hijo.tag,hijo.attrib)
"""
numero registro xml
"""
numero=tree.findall("CD")
print("numero de registros",len(numero))
for item in numero:
    print("\n")
    print("Id",item.attrib["id"]) #es un diccionario
    print("Titulo",item.find("TITLE").text)
    print("Artista:",item.find("ARTIST").text)
    print("precio:",item.find("PRICE").text)