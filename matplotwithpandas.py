import pandas as pd 
import matplotlib.pyplot as plt

data = {
    "name":["sourabh","ram","shyam","mohan","shon"],
    "sales":[1200,1300,1100,1250,1000],
    "months":["jan","feb","mar","apr","may"] 
    
    
    }
df=pd.DataFrame(data)
print(df)

plt.bar(df["name"],df["sales"],color="orange")
plt.title("sales month data ")
plt.xlabel("months")
plt.ylabel("sales")
plt.show()