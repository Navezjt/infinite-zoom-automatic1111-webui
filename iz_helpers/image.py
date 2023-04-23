from PIL import Image

def shrink_and_paste_on_blank(current_image, mask_width, mask_height, opacity=1):
    """
    Decreases size of current_image by mask_width pixels from each side,
    then adds a mask_width width transparent frame,
    so that the image the function returns is the same size as the input.
    :param current_image: input image to transform
    :param mask_width: width in pixels to shrink from each side
    :param mask_height: height in pixels to shrink from each side
    """

    # calculate new dimensions
    width, height = current_image.size
    new_width = width - 2 * mask_width
    new_height = height - 2 * mask_height

    # resize and paste onto blank image
    prev_image = current_image.resize((max(8,new_width), max(8,new_height)))
    blank_image = Image.new("RGBA", (width, height), (0, 0, 0, 1))

    if (1 == opacity ):

        blank_image.paste(prev_image, (mask_width, mask_height))
    else:

        blank_image.putalpha(round(255*opacity))
        blank_image.paste(prev_image, (mask_width, mask_height))

    return blank_image
