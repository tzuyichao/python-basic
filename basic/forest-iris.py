from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

iris = load_iris()
iris_X = iris.data
iris_y = iris.target

train_X, test_X, train_y, test_y = train_test_split(iris_X, iris_y, test_size=0.3)

clf = RandomForestClassifier()
iris_clf = clf.fit(train_X, train_y)

test_y_predicted = iris_clf.predict(test_X)

print(test_y_predicted)
print(test_y)

accuracy = metrics.accuracy_score(test_y, test_y_predicted)
print('Accuracy: ', accuracy)

# https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_curve.html
# Note: this implementation is restricted to the binary classification task.
# multiclass format is not supported
# fpr, tpr, thresholds = metrics.roc_curve(test_y, test_y_predicted)
# auc = metrics.auc(fpr, tpr)
# print("AUC: ", auc)
