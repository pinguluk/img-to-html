from PIL import Image
import argparse, sys

parser=argparse.ArgumentParser()
parser.add_argument('-image', '--image', '-img' , '--img', help='Image filename + extension', required=True)
parser.add_argument('-output', '--output', help='Output filename + extension (should be .html)', required=True)
args=parser.parse_args()

# image name + extension
imageFileName = args.image
# load image + convert to RGBA
image = Image.open(imageFileName).convert('RGBA')
# load pixels
pixeldata = image.load()

# open / create html file
# take argument output file name if sety
if (args.output):
    file = open(args.output, 'w')
# else use default 'index.html'
else:
    file = open('index.html', 'w')
# write basic stuff
file.write('<!DOCTYPE html><html><head><style>#img{display:flex;flex-direction:column}i{display:inline-block;float:left;width:1px;height:1px;}</style></head><body><div id="img">')

#image height & width
width, height = image.size

# loop rows
for y in range(height):
    # create row div
    file.write('<d>')
    # loop columns
    for x in range(width):
        # print current pixel
        ## print(pixeldata[x, y])
        # if current pixel is transparent => write empty div
        if pixeldata[x, y][3] == 0:
            file.write('<i></i>')
        # else write the current pixel to rgb value
        else:
            # rgbaValue = (r, g, b, a), where a = a / 255 (we need value between 0 and 1) & format to 2 decimals
            r = str(pixeldata[x,y][0])
            g = str(pixeldata[x,y][1])
            b = str(pixeldata[x,y][2])
            a = str(format(pixeldata[x,y][3]/255, '.2f'))

            # if a == 0.00, set it to 0 so we minify the output
            if a == '0.00':
                a = '0'
            # else if a == 1.00, set it to 0 so we minify the output as well
            elif a == '1.00':
                a = '1'

            # write current pixel
            # if a != 1, then add a
            if a != '1':
                file.write('<i style="background:' + "rgb(" +  r + ',' +  g + ',' + b +',' + a + ")" + '"></i>')
            # else, we don't add a (1), in order to reduce filesize and performance
            else:
                file.write('<i style="background:' + "rgb(" +  r + ',' +  g + ',' + b + ")" + '"></i>')

    # close row div
    file.write('</d>')

# close "image" div
file.write('</div>')
# close body & html tags
file.write('</body></html>')


