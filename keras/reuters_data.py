from keras.datasets import reuters

(train_data, train_labels), (test_data, test_labels) = reuters.load_data(num_words=10000)

print("train data: {}".format(len(train_data)))
print("test data: {}".format(len(test_data)))

print(train_data[5])

# word -> index 
word_index = reuters.get_word_index()
# print(word_index)
reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])
# print(reverse_word_index)
print(reverse_word_index.get(0))
print(reverse_word_index.get(1))
print(reverse_word_index.get(2))
print(reverse_word_index.get(3))
decoded_news = ' '.join([reverse_word_index.get(i-3, '?') for i in train_data[5]])
print(decoded_news)