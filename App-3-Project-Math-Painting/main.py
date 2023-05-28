from my_funcs import confirm_no_empty_str, confirm_input_is_number
from utiility import Canvas, Square, Rectangle

### CLI app ###
canvas_color = confirm_no_empty_str("Hi! Let's draw some shapes on a canvas\nWhat background color do you prefer? (white/black) ")
canv = Canvas(canvas_color)

# User chooses what shapes do they want to draw

while True:
    want_to_draw = confirm_no_empty_str("Press q to quit.\nSo, what shape do you want to draw? (square/rectangle): ")
    
    # Square drawing
    if want_to_draw == "square":
        # Square data
        x, y = confirm_no_empty_str("Ok. please enter the shape position x, y: ").split(',')
        x, y = int(x), int(y)
        length = int(confirm_input_is_number("Now we need the length of the square: "))
        color = confirm_no_empty_str("And finally the square color, sepecify a number (0-255,\n foreach color in this sequence please R,G,B: ").split(',')
        color = tuple(color)
        
        # drawing the square
        sq = Square(x, y, length, color)
        sq.draw(canv)
        
    elif want_to_draw == "rectangle":
        # Rect data
        x, y = confirm_no_empty_str("Ok. please enter the shape position x, y: ").split(',')
        x, y = int(x), int(y)
        length = int(confirm_input_is_number("Now the length of the rectangle: "))
        width = int(confirm_input_is_number("And its width: "))
        color = confirm_no_empty_str("And finally the rectangle color, sepecify a number (0-255),\nfor each color in this sequence please R,G,B: ").split(',')
        color = tuple(color)
        
        # Drawing the rectangle
        rect = Rectangle(x, y, length, width, color)
        rect.draw(canv)
        
    elif want_to_draw == 'q':
        break
    
        # if user wants to draw again
    draw_again = confirm_no_empty_str("Done. Do you want to draw something else? (y/n - q to quit): ")
    if draw_again == "y":
        continue
    elif draw_again == "n":
        canv.make(filename="files\\image.jpg")
        break


print("Thank you for using the app. Your image is ready!")


'''
#*: In np.zeros(shape=(x, y, z)) shape formula is like this:
    x: number of matrices
    y: length of each matrix
    z: 3rd dimension length
#**: Remember! indeces: [first matrix(row):last matrix(row - not included), column1:column2]
'''