from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn import metrics

iris = load_iris()
iris_X = iris.data
iris_y = iris.target

train_X, test_X, train_y, test_y = train_test_split(iris_X, iris_y, test_size=0.3)

clf = tree.DecisionTreeClassifier(max_depth=3)
iris_clf = clf.fit(train_X, train_y)

test_y_predicted = iris_clf.predict(test_X)

print(test_y_predicted)

print(test_y)

accuracy = metrics.accuracy_score(test_y, test_y_predicted)
print("Accuracy: ", accuracy)

r = tree.export_text(iris_clf, feature_names=iris['feature_names'])
print(r)
