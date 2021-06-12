import numpy as np
def sigmoid(x):
    return 1/(1+np.exp(-x))
inputs = np.array([0,0,1])
weights = np.array([10,0,-5])
outputs = sigmoid(np.dot(inputs, weights))
print(outputs)