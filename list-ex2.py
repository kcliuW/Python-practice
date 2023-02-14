test_score = [74, 85, 69, 77, 81]
print("測驗成績為:", test_score, ".")

print("升冪排序的結果為:",sorted(test_score), ".")
print("降冪排序的結果為:",sorted(test_score,reverse=True), ".")

test_score = [74, 85, 69, 77, 81]
s = [n for n in test_score if n >= 80]
print("80分以上有:",s, ".")
print("80分以上的人數有",len(s),"人.") 