from sklearn.datasets import load_iris
from sklearn import tree
import matplotlib.pyplot as plt

X, y = load_iris(return_X_y=True)
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, y)

tree.plot_tree(clf, filled=True)
plt.show()
