Score = int(input("輸入學生的分數:"))
if Score > 100:
    print("輸入的分數超過 100.")
else: 
    if Score < 0:
        print( "怎麼會有負的分數??")
    else:
        if Score >= 60:
            print("得到 %d 分, 還不錯唷..." %Score)
        else:
            print("不太理想喔..., 只考了 %d 分" %Score)