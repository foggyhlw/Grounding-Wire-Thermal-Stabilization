import sqlite3
conn = sqlite3.connect('wires.db')
cursor = conn.cursor()
cursor.execute('select * from [导地线参数]')
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()