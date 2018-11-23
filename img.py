from PIL import Image
import cv2
import numpy

def rgb2hex(rgb):
    r = rgb[0]
    g = rgb[1]
    b = rgb[2]
    hex = "#{:02x}{:02x}{:02x}".format(r,g,b)
    return hex


image = cv2.imread("smaller.png")

#contor
i = 0
# grab the image dimensions
h = image.shape[0]
w = image.shape[1]

file = open('index.html', 'w')
file.write('<!DOCTYPE html><html><head><style>#image{display:flex;flex-direction:column}.row div{display:inline-block;float:left;width:5px;height:5px;}</style></head><body><div id="image">')

# loop over the image, pixel by pixel
for y in range(0, h):
    file.write('<div class="row">')
    for x in range(0, w):
        hexValue = rgb2hex(image[y, x])
        file.write('<div style="background:' + hexValue + '"></div>')
        i = i + 1
    file.write('</div></body></html>')


file.write('<div></div>')
file.write('</body></html>')


