# kod som merger olika databser till en

import sqlite3
import pandas as pd
import glob

path = r"mappen"


conn = sqlite3.connect('MERGED.db')


all_files = glob.glob(path + "/*.db")


for file in all_files:
   
    current_conn = sqlite3.connect(file)
   
    df = pd.read_sql_query("SELECT * FROM table name", current_conn)
    
    df.to_sql("Total", conn, if_exists='append', index=False)
   
    current_conn.close()


conn.close()




