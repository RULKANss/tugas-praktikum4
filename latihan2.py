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
