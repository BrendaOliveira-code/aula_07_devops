import sqlite3

conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute('''CREATE TABLE teste (id integer, nome text not null)''')
c.execute("INSERT INTO teste VALUES (1, 'Thiago')")
c.execute("INSERT INTO teste VALUES (2, 'Kuma')")

c.execute('''SELECT * FROM teste''')

for row in c.fetchall():
    print(row)

conn.commit()
conn.close()