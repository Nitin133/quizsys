from django.db import models
import mysql.connector as c

con=c.connect(host="localhost",user="root",password="root",database="quizdata")
cur=con.cursor()

def getData():
    sql="select * from questiondata where id=1"
    cur.execute(sql)
    data=cur.fetchall()
    res=[]

    for row in data:
        d={}
        d["id"]=row[0]
        d["question"]=row[1]
        d["option1"]=row[2]
        d["option2"]=row[3]
        d["option3"]=row[4]
        d["option4"]=row[5]
        d["correctans"]=row[6]


        res.append(d)

    
    return res
def editques(id):
    sql="select * from questiondata where id='"+id+"'"
    cur.execute(sql)
    data=cur.fetchall()
#a=editques(3)
#print(a)

        

    



