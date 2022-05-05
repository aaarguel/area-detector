# Third party modules
import numpy as np
from PIL import Image

def generate_image(image):    
    img = Image.fromarray(image, 'RGB')
    img.save('examples/result.png')
    img.show()
#def analize_image(image):

def get_image(image_path):
    """Get a numpy array of an image so that one can access values[x][y]."""
    img = Image.open(image_path)
    pixels = img.load()
    # convert image to numpy array
    for i in range(img.size[0]): # for every pixel:
        for j in range(img.size[1]):
            if pixels[i,j] != (241, 238, 233):
                # change to black if not red
                pixels[i,j] = (255, 0 ,0)
    data = np.asarray(img)
    #print(type(data))
    # summarize shape
    #print(data.shape)
    return data

def difference_image(image):
    print(image.shape)
    color_red = np.array([255, 255 ,255])
    color_test = np.array([[241, 238, 255], [255, 255 ,255] ])
    a = np.array([241, 238, 255])          
    print(color_test)
    print(color_test[0])
    for row in color_test:         
        if (row == a).all():            
            print(row)
    print(color_test)
    print(image.shape)


def redOrBlack (pathimage):    
    im = Image.open(pathimage)
    newimdata = []
    redcolor = (255,0,0)
    color2compare = (241, 238, 233)
    for color in im.getdata():
        diffRed = abs(color[0] - color2compare[0])
        diffGreen = abs(color[1] - color2compare[1])
        diffBlue = abs(color[2] - color2compare[2])

        pctDiffRed =  diffRed   / 255
        pctDiffGreen =  diffGreen   / 255
        pctDiffBlue =  diffBlue   / 255
        
        pctTotal = (pctDiffRed + pctDiffGreen + pctDiffBlue) / 3 * 100
        if pctTotal < 10.0:
            newimdata.append(redcolor)                    
        else:
            newimdata.append(color)
    newim = Image.new(im.mode,im.size)
    newim.putdata(newimdata)
    newim.save('examples/result.png')
    newim.show()
    


redOrBlack("examples/area1.png")
#difference_image(image)
#generate_image(image)