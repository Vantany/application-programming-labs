import argparse

from img_actions import image_reader, get_image_shape

def get_arguments() -> tuple:
    """
    Читает аргументы
    :return: аргументы
    """

    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("-i", type=str)
        parser.add_argument("-p", type=str)
        return parser.parse_args().i, parser.parse_args().p

    except:
        raise Exception("Incorrect argument format")

if __name__ == '__main__':
    image_name, save_path = get_arguments()

    try:
        img = image_reader(image_name)
    except:
        raise Exception("Can't read image")
    
    width, height = get_image_shape(img)
    print("Image size: {}x{}".format(width, height))

    

    