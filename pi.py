# -*- coding: utf-8 -*-
# Created on Mon Jun 22
import sys
import numpy as np

NUMBER_OF_SAMPLES = 1000000
NUMBER_OF_EPOCHS = 10
rng = np.random.default_rng()

# circle sits inside a square with side length 1
def random_circle(nos=1000):
    X = rng.random((nos,)) - 0.5
    Y = rng.random((nos,)) - 0.5
    # Z is diagonal and radius
    Z = np.sqrt(X*X + Y*Y)
    # radius must be <= 0.5
    mu = np.mean(Z <= 0.5)
    return mu*4

p_array = np.zeros(NUMBER_OF_EPOCHS)
for i in range(NUMBER_OF_EPOCHS):
    p_array[i] = random_circle(NUMBER_OF_SAMPLES)

# print(sys.version)
print("Estimated pi: ", p_array.mean())
print("pi: ", np.pi)


