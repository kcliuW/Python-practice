from decimal import Decimal
import math
import cmath

num = 0.1 + 0.2
print('0.1 + 0.2 =', num)
# 0.1 + 0.2 = 0.30000000000000004
# 這是因為浮點數的精度問題，Python 中的浮點數是基於二進制表示的，而某些十進制數字在二進制中無法精確表示。
# 為了解決這個問題，可以使用 Decimal 類來進行精確的十進制計算。
num_decimal = Decimal('0.1') + Decimal('0.2')
print('Decimal(0.1) + Decimal(0.2) =', num_decimal)
# Decimal(0.1) + Decimal(0.2) = 0.3
# Decimal 類提供了更高的精度，適合需要精確計算的場合。
# 這樣可以避免浮點數精度問題。
# 另外，Python 3.6 以後也可以使用 f-string 來格式化輸出。
num = 0.1 + 0.2
print(f'0.1 + 0.2 = {num:.2f}')
# 0.1 + 0.2 = 0.30
# 使用 f-string 可以指定小數點後的位數，這樣可以更好地控制輸出格式。
# 這樣的輸出方式在處理財務數據或其他需要精確表示的小數時非常有用。
# 另外，Python 也提供了 format 函數來格式化輸出。
num = 0.1 + 0.2
print('0.1 + 0.2 = {:.2f}'.format(num))
# 0.1 + 0.2 = 0.30
# 使用 format 函數也可以達到同樣的效果，這樣可以在 Python 2 和 Python 3 中都能使用。
# 總結：在 Python 中處理浮點數時，應該注意浮點數的精度問題，特別是在需要精確計算的場合。
# 使用 Decimal 類可以避免浮點數精度問題，並且可以使用 f-string 或 format 函數來格式化輸出。
# 這樣可以更好地控制輸出格式，特別是在處理財務數據或其他需要精確表示的小數時。
# 另外，Python 也提供了 round 函數來進行四捨五入。
num = 0.1 + 0.2
print('四捨五入到小數點後兩位:', round(num, 2))
# 四捨五入到小數點後兩位: 0.3
# 使用 round 函數可以將浮點數四捨五入到指定的小數位數，這樣可以更好地控制輸出格式。
# 這樣的輸出方式在處理財務數據或其他需要精確表示的小數時非常有用。
# 另外，Python 也提供了 math 模組來進行數學計算。
num = 0.1 + 0.2
print('使用 math 模組的 round 函數:', math.ceil(num * 100) / 100)
# 使用 math 模組的 round 函數: 0.3
# math.ceil 函數可以將數字向上取整，這樣可以更好地控制輸出格式。
# 這樣的輸出方式在處理財務數據或其他需要精確表示的小數時非常有用。
# 總結：在 Python 中處理浮點數時，應該注意浮點數的精度問題，特別是在需要精確計算的場合。
# 使用 Decimal 類可以避免浮點數精度問題，並且可以使用 f-string 或 format 函數來格式化輸出。
# 這樣可以更好地控制輸出格式，特別是在處理財務數據或其他需要精確表示的小數時。  


print (complex (1, 2))  # 複數
print (complex (1, 2).real)  # 複數的實部
print (complex (1, 2).imag)  # 複數的虛部
print (complex (1, 2).conjugate())  # 複數的共軛
print (complex (1, 2) + complex (3, 4))  # 複數加法
print (complex (1, 2) - complex (3, 4))  # 複數減法
print (complex (1, 2) * complex (3, 4))  # 複數乘法
print (complex (1, 2) / complex (3, 4))  # 複數除法
print (complex (1, 2) ** 2)  # 複數平方
print (complex (1, 2) ** 0.5)  # 複數開平方
print (complex (1, 2) ** complex (3, 4))  # 複數冪
print (complex (1, 2) == complex (1, 2))  # 複數比較
print (complex (1, 2) != complex (3, 4))  # 複數不等比較
# Python 不支援複數的大小比較（<, >, <=, >=），會產生 TypeError
# print (complex (1, 2) < complex (3, 4))  # 複數小於比較
# print (complex (1, 2) > complex (3, 4))  # 複數大於比較
# print (complex (1, 2) <= complex (3, 4))  # 複數小於等於比較
# print (complex (1, 2) >= complex (3, 4))  # 複數大於等於比較
# 複數的絕對值
print(abs(complex(1, 2)))  # 複數的絕對值
# 複數的角度
print(math.atan2(complex(1, 2).imag, complex(1, 2).real))  # 複數的角度
print(cmath.polar(complex(1, 2)))  # 複數的極坐標表示
print(cmath.rect(2.23606797749979, 1.1071487177940904))  # 複數的極坐標表示轉換為直角坐標

