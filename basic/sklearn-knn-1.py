import numpy as np
import matplotlib.pyplot as plt

x_train = np.array([
 [158, 64],
 [170, 86],
 [183, 84],
 [191, 80],
 [155, 49],
 [163, 59],
 [180, 67],
 [158, 54],
 [170, 67]])
y_train = ['male', 'male', 'male', 'male', 'female', 'female', 'female', 'female', 'female']

plt.figure()
plt.title('Human Heights and Weights by sex')
plt.xlabel('Height in cm')
plt.ylabel('Weight in kg')

for i, x in enumerate(x_train):
    plt.scatter(x[0], x[1], c='k', marker='x' if y_train[i] == 'male' else 'D')

plt.grid(True)
plt.show()

x = np.array([[155, 70]])
distance = np.sqrt(np.sum((x_train - x)**2, axis=1))
print(distance)
print(distance.argsort())

nearest_neighbor_indices = distance.argsort()[:3]
nearest_neighbor_genders = np.take(y_train, nearest_neighbor_indices)
print(nearest_neighbor_genders)

from collections import Counter
b = Counter(nearest_neighbor_genders)
print(b)
print(b.most_common(1)[0][0])

from sklearn.preprocessing import LabelBinarizer
from sklearn.neighbors import KNeighborsClassifier

lb = LabelBinarizer()
y_train_binarized = lb.fit_transform(y_train)
print(y_train_binarized)
print(y_train_binarized.reshape(-1))

K = 3
clf = KNeighborsClassifier(n_neighbors=K)
clf.fit(x_train, y_train_binarized.reshape(-1))
predicted_binaried = clf.predict(np.array([155, 70]).reshape(1, -1))[0]
predicted_label = lb.inverse_transform(predicted_binaried)
print(predicted_label)