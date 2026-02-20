import matplotlib.pyplot as plt
import random 
data =[random .randint(1,30) for i in range (120)]
plt.hist(data,bins=15,color="red")
plt.title("data of histogram")
plt.show()