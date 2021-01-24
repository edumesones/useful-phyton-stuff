# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 12:46:46 2021

@author: egzlz
"""

import os
os.chdir(r"C:\Users\egzlz\OneDrive\Escritorio\MASTER\modulo2")
text_file=open("mbox.txt","r")
lines=text_file.read()
import pandas as pd
"""
expresiones regulares
"""
import re 
"""
\S que sea algo diferente de un espacio en blanco,+ que haya uno o mas 
"""
patron="\S+@\S+"
extract=re.findall(patron,lines,flags=re.IGNORECASE)
"""
si hago esto me sale tipo < y eso no lo quiero 
""
modifico
"""
pattern="[a-z0-9]\S@\S*[a-z]"  #primer caracter letra o numero,texto,arroba,y ultimo caracter letra si o si
extraccion2=re.findall(pattern,lines,flags=re.IGNORECASE)
"""
ahora agrupo
"""
pattern2="([a-z0-9]\S*)@(\S*[a-z])"
extraccion3=re.findall(pattern2,lines,flags=re.IGNORECASE)
df=pd.DataFrame(extraccion3,columns=["Nombre","Dominio"])

