original = {"abase", "abate", "abdicate", "abhor", "abate", "acrid",
            "appoint", "abate", "kindle"}
print("單字收集的原始內容: ")
print(original)
set1 = set(original)
not_duplicated = list(set1)
print("刪除重複單字的最佳內容: ")
print(not_duplicated)
print("按照字母的排列順序: ")
not_duplicated.sort()
print(not_duplicated)