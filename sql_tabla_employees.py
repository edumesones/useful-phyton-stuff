# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 11:27:44 2021

@author: egzlz
"""

import pymysql
import pandas as pd

database_host="relational.fit.cvut.cz"
username="guest"
password="relational"
database_name="employee"

db=pymysql.connect(host=database_host,user=username,password=password,database=database_name) 
query="SHOW TABLES"
a=pd.read_sql(query,db)
query1="""
SELECT * FROM employees
LIMIT 10
"""
b=pd.read_sql(query1,db)
query2="""
SELECT * FROM titles
LIMIT 10
"""
c=pd.read_sql(query2,db)
query4="""
SELECT * FROM salaries
LIMIT 10
"""
d=pd.read_sql(query4,db)
#vamos a ver si hay equilibrio entre salario mujeres y hombres
query="""
SELECT title,gender,min(salary),max(salary)


FROM employees emp
JOIN titles tit
ON emp.emp_no=tit.emp_no
JOIN salaries sal
ON emp.emp_no=sal.emp_no
WHERE sal.to_date="9999-01-01"
GROUP BY title,gender

"""
salarios=pd.read_sql(query,db)
#el where para el salario mas actual