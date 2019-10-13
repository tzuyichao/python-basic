from keras.datasets import boston_housing

(train_data, train_targets), (test_data, test_targets) = boston_housing.load_data()

print("train data shape: {}".format(train_data.shape))
print("test data shape: {}".format(test_data.shape))
print(train_targets)
print(test_targets)