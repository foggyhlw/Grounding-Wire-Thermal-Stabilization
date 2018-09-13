import pandas
import sqlite3,csv
index_label=['N','alS','ironS','S','d','R','A','E','Tp','W']
conn = sqlite3.connect('wires.db')
df = pandas.read_csv('wires.csv')
df.to_sql('wires',conn, if_exists='replace',index_label=index_label,index=False) 
print('done')
