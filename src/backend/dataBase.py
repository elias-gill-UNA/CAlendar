import sqlite3
import time
import random

conn = sqlite3.connect('../dataBase.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS tabla1(palabraclave TEXT, valor REAL)")

def data_entry():
    c.execute("INSERT INTO tabla1 VALUES(1452549219,'2016-01-11 13:53:39','Python',6)")
    conn.commit()
    c.close()
    conn.close()

def dynamic_data_entry(i):
    keyword = f'Numero {i}'
    value = random.randrange(0,10)

    c.execute("INSERT INTO tabla1 (palabraclave, valor) VALUES (?, ?)",
              (keyword, value))
    conn.commit()

create_table()
for i in range(10):
    dynamic_data_entry(i)
    time.sleep(1)

def read_from_db():
    c.execute('SELECT * FROM tabla1')
    data = c.fetchall()
    print(data)
    for row in data:
        print(row)

read_from_db()

c.close
conn.close()

