# img-to-html

img-to-html is a Python script that converts every pixel from an image, to a HTML element.

## Installation

Download the imgtohtml.py script and install PIL

```
pip install pillow
```

## Usage

```
imgtohtml.py -img IMAGE_DOT_EXTENSION -output FILENAME.html
```

## Example

```
imgtohtml.py -img cat.jpg -output cat.html
imgtohtml.py -img fish.png -output fish.html
```

## Preview

![Cat](https://media.giphy.com/media/J1dllY9a4aSWQZUeMU/giphy.gif)
![Fish](https://media.giphy.com/media/JUk9HGd22CPeAVkzJB/giphy.gif)

## TODO

- Find a better way to implement background style (color) for each element, to reduce the file size
- Improve the width (and height) of a pixel, when the adjacent pixels are the same, in order to remove repetitive pixels and improve file size 
