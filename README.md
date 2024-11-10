## flowchart
![flowchart](/flowchart1.png)


## sistem perulangan data random latihan 1
```
import random
n = int(input("Masukkan nilai N: "))
for i in range(n):
  random_number = random.random()
  print(f"data ke: {i + 1} => {random_number}")

print("Selesai")
```


## out-put program latihan 1
```
PS C:\pemrog> & C:/Users/Syahrul/AppData/Local/Microsoft/WindowsApps/python3.11.exe c:/pemrog/lat1.py
Masukkan nilai N: 11
data ke: 1 => 0.7579621240149477
data ke: 2 => 0.15424615316903212
data ke: 3 => 0.7810785283268161
data ke: 4 => 0.8169388633357298
data ke: 5 => 0.2950452590404994
data ke: 6 => 0.9026964771475103
data ke: 7 => 0.8308487317858666
data ke: 8 => 0.2623206593049592
data ke: 9 => 0.304385233325254
data ke: 10 => 0.5406667509321474
data ke: 11 => 0.5090862482598367
Selesai
```


## cara kerja program
- Import random: Program dimulai dengan mengimpor modul random. Modul ini berisi fungsi random() yang digunakan untuk menghasilkan bilangan acak.

- Masukan Nilai N: Program meminta pengguna untuk memasukkan nilai N, yang merupakan jumlah bilangan acak yang ingin dihasilkan.

- Loop for: Program menggunakan loop for untuk mengulangi N kali, sesuai dengan nilai yang dimasukkan pengguna.

- Generasi Bilangan Acak: Di dalam loop, program menggunakan fungsi random() untuk menghasilkan bilangan acak antara 0 dan 1 (bukan termasuk 1).

- Tampilan Hasil: Untuk setiap iterasi loop, program menampilkan bilangan acak yang dihasilkan, beserta nomor urut data.

- Selesai: Setelah loop selesai, program menampilkan pesan "Selesai", menunjukkan bahwa proses generasi bilangan acak sudah selesai.



## kode latihan 2
```
# Initial investment
modal_awal = 100000000  # 100 million

# Monthly profit initialization
laba_bulan = [0] * 8  # Initialize profit for each month

# Calculate profit for each month
for bulan in range(8):
    if bulan < 2:
        laba_bulan[bulan] = 0
    elif bulan == 2 or bulan == 3:
        laba_bulan[bulan] = modal_awal * 0.01
    elif bulan == 4 or bulan == 5:
        laba_bulan[bulan] = modal_awal * 0.05
    elif bulan == 6 or bulan == 7:
        laba_bulan[bulan] = modal_awal * 0.02
    elif bulan == 8:
        laba_bulan[bulan] = modal_awal * 0.03

# Print profit for each month and calculate the total profit
total_laba = 0
for bulan in range(8):
    print(f"Laba bulan ke-{bulan + 1} sebesar: {int(laba_bulan[bulan])}")
    total_laba += laba_bulan[bulan]

print(f"Total laba adalah: {int(total_laba)}")
```


## Flowchart
![flowchart}()


## out put program
```
PS C:\tugas membuat struk> & C:/Users/Syahrul/AppData/Local/Microsoft/WindowsApps/python3.11.exe "c:/tugas membuat struk/latihan2.py"
Laba bulan ke-1 sebesar: 0
Laba bulan ke-2 sebesar: 0
Laba bulan ke-3 sebesar: 1000000
Laba bulan ke-4 sebesar: 1000000
Laba bulan ke-5 sebesar: 5000000
Laba bulan ke-6 sebesar: 5000000
Laba bulan ke-7 sebesar: 2000000
Laba bulan ke-8 sebesar: 2000000
Total laba adalah: 16000000
PS C:\tugas membuat struk>
```


## cara kerja program
Program yang Anda berikan menghitung dan mencetak laba bulanan dari sebuah investasi awal selama 8 bulan. Berikut adalah kesimpulan cara kerja program tersebut:
- Inisialisasi Modal Awal: Program dimulai dengan mendefinisikan modal awal sebesar 100 juta (100000000).
- Inisialisasi Laba Bulanan: Sebuah list laba_bulan diinisialisasi dengan 8 elemen yang semuanya bernilai 0. List ini akan digunakan untuk menyimpan laba yang diperoleh setiap bulan.

Perhitungan Laba Bulanan:

- Program menggunakan loop for untuk iterasi dari bulan 0 hingga 7 (total 8 bulan).
- Untuk bulan 0 dan 1, laba ditetapkan sebagai 0.
- Untuk bulan 2 dan 3, laba ditetapkan sebesar 1% dari modal awal.
- Untuk bulan 4 dan 5, laba ditetapkan sebesar 5% dari modal awal.
- Untuk bulan 6 dan 7, laba ditetapkan sebesar 2% dari modal awal.
- Untuk bulan 8, laba ditetapkan sebesar 3% dari modal awal.
- Pencetakan Laba Bulanan: Setelah menghitung laba untuk setiap bulan, program mencetak laba yang diperoleh untuk setiap bulan dengan format yang jelas.

- Perhitungan Total Laba: Program juga menghitung total laba yang diperoleh selama 8 bulan dengan menjumlahkan semua laba bulanan dan mencetak total tersebut.

Contoh Output
- Jika program dijalankan, outputnya akan menunjukkan laba untuk setiap bulan dan total laba setelah 8 bulan.

Best Practices
- Gunakan nama variabel yang lebih deskriptif untuk meningkatkan keterbacaan kode.
- Pertimbangkan untuk menggunakan struktur data yang lebih fleksibel, seperti dictionary, jika persentase laba bervariasi lebih banyak di masa depan.
- Tambahkan komentar yang lebih mendetail untuk menjelaskan setiap bagian dari kode.



## kode latihan 3
```
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
```


## Flowchart latihan 3
![flowchart]()



## out put latihan 3
```
PS C:\tugas membuat struk> & C:/Users/Syahrul/AppData/Local/Microsoft/WindowsApps/python3.11.exe "c:/tugas membuat struk/latihan3.py"

Saldo saat ini: Rp 1000000
1. Tarik Uang
2. Keluar
Pilih menu (1/2): 1
Masukkan jumlah penarikan: 50000
Penarikan berhasil!

Saldo saat ini: Rp 950000
1. Tarik Uang
2. Keluar
Pilih menu (1/2): 2
Terima kasih telah menggunakan ATM!
PS C:\tugas membuat struk>
```


## cara kerja program
Program ATM yang disajikan adalah sebuah simulasi sederhana yang memungkinkan pengguna untuk mengelola saldo mereka dengan dua fungsi utama: menarik uang dan keluar dari program. Berikut adalah ringkasan cara kerja program ini:

Inisialisasi Saldo:
- Program dimulai dengan menetapkan saldo awal sebesar Rp 1.000.000, yang merupakan jumlah uang yang tersedia untuk ditarik oleh pengguna.
  
Loop Interaktif:

- Program menggunakan loop while True untuk menciptakan interaksi berkelanjutan dengan pengguna. Ini memungkinkan pengguna untuk melakukan beberapa transaksi tanpa harus memulai ulang program.

Menampilkan Informasi:

-Di setiap iterasi loop, program menampilkan saldo saat ini dan memberikan dua pilihan menu kepada pengguna:
- Tarik Uang
- Keluar
Pengolahan Pilihan Pengguna:

- Program menerima input dari pengguna untuk memilih menu. Berdasarkan pilihan yang dimasukkan, program melakukan tindakan berikut:
Tarik Uang:
- Jika pengguna memilih untuk menarik uang, program meminta jumlah yang ingin ditarik.
- Program memeriksa apakah jumlah yang diminta tidak melebihi saldo yang tersedia.
- Jika cukup, saldo akan dikurangi dengan jumlah yang ditarik, dan program mengonfirmasi bahwa penarikan berhasil.
- Jika tidak cukup, program memberikan peringatan bahwa saldo tidak mencukupi.
Keluar:
- Jika pengguna memilih untuk keluar, program mengucapkan terima kasih dan menghentikan loop, sehingga program berakhir.
Pilihan Tidak Valid:
- Jika pengguna memasukkan pilihan yang tidak valid, program memberikan umpan balik dan meminta pengguna untuk mencoba lagi.
Akhir Program:
- Program akan terus beroperasi hingga pengguna memilih untuk keluar. Setelah keluar, program selesai dan tidak ada lagi interaksi yang terjadi.
