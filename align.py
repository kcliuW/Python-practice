str1 = '淡泊以明志, 寧靜以致遠'
print('欄寬20, 字串置中', str1.center(20))
print('字串置中, # 填補', str1.center(20, '#'))
print('欄寬20, 字串靠左', str1.ljust(20, '@'))
print('欄寬20, 字串靠右', str1.rjust(20, '!'))

mobilephone = '931828736'
print('字串左側補 0:', mobilephone.zfill(10))

str2 = 'Time create hero., I love my family.'
print('以逗點分割字元', str2.partition(','))

str3 = '忠孝 \n 仁愛 \n 信義 \n 和平'
print('依\\n 分割字串', str3.splitlines(False))