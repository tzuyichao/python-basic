import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv('../data/iris/iris.csv', header=1, names=['id', 'sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])

print(iris.head())

colors = {'Iris-setosa':'r', 'Iris-versicolor':'g', 'Iris-virginica':'b'}

fig, ax = plt.subplots()

for i in range(len(iris['sepal_length'])):
    ax.scatter(iris['sepal_length'][i], iris['sepal_width'][i], color=colors[iris['class'][i]])

ax.set_title('Iris Dataset')
ax.set_xlabel('sepal_length')
ax.set_ylabel('sepal_width')

plt.show()