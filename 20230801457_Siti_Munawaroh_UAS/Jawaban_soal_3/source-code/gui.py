import tkinter as tk

def greet():
    print("Hello, world!")

# Membuat jendela utama
window = tk.Tk()
window.title("Contoh GUI Sederhana")

# Membuat label
label = tk.Label(window, text="Selamat Datang di GUI dengan Tkinter!")
label.pack(pady=10)

# Membuat tombol
button = tk.Button(window, text="Klik Saya", command=greet)
button.pack(pady=10)

# Menjalankan aplikasi
window.mainloop()
