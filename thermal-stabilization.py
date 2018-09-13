import sqlite3
conn = sqlite3.connect('wires.db')
cursor = conn.cursor()
cursor.execute('select W,S,n from wires')
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()
