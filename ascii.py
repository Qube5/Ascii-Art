from skimage import color
from skimage import io
from skimage import filters
import math


def main():
    fileName = '../adithyaj'
    outputWidth = 100
    mapping = {
        0.1 : "0", #█
        0.2 : "8", #▇
        0.3 : "6", #▆
        0.4 : "4", #▅
        0.5 : "2", #▄
        0.6 : "1", #▃
        0.7 : "a", #▂
        0.8 : "i", #▁
        0.9 : ":", #▁
        1.0 : ".", #
    }
    createAscii(fileName, outputWidth)

def displayImage(img):
    io.imshow(img)
    io.show()
    print(img.shape)

def getDims(img, width):
    sourceWidth  = img.shape[1]
    sourceHeight = img.shape[0]
    outputWidth = width # desired ascii width
    outputHeight = outputWidth * (sourceHeight / sourceWidth) # scales appropriately
    width  = int(sourceWidth  / outputWidth )
    height = int(sourceHeight / outputHeight)
    return width, height

def process(average):
    value = min(mapping, key = lambda x: abs(x-average))
    return mapping[value] + mapping[value]

def processImg(fileName):
    img = io.imread(fileName+'.jpg')
    img = color.rgb2gray(img) # convert to grayscale
    return img

def writeFile(fileName, output):
    file = open(fileName+'.txt','w')
    file.write(output)

def genOutput(width, height, img):
    output = ""
    for x in range(math.floor(len(img[:,0]) / width)):
        for y in range(math.floor(len(img[0]) / height)):
            average = getAverage(x, y, width, height, img)
            output += process(average)
        output += "\n"
    return output

def getAverage(x, y, width, height, img):
    sum = 0
    for i in range(width):
        for j in range(height):
            sum += img[x * width + i, y * height + j]
    average = sum / (width * height)
    return average

def createAscii(fileName, outputWidth):
    img = processImg(fileName)
    width, height = getDims(img, outputWidth)
    # width, height = 1, 1 # actual pixel for pixel size
    output = genOutput(width, height, img)
    print(output)
    writeFile(fileName, output)

if __name__ == "__main__":
    main()
