#=================20==================40==================60==================80
#                 Chinese-English Flashcard App. Database
#==============================================================================!
#Use SQLite to develop a database for the app.
#convention is to use all caps for SQL commands, normal otherwise.
#==============================================================================!
#       Modified:
#   15 March 2020
#       Authors:
#   Chris Zhang & Shane Flynn
#==============================================================================#
#               TO DO:
#pass in variables to the functions,
#Generate database from a file
#define paths for the database relative path to audiofile locations
#==============================================================================#
import sqlite3
from sys import argv
#==============================================================================#
conn=sqlite3.connect('english_chinese.db')             #database file connection
c=conn.cursor()                                  #cursor to execute SQL commands
#==============================================================================#
#                  Define Database table columns  and types
#==============================================================================#
def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS EC_table (
            card_id INTEGER, word_english TEXT, word_chinese TEXT, pinyin TEXT,
            tone INTEGER, audio_path TEXT
            )""")
#==============================================================================#
def data_entry():
    val0=0
    val1='often'
    val2='test'
    val3='o er'
    val4=13
    val5='my path'
    c.execute("""INSERT INTO EC_table (card_id, word_english, word_chinese,
    pinyin, tone, audio_path) VALUES (?,?,?,?,?,?)
                """,(val0, val1, val2, val3, val4, val5))
    conn.commit()
#==============================================================================#
#                                  Main                                        #
#==============================================================================#
new_table=True
new_data=True
if new_table==True:
    create_table()
if new_data==True:
    data_entry()
#==============================================================================#
c.execute("SELECT * FROM EC_table WHERE word_english='often'")
print(c.fetchone())
#==============================================================================#
c.close()
conn.close()
