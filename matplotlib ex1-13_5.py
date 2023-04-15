# ch1_13.py
import matplotlib.pyplot as plt

Benz = [3367, 4120, 5539]
BMW = [4000, 3590, 4423]
Lexus = [5200, 4930, 5350]

seq = [2021, 2022, 2023]
plt.xticks(seq)
plt.plot(seq, Benz, '-*', label='Benz')
plt.plot(seq, BMW, '-o', label='BMW')
plt.plot(seq, Lexus, '-^', label='Lexus')
plt.legend(loc='upper left', bbox_to_anchor=(1,1))
plt.tight_layout(pad=2.5)
plt.text(2021,4500, 'Deepen Your Mind')
plt.title("Sales Report", fontsize=24)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Number of Sales", fontsize=14)
plt.tick_params(axis='both', labelsize=12, color='red')
plt.show()