
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 18:34:06 2023

@author: Admin
"""


from sqlite3 import *

class bankinfodbaccess:
     
    def binfo(self,acno,name,actp,dob,gender,add,adh,nlty,info):
        self.acno=acno
        self.name=name
        self.actp=actp
        self.dob=dob
        self.gender=gender
        self.add=add
        self.adh=adh
        self.nlty=nlty
        self.info=info
   
