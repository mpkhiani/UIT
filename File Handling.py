# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 15:57:00 2019

@author: Manoj Khiani
"""
"""
with open("Exception Handling.py") as fileObj:
    lines = fileObj.read()
    print (lines)
"""

with open("demo.txt","r+") as filOb:
    """filOb.write("\nI am Pakistani.\nI Love programming")
    """
    filOb.seek(0)
    content = filOb.readlines()
    print(content)