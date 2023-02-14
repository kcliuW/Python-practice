data = [
    ["東京", 32, 25],
    ["名古屋", 28, 21],
    ["大阪", 27, 20],
    ["京都", 26, 19],
    ["福岡", 27, 22]
]

print("現在的資料為:", data, ".")

for dat in data:
    print("各都市資料為", dat, ".")
    for d in dat:
        print(d, end ="\t")
    print()

print(data[0][0], "的最高氣溫為", data[0][1], "最高氣溫為", data[0][2], ".")
 