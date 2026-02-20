import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [10, 20, 25, 30, 40]
y2 =[20,30,40,50,60]

plt.plot(x, y1,label="sales 2024")
plt.plot(x,y2,label="sles 2025")
plt.title("sales data")
plt.xlabel("months")
plt.ylabel("sale")
plt.legend()
plt.show()