import matplotlib.pyplot as plt
import csv

x=[]
y=[]

with open('plot.txt', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(str(row[0]))
        y.append(float(row[1]))


plt.plot(x,y, marker='o')

plt.title('Plot for Time taken by Algorithms')

plt.xlabel('Algorithm')
plt.ylabel('Time(sec)')

plt.show()


