import matplotlib.pyplot as plt
import numpy as np
from random import randint
plt.rcParams["font.family"] = ["Microsoft JhengHei"]

def dice_generator(times, sides):
    ''' 處理隨機數''' 
    for i in range(times):
        ranNum = randint(1, sides)
        dice.append(ranNum)

times = 10000
sides = 6
dice = []
dice_generator(times, sides)

h = plt.hist(dice, sides)
print("bins的y軸 ",h[0])
print("bins的x軸 ",h[1])
plt.ylabel('頻率')
plt.title('測試 10000 次')
plt.show()