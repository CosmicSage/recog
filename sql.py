import sqlite3
con = sqlite3.connect('test.db')
cur = con.cursor()
# obama_time = 10000
# con.cursor().execute("UPDATE presence SET time_spent=? WHERE name = 'Obama' ", (f"{obama_time}s",))
# commit cur
# con.commit()
# con.close()
# cur.execute('''INSERT INTO presence(name, time_spent) VALUES("Gavin Newsom", "0s")''')
# for tit in cur.execute('''SELECT * FROM presence'''):
#     print(tit)
