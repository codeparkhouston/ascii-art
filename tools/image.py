from PIL import Image
import urllib, warnings

from skimage import io, img_as_ubyte
from skimage.transform import rescale, resize
from skimage.color import rgb2gray
import matplotlib.pyplot as plt

from ipywidgets.widgets import interactive

# This function shows us our images so we can see what we're doing to them.
def show(*images):
    fig, ax = plt.subplots(nrows=1, ncols=len(images), squeeze=False)

    # assumes images are all the same size.
    (image_height, image_width) = get_size(images[0])
    aspect_ratio = image_width/image_height
    fig_height = 5
    fig_image_width = fig_height * aspect_ratio
    fig_width = len(images) * fig_image_width

    for index, image in enumerate(images):
        ax[0][index].imshow(image, cmap=plt.cm.gray)
    fig.set_size_inches(fig_width, fig_height)
    steps = plt.gcf()
    plt.close()
    return steps

# This function grabs the image from a url so we can change it.
def get_image_from_url(image_url_path):
    image = io.imread(image_url_path)
    return image

# This will let us easily update where the url for image should come from.
set_image = interactive(get_image_from_url, image_url_path='http://png.clipart.me/previews/a03/puppy-vector-8-39942.jpg')

def resize_image(input_image, new_width, new_height):
    resized_image = resize(input_image, (new_height, new_width), mode = 'constant', anti_aliasing = False)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        return(img_as_ubyte(resized_image))

def convert_image_to_grayscale(input_image):
    # return rgb2gray(input_image)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        return(img_as_ubyte(rgb2gray(input_image)))


def get_image_pixel_data(input_image):
    return input_image.getdata()

def get_size(input_image):
    return input_image.shape[:2]

def scaleto255(grayscale_value):
    return int(round(grayscale_value*255))

def center_gray(image_values_list):
    imagemax = max(image_values_list)
    imagemin = min(image_values_list)

    def _center_gray(grayscale_value):
        return (grayscale_value - imagemin)/(imagemax - imagemin)

    return _center_gray

def get_image_values(gray_image):
    imagelist = gray_image.flatten()
    # center_gray_to_list = center_gray(imagelist)
    # imagelist = map(center_gray_to_list, imagelist)
    # pixels_in_image = list(map(scaleto255, imagelist))
    return(list(imagelist))