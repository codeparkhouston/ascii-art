import urllib, cStringIO
from PIL import Image as Image

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from IPython.html.widgets import interactive
from IPython.display import display

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

def get_ascii_char_from_value(ascii_chars, pixel_value):
    range_width=256/(len(ascii_chars)-1)
    ascii_char = ascii_chars[int(math.floor(pixel_value/range_width))]
    return ascii_char
