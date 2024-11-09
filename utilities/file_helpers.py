from PIL import Image
import os

def get_extension_with_dot(filename) -> str:
    """
    Return the file extension with a dot.
    
    Parameters:
    filename (str): The filename
    
    Returns:
    str: The file extension with a dot. ('.jpg', '.png', etc.)
    """
    return os.path.splitext(filename)[1]

def image_to_webp (input_image_path, output_image_path, quality=80, lossless=False, **params): 
    """
    Save an image to the webp format.
    
    Parameters:
    input_image_path (str): The path to the image to be converted.
    output_image_path (str): The path where the converted image will be saved.
    quality (int): The quality of the output image. Range is 0-100. Default is 80.
    lossless (bool): If True, the image will be saved losslessly. Default is False.
    **params: Additional parameters to be passed to PIL's save() method.
    
    Returns:
    None
    """
    with Image.open(input_image_path) as img:
        img.save(output_image_path, format='WEBP', quality=quality, lossless=lossless, **params)
