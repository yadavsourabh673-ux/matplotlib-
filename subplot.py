import matplotlib.pyplot as plt
categories=["a","b","c","d","e"]
sales=[10,20,23,34,54]

x=[10,20,30,40,50]
y=[20,30,40,50,60]

plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.pie(sales,labels=categories,autopct="%1.1f%%")
plt.title("sales data ")

plt.subplot(1,2,2)
plt.scatter(x,y,color="purple")
plt.title("scatter plot graph ")
plt.xlabel("x axis sales ")
plt.ylabel("y axis categories")
plt.show()