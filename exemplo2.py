import sqlite3
conn = sqlite3.connect('example.db')

c = conn.cursor()


c.execute("SELECT * FROM stocks")

for row in c.fetchall():
    print(row)
    print('Data:',row[0])

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()