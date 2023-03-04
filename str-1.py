str1='do your best what can you do'
s1 = str1.count("do",0) # 從 str1 字串索引 0 的位置開始搜尋
s2 = str1.count("o",0,20) # 搜尋 str1 從索引值 0 到索引值 20 的位置
print("{}\n [do] 出現 {} 次, [o] 出現 {} 次".format(str1,s1,s2))

word = "Happy New Year?"
w1 = word.strip("H?")
print(w1)