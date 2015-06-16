from __future__ import division
from IPython.html.widgets import interactive
from IPython.display import display

from imageUtils import show, get_image_from_url, get_size, resize_image, convert_image_to_grayscale, get_image_values
from listUtils import join_list_items, add_to_list, reshape_list

ASCII_A = [ '..', '%%', '@@', '??', 'SS', '++', '..', '**', '::', ',,', '..']
ASCII_B = [ '##', '??', '%%', '..', 'SS', '++', '..', '**', '::', ',,', '@@']
ASCII_C = [ '##', '??', '%%', '..', 'SS', '++', '..', '**', '::', ',,', '..']
ASCII_D = ["$$","@@","BB","%%","88","&&","WW","MM","##","**","oo","aa","hh","kk","bb","dd","pp","qq","ww","mm","ZZ","OO","00","QQ","LL","CC","JJ","UU","YY","XX","zz","cc","vv","uu","nn","xx","rr","jj","ff","tt","//","\\","||","((","))","11","{{","}}","[[","]]","??","--","__","++","~~","<<",">>","ii","!!","ll","II",";;","::",",,",'""',"^^","``","''","..","  "]
ASCII_E = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

def get_ascii_for_pixel_value(pixel_value, ascii_chars):
    range_width = 256/(len(ascii_chars)-1)
    ascii_index = int(pixel_value/range_width)

    return ascii_chars[ascii_index]

def make_to_ascii(image_url_path, ascii_chars, new_width=35):
    # First, get image from URL.
    image = get_image_from_url(image_url_path)

    # Next, resize image to new width while preserving aspect ratio.
    (original_height, original_width) = get_size(image)
    aspect_ratio = original_width/original_height
    new_height = int(new_width/aspect_ratio)
    small_image = resize_image(image, new_width, new_height)

    # Then, make the image grayscale.
    gray_image = convert_image_to_grayscale(small_image)

    # Let's use the pixel values to map to the ASCII character set of choice.
    pixels_in_image = list(get_image_values(gray_image))
    pixels_to_chars = [get_ascii_for_pixel_value(pixel_value, ascii_chars) for pixel_value in pixels_in_image]

    # Shape the ASCII list to make the final ASCII image.
    ascii_width = new_width * len(ascii_chars[0])
    ascii_art = reshape_list(pixels_to_chars, ascii_width)

    show(image, small_image, gray_image)
    print(ascii_art)

    return ascii_art

convert_image_to_ascii = interactive(make_to_ascii, image_url_path='http://png.clipart.me/previews/a03/puppy-vector-8-39942.jpg', ascii_chars = {'a': ASCII_A, 'b': ASCII_B, 'c': ASCII_C, 'd': ASCII_D, 'e': ASCII_E}, new_width=[20, 50, 5])

def interactive_ascii():
    display(convert_image_to_ascii)
