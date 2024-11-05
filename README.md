## Sistem perulangan data random
untuk mengetahui nilai random 


## deskripsi perulangan data random
siuhewihdihewifhi


## flowchart
![flowchart](/flowchart1.png)


## Kode program
```
import random
n = int(input("Masukkan nilai N: "))
for i in range(n):
  random_number = random.random()
  print(f"data ke: {i + 1} => {random_number}")

print("Selesai")
```


## out-put program
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

