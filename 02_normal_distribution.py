import matplotlib.pyplot as plt
import numpy as np
import math
#Random input value
numberOfRandomValue = 1000
x = np.linspace(1,350,numberOfRandomValue)
i = 0
#Calculate mean
total = 0
for i in range(0, len(x)):
    total += x[i]
mean = total/len(x)

#Calculate standard deviation
deviation = [(val-mean)**2 for val in x]
variance = sum(deviation) / len(x)
std = math.sqrt(variance)


#Calculate ditribution value
PDF = []
for i in range(0, len(x)):
    pdf = (1/(std*math.sqrt(2*math.pi))) * math.exp(-0.5*(((x[i]-mean)/std)**2))
    PDF.append(pdf)

print(PDF)
print("-------------------------------")
plt.plot(x, PDF, color='red')
plt.show()

