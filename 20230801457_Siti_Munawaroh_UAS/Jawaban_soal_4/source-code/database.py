import sqlite3

# Membuat koneksi ke database SQLite
conn = sqlite3.connect('example.db')
cur = conn.cursor()

# Membuat tabel baru jika belum ada
cur.execute('''
CREATE TABLE IF NOT EXISTS Users (
    UserID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Email TEXT NOT NULL UNIQUE,
    DateOfBirth TEXT
)
''')
conn.commit()

# Menambahkan data
cur.execute('''
INSERT INTO Users (Name, Email, DateOfBirth)
VALUES (?, ?, ?)
''', ('Alice Smith', 'alice@gmail.com', '1990-05-12'))
conn.commit()

# Mengambil data
cur.execute('SELECT * FROM Users')
rows = cur.fetchall()

# Menampilkan data
for row in rows:
    print(row)

# Menutup koneksi
conn.close()
