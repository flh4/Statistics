import math 
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

class Stats:

	def __init__(self, data):
		self.data = data

	def mergeSort(self): 
	    if len(data) >1: 
	        mid = len(self.data)//2 #Finding the mid of the array 
	        L = self.data[:mid] # Dividing the array elements  
	        R = self.data[mid:] # into 2 halves 
	  
	        mergeSort(L) # Sorting the first half 
	        mergeSort(R) # Sorting the second half 
	  
	        i = j = k = 0
	          
	        # Copy data to temp arrays L[] and R[] 
	        while i < len(L) and j < len(R): 
	            if L[i] < R[j]: 
	                self.data[k] = L[i] 
	                i+=1
	            else: 
	                self.data[k] = R[j] 
	                j+=1
	            k+=1
	          
	        # Checking if any element was left 
	        while i < len(L): 
	            self.data[k] = L[i] 
	            i+=1
	            k+=1
	          
	        while j < len(R): 
	            self.data[k] = R[j] 
	            j+=1
	            k+=1
	      	

	def sort(self):
		mergeSort(self.data)

	def Userdata(self):
		self.data = []
		while True:
			x = input("Enter data: ")
			if x.isnumeric():
				data.append(int(x))
			else:
				break
		return data

	def frequency(self):
		d = {x:self.data.count(x) for x in self.data}
		for i in d:
			print(str(i)+":"+str(d[i]))

	def relativeFreq(self):
		totl = len(self.data)
		d = {x:self.data.count(x)/totl for x in self.data}
		for i in d:
			print(str(i)+":"+str(d[i]))



	def histogram(self, classes):
		n, bins, patches = plt.hist(self.data, classes, facecolor='blue', alpha=0.5)
		plt.show()

	def min(self):
		minimum = 1000000
		for i in self.data:
			if i < minimum:
				minimum = i
		return minimum


	def max(self):
		maximum = -10000
		for i in self.data:
			if i > maximum:
				maximum = i
		return maximum

	def rng(self):
		return max(self.data)-min(self.data)

	def mean(self):
		return sum(self.data) / len(self.data)


	def variance(self):
		s = 0
		n = len(self.data)
		for i in self.data:
			s += (i - mean(self.data))**2
		return s / (n - 1)

	def std_dev(self):
		return math.sqrt(variance(self.data))

	def x_minux_xbar(self):
		return [i - mean(self.data) for i in self.data]

	def five_num_summary(lst):
		return 0

	def estimate_coef(x, y): 
		# number of observations/points 
		n = np.size(x) 
	  
		# mean of x and y vector 
		m_x, m_y = np.mean(x), np.mean(y) 
	  
		# calculating cross-deviation and deviation about x 
		SS_xy = np.sum(y*x) - n*m_y*m_x 
		SS_xx = np.sum(x*x) - n*m_x*m_x 
	  
		# calculating regression coefficients 
		b_1 = SS_xy / SS_xx 
		b_0 = m_y - b_1*m_x 
	  
		return(b_0, b_1) 
	  
	def plot_regression_line(x, y, b): 
		# plotting the actual points as scatter plot 
		plt.scatter(x, y, color = "m", 
			marker = "o", s = 30) 
	  
		# predicted response vector 
		y_pred = b[0] + b[1]*x 
	  
		# plotting the regression line 
		plt.plot(x, y_pred, color = "g") 
	  
		# putting labels 
		plt.xlabel('x') 
		plt.ylabel('y') 
	  
		# function to show plot 
		plt.show() 
		

	def getSummary(self):
		print("n:",end=" ")		
		n = len(self.data)
		print(n)
		print("Sum:",end=" ")
		print(sum(self.data))
		print("Range:",end=" ")
		print(rng(self.data))
		print("Min:",end=" ")
		print(min(self.data))
		print("Max:",end=" ")
		print(max(self.data))
		print("Mean:",end=" ")
		print(mean(self.data))
		print("Variance:",end=" ")
		print(variance(self.data))
		print("Standard Deviation:",end=" ")
		print(stdev(self.data))
		
		c = mean(self.data) + stdev(self.data)
		twoS = 2 * stdev(self.data)
		print("Mean + S: "+str(c))


		
		sort(self.data)
		print(self.data)
		print()
		frequency(self.data)
		relativeFreq(self.data)
		histogram(self.data,7)

	

data_set = [1.03, 1.03, 1.06, 1.02, 1.03, 1.03, 1.03, 1.02, 1.03, 1.03, 
1.06, 1.04, 1.05, 1.03, 1.04, 1.03, 1.05, 1.06, 1.04, 1.04, 
1.03, 1.04, 1.04, 1.06, 1.03, 1.04, 1.05, 1.04, 1.04, 1.02,
1.03, 1.05, 1.05, 1.03, 1.04, 1.03, 1.04, 1.04, 1.03, 1.04,
1.03, 1.04, 1.04, 1.04, 1.05, 1.04, 1.04, 1.03, 1.03, 1.05,
1.04, 1.04, 1.05, 1.04, 1.03, 1.03, 1.05, 1.03, 1.04, 1.05,
1.04, 1.04, 1.04, 1.05, 1.03, 1.04, 1.04, 1.04, 1.04, 1.03,
1.05, 1.05, 1.05, 1.03, 1.04, 1.09, 1.08, 1.12, 1.10, 1.009]
d1 = Stats(data_set)

print(Stats.sort(d1))
		




