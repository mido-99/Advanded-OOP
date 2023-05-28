'''
## This file will hold the functions I make or find useful and may need it one day ##
Whenever i need them, copy this file into working directory and import from it
'''

### String Manipulation ###
def package_version_remover(filename='requirements.txt', separator='=', delete=False):
    '''deletes the version specified after each package -just to install the latest version'''
    
    with open(filename, 'r+') as file:
        packages = file.readlines()
        if delete == True:
            file.seek(0)
            file.truncate()
        
        for i in range(len(packages)):
            packages[i] = packages[i].split(separator)[0]
            
        file.writelines('\n'.join(packages))


### PDF ###
def add_cell_with_format(pdf, text, font_family, font_style, font_size, cell_width, cell_height):
    '''Special function used with fpdf, to simplify the process of adding cells with specific font formatting'''
    
    pdf.set_font(font_family, font_style, font_size)
    pdf.cell(cell_width, cell_height, text)

### Input ###
def confirm_no_empty_str(input_message: str):
    '''Confirms that the user doesn't enter an empty string'''
    while True:
        input_name = input(input_message)
        if not input_name:
            print("Empty input!")
            continue
        break
    return input_name

def confirm_input_is_number(input_message: str):
    '''Confirms that the user enters a number'''
    while True:
        try:
            input_number = float(input(input_message))
        except ValueError:
            print("Please enter a number!")
            continue
        break
    return input_number

def float_coordinate(input_message):
    coords = input(input_message).split(',')
    for i in range(len(coords)):
        coords[i] = float(coords[i])
    return coords

