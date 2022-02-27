from sqlite3 import *
import sqlite3
con = sqlite3.connect("data_base.db")

con.commit()
con.close()