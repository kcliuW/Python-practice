import my_module # 匯入自己建立的模組
e1, e2 = my_module.payment() # 呼叫自訂模組內的函數 , e1, e2 等於模組內傳回的兩個數值 
print("總銷售業績 {}, 應付獎金 {}".format(e1,e2))