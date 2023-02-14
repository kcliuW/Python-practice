amount = int(input("請輸入將兌換金額: "))
hundred_note = amount//100
fifty_note = (amount-hundred_note * 100)//50
ten_dollar_note = (amount-hundred_note *100 - fifty_note * 50)//10
print("一百元紙幣有 %d 張, 五十元紙幣有 %d張, 十元紙幣有 %d張" %(hundred_note, fifty_note, ten_dollar_note))