import time

print("=== Pengingat Minum Air (Otomatis) ===")
interval = int(input("Masukkan interval pengingat (detik): "))
print(f"\nPengingat otomatis setiap {interval} detik. Tekan Ctrl+C untuk berhenti.\n")

counter = 1

while True:
    try:
        time.sleep(interval)
        print(f"\n[Pengingat {counter}] 💧 Ayo minum air! 💧\n")
        counter += 1

    except KeyboardInterrupt:
        print("\nProgram dihentikan.")
        break
