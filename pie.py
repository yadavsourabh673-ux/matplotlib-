# data 
import matplotlib.pyplot as plt
categories=["a","b","c","d","e"]
sales=[10,20,23,34,54]
plt.pie(sales,labels=categories,autopct="%1.1f%%")
plt.title("sales data ")
plt.show()