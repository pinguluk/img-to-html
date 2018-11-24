from PIL import Image

# function rgb => hex
def rgb2hex(rgb):
    r = rgb[0]
    g = rgb[1]
    b = rgb[2]
    hex = "#{:02x}{:02x}{:02x}".format(r,g,b)
    return hex

# image name + extension
filename = "2018.png"
# load image + convert to RGBA
image = Image.open(filename).convert('RGBA')
# load pixels
pixeldata = image.load()

# open / create html file
file = open('index.html', 'w')
# write basic stuff
file.write('<!DOCTYPE html><html><head><style>#image{display:flex;flex-direction:column}.row div{display:inline-block;float:left;width:1px;height:1px;}</style></head><body><div id="image">')

#image height & width
width, height = image.size

# loop rows
for y in range(height):
    # create row div
    file.write('<div class="row">')
    # loop columns
    for x in range(width):
        # print current pixel
        # print(pixeldata[x, y])
        # if current pixel is transparent => write empty div
        if pixeldata[x, y][3] == 0:
            file.write('<div></div>')
        # else write the current pixel to hex value
        else:
            hexValue = rgb2hex(pixeldata[x,y])
            file.write('<div style="background:' + hexValue + '"></div>')
    # close row div
    file.write('</div>')

# close "image" div
file.write('</div>')
# close body & html tags
file.write('</body></html>')


