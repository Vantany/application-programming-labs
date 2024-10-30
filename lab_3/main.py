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
        parser.add_argument("-i", "--image", type=str, help = "Путь до исходного изображения")
        parser.add_argument("-p", "--save_path", type=str, help = "Путь для сохранения")

        if not parser.parse_args().image or not parser.parse_args().save_path:
            raise argparse.ArgumentError
        
        return parser.parse_args().image, parser.parse_args().save_path

    except argparse.ArgumentError as e:
        print(e)

if __name__ == '__main__':
    image_name, save_path = get_arguments()

    try:
        img = image_reader(image_name)

        width, height = get_image_shape(img)
        print("Image size: {}x{}".format(width, height))

        draw_histogram(img, enable_grid=True)

        inverted_img = image_invert(img)
        show_images(img, inverted_img)

        save_image(save_path=save_path, img = inverted_img)

    except Exception as e:
        print(e)

    