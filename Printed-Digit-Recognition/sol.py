#!/usr/bin/env python

import numpy as np
import csv
import matplotlib
import matplotlib.pyplot as plt

# Grab Values from CSV (1's and 0's representing the digits)
feature_set = np.array(list(csv.reader(open("digits.csv", "rt"), delimiter=","))).astype("int")

# Stores the Numerical Values (0 - 9)
labels = np.array([[1,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,0,0], [0,0,1,0,0,0,0,0,0,0], [0,0,0,1,0,0,0,0,0,0], [0,0,0,0,1,0,0,0,0,0], 
                  [0,0,0,0,0,1,0,0,0,0], [0,0,0,0,0,0,1,0,0,0], [0,0,0,0,0,0,0,1,0,0], [0,0,0,0,0,0,0,0,1,0], [0,0,0,0,0,0,0,0,0,1]])

np.random.seed(42)  
weights = np.random.uniform(low=(0), high=(2/45), size=(45,10))  
bias = np.random.rand(10)  
lr = 0.1

def sigmoid(x):  
    return 1/(1 + np.exp(-x))

def sigmoid_der(x):  
    return sigmoid(x) * (1 - sigmoid(x))

if __name__ == "__main__":
    epochs = []
    errors = []

    for epoch in range(50):  
        inputs = feature_set

        # feedforward step1
        XW = np.dot(feature_set, weights) + bias

        #feedforward step2
        z = sigmoid(XW)


        # backpropagation step 1
        error = z - labels

        print(error.sum())

        # backpropagation step 2
        dcost_dpred = error
        dpred_dz = sigmoid_der(z)

        z_delta = dcost_dpred * dpred_dz

        inputs = feature_set.T
        weights -= lr * np.dot(inputs, z_delta)

        for num in z_delta:
            bias -= lr * num
            
        epochs.append(epoch)
        errors.append(error.sum())

    ax = plt.subplot()
    ax.plot(epochs, errors)

    ax.set(xlabel='Epochs', ylabel='Errors',
        title='Sum of Squared Errors vs Epochs')
    ax.grid()
    plt.show()

    #test for digit 0
    single_point = feature_set[9]  
    result = sigmoid(np.dot(single_point, weights) + bias)  
    print(result) 