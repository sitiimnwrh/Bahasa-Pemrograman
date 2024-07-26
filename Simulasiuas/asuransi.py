import sqlite3

class AsuransiKendaraan:
    def __init__(self, nama_pemilik, nomor_polisi, jenis_kendaraan, premi_asuransi):
        self.nama_pemilik = nama_pemilik
        self.nomor_polisi = nomor_polisi
        self.jenis_kendaraan = jenis_kendaraan
        self.premi_asuransi = premi_asuransi

    def tampilkan_info(self):
        print("\n=== Data Asuransi Kendaraan ===")
        print(f"Nama Pemilik     : {self.nama_pemilik}")
        print(f"Nomor Polisi     : {self.nomor_polisi}")
        print(f"Jenis Kendaraan  : {self.jenis_kendaraan}")
        print(f"Premi Asuransi   : Rp{self.premi_asuransi:.2f}")

def buat_tabel():
    conn = sqlite3.connect('asuransi_kendaraan.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS asuransi (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama_pemilik TEXT NOT NULL,
            nomor_polisi TEXT NOT NULL,
            jenis_kendaraan TEXT NOT NULL,
            premi_asuransi REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def simpan_asuransi(asuransi):
    conn = sqlite3.connect('asuransi_kendaraan.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO asuransi (nama_pemilik, nomor_polisi, jenis_kendaraan, premi_asuransi)
        VALUES (?, ?, ?, ?)
    ''', (asuransi.nama_pemilik, asuransi.nomor_polisi, asuransi.jenis_kendaraan, asuransi.premi_asuransi))
    conn.commit()
    conn.close()

def tampilkan_semua_asuransi():
    conn = sqlite3.connect('asuransi_kendaraan.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM asuransi')
    rows = cursor.fetchall()
    conn.close()
    
    if not rows:
        print("Tidak ada data asuransi kendaraan.")
        return
    
    print("\n=== Semua Data Asuransi Kendaraan ===")
    for row in rows:
        print(f"ID              : {row[0]}")
        print(f"Nama Pemilik    : {row[1]}")
        print(f"Nomor Polisi    : {row[2]}")
        print(f"Jenis Kendaraan : {row[3]}")
        print(f"Premi Asuransi  : Rp{row[4]:.2f}\n")

def tambah_asuransi():
    print("=== Input Data Asuransi Kendaraan ===")
    nama_pemilik = input("Nama Pemilik: ")
    nomor_polisi = input("Nomor Polisi: ")
    jenis_kendaraan = input("Jenis Kendaraan: ")
    premi_asuransi = float(input("Premi Asuransi (dalam Rupiah): "))
    
    return AsuransiKendaraan(nama_pemilik, nomor_polisi, jenis_kendaraan, premi_asuransi)
import sqlite3

class AsuransiKendaraan:
    def __init__(self, nama_pemilik, nomor_polisi, jenis_kendaraan, premi_asuransi):
        self.nama_pemilik = nama_pemilik
        self.nomor_polisi = nomor_polisi
        self.jenis_kendaraan = jenis_kendaraan
        self.premi_asuransi = premi_asuransi

    def tampilkan_info(self):
        print("\n=== Data Asuransi Kendaraan ===")
        print(f"Nama Pemilik     : {self.nama_pemilik}")
        print(f"Nomor Polisi     : {self.nomor_polisi}")
        print(f"Jenis Kendaraan  : {self.jenis_kendaraan}")
        print(f"Premi Asuransi   : Rp{self.premi_asuransi:.2f}")

def buat_tabel():
    conn = sqlite3.connect('asuransi_kendaraan.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS asuransi (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama_pemilik TEXT NOT NULL,
            nomor_polisi TEXT NOT NULL,
            jenis_kendaraan TEXT NOT NULL,
            premi_asuransi REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def simpan_asuransi(asuransi):
    conn = sqlite3.connect('asuransi_kendaraan.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO asuransi (nama_pemilik, nomor_polisi, jenis_kendaraan, premi_asuransi)
        VALUES (?, ?, ?, ?)
    ''', (asuransi.nama_pemilik, asuransi.nomor_polisi, asuransi.jenis_kendaraan, asuransi.premi_asuransi))
    conn.commit()
    conn.close()

def tampilkan_semua_asuransi():
    conn = sqlite3.connect('asuransi_kendaraan.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM asuransi')
    rows = cursor.fetchall()
    conn.close()
    
    if not rows:
        print("Tidak ada data asuransi kendaraan.")
        return
    
    print("\n=== Semua Data Asuransi Kendaraan ===")
    headers = ["ID", "Nama Pemilik", "Nomor Polisi", "Jenis Kendaraan", "Premi Asuransi"]
    print(f"{headers[0]:<5} | {headers[1]:<20} | {headers[2]:<15} | {headers[3]:<20} | {headers[4]:<15}")
    print("-" * 80)
    for row in rows:
        print(f"{row[0]:<5} | {row[1]:<20} | {row[2]:<15} | {row[3]:<20} | Rp{row[4]:<15.2f}")

def tambah_asuransi():
    print("=== Input Data Asuransi Kendaraan ===")
    nama_pemilik = input("Nama Pemilik: ")
    nomor_polisi = input("Nomor Polisi: ")
    jenis_kendaraan = input("Jenis Kendaraan: ")
    premi_asuransi = float(input("Premi Asuransi (dalam Rupiah): "))
    
    return AsuransiKendaraan(nama_pemilik, nomor_polisi, jenis_kendaraan, premi_asuransi)

def main():
    buat_tabel()
    
    while True:
        asuransi = tambah_asuransi()
        asuransi.tampilkan_info()
        simpan_asuransi(asuransi)
        
        lanjut = input("\nApakah Anda ingin menambahkan data asuransi lain? (y/n): ").strip().lower()
        if lanjut != 'y':
            break

    print("\nTerima kasih! Have a nice day :).")
    tampilkan_semua_asuransi()

if __name__ == "__main__":
    main()

def main():
    buat_tabel()
    
    while True:
        asuransi = tambah_asuransi()
        asuransi.tampilkan_info()
        simpan_asuransi(asuransi)
        
        lanjut = input("\nApakah Anda ingin menambahkan data asuransi lain? (y/n): ").strip().lower()
        if lanjut != 'y':
            break

    print("\nTerima kasih!  :).")
    tampilkan_semua_asuransi()

if __name__ == "__main__":
    main()
