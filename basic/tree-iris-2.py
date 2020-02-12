from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_text

iris = load_iris()
decisionTreeClassifier = DecisionTreeClassifier(random_state=0, max_depth=2)
decisionTreeClassifier = decisionTreeClassifier.fit(iris.data, iris.target)
r = export_text(decisionTreeClassifier, feature_names=iris['feature_names'])
print(r)
