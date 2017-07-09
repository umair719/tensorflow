# House_Price_Prediction.py
# This is a very simple prediction of house prices based on house size
# implemented in TensorFlow.

import tensorflow as tf
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# generate some house sizes between 1000 and 3500 (typical sq ft of house)

num_house = 160
np.random.seed(42)
house_size = np.random.randint(low=1000, high=3500, size=num_house)

# generate house prices from house dize qith a random noise added.
np.random.seed(42)
house_price = house_size * 100.0 + np.random.randint(low=2000, high=7000, size=num_house)

# Plot generated house and size
plt.plot(house_size, house_price, "bx") # bx = blue x
plt.ylabel("Price")
plt.xlabel("Size")
plt.show()
