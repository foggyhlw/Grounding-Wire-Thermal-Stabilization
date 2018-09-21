import sqlite3
conn = sqlite3.connect('wires.db')
cursor = conn.cursor()
cursor.execute("select * from wires where N= 'LGJ-240/30'")
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()
