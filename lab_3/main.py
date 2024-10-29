import argparse

from img_actions import *
from histogram_actions import draw_histogram

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

        width, height = get_image_shape(img)
        print("Image size: {}x{}".format(width, height))

        draw_histogram(img, enable_grid=True)

        inverted_img = image_invert(img)
        show_images(img, inverted_img, titles = ["Исходное изображение", "Инвертированное изображение"])

        save_image(save_path=save_path, img = inverted_img)

    except:
        raise Exception("Something went wrong")

    