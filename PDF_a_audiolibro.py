# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 20:57:00 2021

@author: egzlz
"""

import pyttsx3
import pdfplumber
import PyPDF2
import os
os.chdir(r"C:\Users\egzlz\OneDrive\Escritorio\MASTER")
"""
PASA QUE FUNCIONE TIENES QUE TENER EL ARCHIVO EN EL DIRECTORIO DE TRABAJO
"""

file="Padre-Rico-Padre-Pobre.pdf" #PAG 15
pdfobj=open(file,"rb")
pdfreader=PyPDF2.PdfFileReader(pdfobj)
pages=pdfreader.numPages

for i in range(14,15):
    page=pdfplumber.open(file).pages[i]
    text=page.extract_text()
    text= text.replace('\r', '').replace('\n', '')
    print(text)
  
speaker=pyttsx3.init()
#voices = speaker.getProperty('voices')
#speaker.setProperty(voices,id)
speaker.say(text)
speaker.save_to_file(text,'test.mp3')
speaker.runAndWait()
