import random
n = int(input("Masukkan nilai N: "))
for i in range(n):
  random_number = random.random()
  print(f"data ke: {i + 1} => {random_number}")

print("Selesai")