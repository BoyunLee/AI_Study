import sqlite3
import os

directory = "C:\\data"
if not os.path.exists(directory):
    os.makedirs(directory)

conn = sqlite3.connect("C:\\data\\First.db") 
cur = conn.cursor()
conn.commit()
conn.close() 