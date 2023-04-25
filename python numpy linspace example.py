# Python numpy.linspace()用法及代碼示例

'''
參數：

-> start  : [optional] start of interval range. By default start = 0
-> stop   : end of interval range
-> restep : If True, return (samples, step). By deflut restep = False
-> num    : [int, optional] No. of samples to generate
-> dtype  : type of output array

返回：

-> ndarray
-> step : [float, optional], if restep = True

'''

# 代碼1：解釋linspace函數

# Python Programming illustrating 
# numpy.linspace method 
  
import numpy as geek 
  
# restep set to True 
print("B\n", geek.linspace(2.0, 3.0, num=5, retstep=True), "\n") 
  
# To evaluate sin() in long range  
x = geek.linspace(0, 2, 10) 
print("A\n", geek.sin(x))


# 代碼2：使用matplotlib模塊的numpy.linspace()的圖形表示-pylab

# Graphical Represenation of numpy.linspace() 
import numpy as geek 
import matplotlib.pyplot as plt
  
# Start = 0 
# End = 2 
# Samples to generate = 10 
x1 = geek.linspace(0, 2, 10, endpoint = False) 
y1 = geek.ones(10) 
  
plt.plot(x1, y1, '*') 
plt.xlim(-0.2, 1.8)
plt.show()

# 代碼3：使用pylab的numpy.linspace()的圖形表示

# Graphical Represenation of numpy.linspace() 
import numpy as geek 
import matplotlib.pyplot as plt
  
# Start = 0 
# End = 2 
# Samples to generate = 15 
x1 = geek.linspace(0, 2, 15, endpoint = True) 
y1 = geek.zeros(15) 
  
plt.plot(x1, y1, 'o') 
plt.xlim(-0.2, 2.1)
plt.show()