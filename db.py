import sqlite3
import bcrypt
from getpass import getpass

con = sqlite3.connect('C:/sqlite/Krinkle.db')

#Checks game against Steam code
def chk_game(code):
    dat = con.execute("SELECT * FROM GAMES WHERE ID="+str(code)+";")
    return dat

#Checks the database for a user
def chk_user():
    return

#Validates user password
def chk_pass():
    return
