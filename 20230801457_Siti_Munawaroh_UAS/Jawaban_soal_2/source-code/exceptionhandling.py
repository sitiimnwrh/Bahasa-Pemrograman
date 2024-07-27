try:
    # Kode yang mungkin menimbulkan pengecualian
    numerator = 10
    denominator = 0
    result = numerator / denominator
    print(f"Result: {result}")

except ZeroDivisionError:
    # Menangani kesalahan pembagian dengan nol
    print("Error: Division by zero is not allowed.")

except Exception as e:
    # Menangani semua jenis kesalahan lainnya
    print(f"An error occurred: {e}")

finally:
    # Kode yang selalu dijalankan
    print("Execution completed.")
