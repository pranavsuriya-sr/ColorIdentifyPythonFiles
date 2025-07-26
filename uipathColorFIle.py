from PIL import ImageGrab

# Dictionary mapping HEX codes to common color names (can be extended)
HEX_TO_NAME = {
    '000000': 'Black',
    'FFFFFF': 'White',
    'FF0000': 'Red',
    '00FF00': 'Lime',
    '0000FF': 'Blue',
    'FFFF00': 'Yellow',
    '00FFFF': 'Cyan',
    'FF00FF': 'Magenta',
    'C0C0C0': 'Silver',
    '808080': 'Gray',
    '800000': 'Maroon',
    '808000': 'Olive',
    '008000': 'Green',
    '800080': 'Purple',
    '008080': 'Teal',
    '000080': 'Navy',
    'A52A2A': 'Brown',
    'FFA500': 'Orange',
    'F0E68C': 'Khaki',
    'ADD8E6': 'Light Blue',
    '90EE90': 'Light Green',
    'FFC0CB': 'Pink',
    'FFD700': 'Gold',
    'D3D3D3': 'Light Grey',
    'FA8072': 'Salmon',
    'D2691E': 'Chocolate',
    'F9FAFB' : 'lightgrey',
    '1F1F1F' : 'darkgrey',
}
def getHex(rgb):
    return '%02X%02X%02X'%rgb

def get_color(x, y):
    x = int(float(x))
    y = int(float(y))

    bbox = (x, y, x + 1, y + 1)
    im = ImageGrab.grab(bbox=bbox)
    rgbim = im.convert('RGB')
    r, g, b = rgbim.getpixel((0, 0))

    # hex_val = '%02X%02X%02X' % (r, g, b)
    hex_val = getHex((r, g, b))
    color_name = HEX_TO_NAME.get(hex_val.upper(), 'Unknown')

    return f'rgb({r},{g},{b}) | HEX #{hex_val} | Name: {color_name}'
