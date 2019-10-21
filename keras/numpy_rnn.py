import numpy as np

timesteps = 100
input_features = 32
output_features = 64

inputs = np.random.random((timesteps, input_features))

# print(inputs.shape)
# print(inputs)

state_t = np.zeros((output_features, ))
# print(state_t.shape)
# print(state_t)

W = np.random.random((output_features, input_features))
U = np.random.random((output_features, output_features))
b = np.random.random((output_features, ))

# print(W.shape)
# print(W)
# print(U.shape)
# print(U)
# print(b.shape)
# print(b)

successive_outputs = []
for input_t in inputs:
    output_t = np.tanh(np.dot(W, input_t) + np.dot(U, state_t) +b)
    successive_outputs.append(output_t)
    state_t = output_t

final_output_sequence = np.array(successive_outputs)
print(final_output_sequence.shape)
