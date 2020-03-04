import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv('../data/iris/iris.csv', header=1, names=['id', 'sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])

print(iris.head())

fig, ax = plt.subplots()

ax.scatter(iris['sepal_length'], iris['sepal_width'])
ax.set_title('Iris Dataset')
ax.set_xlabel('sepal_length')
ax.set_ylabel('sepal_width')

plt.show()