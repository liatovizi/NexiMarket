import psycopg2

conn = psycopg2.connect(host='localhost', dbname='market', user='postgres', password='~~~~', port=5432)

cur = conn.cursor()

# cur.execute("""CREATE TABLE IF NOT EXISTS item(
#      id SERIAL PRIMARY KEY,
#     name VARCHAR(30) NOT NULL UNIQUE,
#     price INT NOT NULL,
#     barcode VARCHAR(12) NOT NULL UNIQUE,
#     description VARCHAR(104) NOT NULL UNIQUE
#
#     );
# """)

# cur.execute("""CREATE TABLE IF NOT EXISTS users(
#       id SERIAL PRIMARY KEY,
#      username VARCHAR(30) NOT NULL UNIQUE,
#      email_address VARCHAR(50) NOT NULL UNIQUE,
#      password_hash VARCHAR(60) NOT NULL,
#      budget INT NOT NULL default 1000
#      );
#  """)

cur.executemany('INSERT INTO item (id, name, price, barcode, description, owner) VALUES (%s, %s, %s, %s, %s, %s)', [
   (4, 'IPhone', 700, '894512299897', 'des', 1),
   (5, 'Laptopka', 1900,'123998473165', 'des2', 1),
   (6, 'Mouse', 150, '231912732846', 'description3', 1)
])

conn.commit()
cur.close()
conn.close()