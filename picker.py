from pynput import keyboard
from pynput import mouse
from PIL import Image, ImageGrab

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


def checkColor(x,y):
    bbox = (x,y,x+1,y+1)
    im = ImageGrab.grab(bbox=bbox)
    rgbim = im.convert('RGB')
    r,g,b = rgbim.getpixel((0,0))
    print(f'COLOR: rgb{(r,g,b)} | HEX #{getHex((r,g,b))} | NAME: {HEX_TO_NAME.get(getHex((r,g,b)).upper(), "Unknown")}')
    
   
def onClick(x,y, button, pressed):
	if pressed and button == mouse.Button.left:
            print(f'x: {x}, y: {y}')
            checkColor(x,y)

def onRel(key):
	if key == keyboard.Key.esc:
		mlstnr.stop()
		return False



if __name__ == '__main__':
    with keyboard.Listener(on_release = onRel) as klstnr:
        with mouse.Listener(on_click = onClick) as mlstnr:
            klstnr.join()
            mlstnr.join()

