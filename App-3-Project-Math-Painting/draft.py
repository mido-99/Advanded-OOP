import numpy as np
from PIL import Image
'''NumPy reexplained with pillow basics'''

# Create an array (matrix) of numbers
# arr2 = np.array([[[1, 2, 3], [4, 5 ,6], [7, 8, 9]]], dtype=np.uint8)
# arr3 = np.ones(shape=(50, 50, 3), dtype=np.uint8)
arr1 = np.zeros(shape=(50, 50, 3), dtype=np.uint8)

# Modify values of the matrix
arr1[:] = (0, 250, 0)
print(arr1)

# Convert the matrix to an image
img = Image.fromarray(arr1)
img.show()
img.save('files\\test.png')