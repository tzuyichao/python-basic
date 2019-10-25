import tensorflow.compat.v1 as tf

x = tf.constant(
    [[
        [[1], [2], [3], [4]],
        [[4], [3], [2], [1]],
        [[5], [6], [7], [8]],
        [[8], [7], [6], [5]]
    ]], 
    dtype=tf.float32)
print(x)

x_ksize = [1, 2, 2, 1]
x_strides = [1, 2, 2, 1]
x_padding = 'VALID'

x_pool = tf.nn.max_pool(value=x, ksize=x_ksize, strides=x_strides, padding=x_padding)
print(x_pool)