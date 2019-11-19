import csv
import matplotlib.pyplot as plt
with open("Iris.csv",'r') as test_file :
	anchor = csv.reader(test_file)
	next(anchor)
	x = []
	y = []
	for line in anchor:
		if(len(line[1]) and len(line[2])):
			x.append(float(line[1]))
			#print(float(line[5]),float(line[6]))
			y.append(float(line[2]))
plt.scatter(x,y)
x_mean = sum(x)/len(x)
y_mean = sum(y)/len(y)
nu1 = 0
de1 = 0
for i in range(len(x)):
	nu1 += (x[i] - x_mean)*(y[i] - y_mean)
	de1 += (x[i] - x_mean)**2
b1 = nu1/de1
b0 = y_mean - b1*x_mean
print(b1,b0) 
y_r = []
for i in x:
	y_r.append(b0 + b1*i)
plt.plot(x,y_r)
plt.show()
