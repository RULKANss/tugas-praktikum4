# Initial balance
saldo = 1000000  # Rp 1,000,000

# Start ATM loop
while True:
    print(f"\nSaldo saat ini: Rp {saldo}")
    print("1. Tarik Uang")
    print("2. Keluar")
    pilihan = input("Pilih menu (1/2): ")

    if pilihan == "1":
        # Withdraw money
        jumlah = int(input("Masukkan jumlah penarikan: "))
        if jumlah <= saldo:
            saldo -= jumlah
            print("Penarikan berhasil!")
        else:
            print("Saldo tidak mencukupi!")
    
    elif pilihan == "2":
        # Exit
        print("Terima kasih telah menggunakan ATM!")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.")
