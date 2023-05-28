import numpy as np
from PIL import Image

class Canvas:
    '''A Canvas object that will have shapes drawn on, then converted to an image'''
    
    def __init__(self, color, width=1000, height=600):
        self.color = color
        self.width = width
        self.height = height
        
        # Create the matrix and giving it a color
        self.arr = np.zeros((self.height, self.width, 3), dtype=np.uint8)    #*
        if self.color == "black":
            pass
        elif self.color == "white":
            self.arr[:] = (255, 255, 255)
        
    def make(self, filename='image.png'):        
        '''Convert this canvas array into an image'''
        img = Image.fromarray(self.arr)
        img.show()
        img.save(filename)

class Square:
    
    def __init__(self, x, y, length, color):
        self.x = x
        self.y = y
        self.length = length
        self.color = color
    
    def draw(self, canvas):
        '''Draw a square shape on a Canvas object'''
        canvas.arr[self.x: self.x + self.length, self.y: self.y + self.length] = self.color

class Rectangle:
    
    def __init__(self, x, y, length, width, color): 
        self.x = x
        self.y = y
        self.length = length
        self.width = width
        self.color = color
        
    def draw(self, canvas):
        '''Draw a rectangle shape on a Canvas object'''
        canvas.arr[self.y: self.y + self.width, self.x: self.x + self.length] = self.color #**


'''NumPy reexplained with pillow basics'''

"""# Create an array (matrix) of numbers
# arr2 = np.array([[[1, 2, 3], [4, 5 ,6], [7, 8, 9]]], dtype=np.uint8)
# arr3 = np.ones(shape=(50, 50, 3), dtype=np.uint8)
arr1 = np.zeros(shape=(400, 400, 3), dtype=np.uint8)

# Modify values of the matrix
arr1[1:100, 2:100] = (0, 250, 0)
print(arr1)

# Convert the matrix to an image
img = Image.fromarray(arr1)
img.show()
img.save('files\\test.png')"""