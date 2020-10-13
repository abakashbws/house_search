import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets,linear_model
from matplotlib import style
style.use("ggplot")
from sklearn.cluster import KMeans

print("House Prices in lakhs = Computaional data * 10,000")
house_price = []
n = int(input("Enter number of houses under consideration:"))
for i in range(0,n):
    ele = int(input(" Enter house_prices in :"))
    house_price.append(ele)
print(house_price)
#If list of  price and area requirement is available put the i/p in the house_price & size
#house_price=[245,312,279,308,199,219]
#size=[1400,1600,1100,1800,1900,1550]
size = []
t = int(input("Enter number of different sizes to compute:"))
for j in range (0, t):
    sq = int(input("Enter size in sq foot:"))
    size.append(sq)
print(size)

mat_x = list(zip(house_price, size))
print(mat_x)

size2=np.array(size).reshape((-1,1))
regr=linear_model.LinearRegression()
regr.fit(size2,house_price)

print("Coefficient: \n",regr.coef_)
print("Intercept: \n",regr.intercept_)

size_new=int(input("Enter desired size in square foot:"))

price=(size_new*regr.coef_)+regr.intercept_

print(price)
house_price.append(price)
size.append(size_new)

#print(size)

plt.scatter(size, house_price)
plt.show()

kmeans = KMeans(n_clusters= 2)
kmeans.fit(mat_x)
centroids = kmeans.cluster_centers_
labels = kmeans.labels_
print("centroids \n",centroids)
print("labels \n", labels)

def graph(formula,x_range):
 x=np.array(x_range)
 y=eval(formula)
 plt.plot(x,y)
graph('regr.coef_*x+regr.intercept_',range(1000,2500))
plt.scatter(size,house_price,color='black')
plt.ylabel('House price')
plt.xlabel('size')
plt.show()

