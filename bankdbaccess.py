# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 19:47:26 2023

@author: SWAMINATHAN
"""

from sqlite3 import*

from bankclass import*

class bankDB:
    def addrecord(self,e):
        conn=connect("bankdatabase.db")
        sql=f"""insert into Bankinfo values ('{e.acno}','{e.name}','{e.actp}','{e.dob}',
        '{e.gender}','{e.add}','{e.adh}','{e.nlty}','{e.info}')"""
        conn.execute(sql)
        conn.commit()
        conn.close()
        return
    
    def search(self, acn):
        conn=connect("bankdatabase.db")
        sql=f"Select * from Bankinfo where acno='{acn}'"
        cursor=conn.execute(sql)
        e=bankinfodbaccess()
        found=False
        
        for row in cursor:
            
            found=True
            e.acno=row[0]
            e.name=row[1]
            e.actp=row[2]
            e.dob=row[3]
            e.gender=row[4]
            e.add=row[5]
            e.adh=row[6]
            e.nlty=row[7]
            e.info=row[8]
        return found,e 

    def delrecord(self, acno ):
        conn=connect("bankdatabase.db")
        sql=f"delete from Bankinfo where acno='{acno}'"
        conn.execute(sql)
        conn.commit()
        conn.close()
        return
    
    def updaterecord(self, e):
        conn=connect("bankdatabase.db")
        sql=f""" update Bankinfo set name='{e.name}',acctp='{e.actp}',dob='{e.dob}',gen='{e.gender}',
        address='{e.add}',adhno='{e.adh}',nlty='{e.nlty}',info='{e.info}' where acno='{e.acno}'"""
        conn.execute(sql)
        conn.commit()
        conn.close()
        return