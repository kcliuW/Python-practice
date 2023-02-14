city = ['東京', '名古屋', '大阪', '京都', '福岡']
max_temp = [32, 28, 27, 26, 27]
min_temp = [25, 21, 20, 19, 22]
print("都市資料為:", city, ".")
print("最高氣溫為:", max_temp, ".")
print("最低氣溫為:", min_temp, ".")

for c, max, min in zip(city, max_temp, min_temp):
    print(c, "最高氣溫為", max, "最低氣溫為", min, "." )