from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()
print(type(iris.data))
print(iris.feature_names)
print(iris.target_names)

iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df["species"] = iris.target

print(iris_df.head())