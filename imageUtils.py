import urllib, cStringIO
from PIL import Image as Image

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from IPython.html.widgets import interactive

# This function shows us our images so we can see what we're doing to them.
def show_image(image):
    fig, ax = plt.subplots()
    plt.figure(figsize=(3,3))
    plt.gray()

    ax.imshow(image)
    ax.axis('off')

    plt.show()

# This function grabs the image from a url so we can change it.
def get_image_from_url(image_url_path):
    file = cStringIO.StringIO(urllib.urlopen(image_url_path).read())
    image = Image.open(file)
    return image

# This will let us easily update where the url for image should come from.
set_image = interactive(get_image_from_url, image_url_path='http://png.clipart.me/previews/a03/puppy-vector-8-39942.jpg')

def resize_image(input_image, size):
    return input_image.resize(size)

def convert_image_to_grayscale(input_image):
    return input_image.convert('L')

def get_image_pixel_data(input_image):
    return input_image.getdata()
