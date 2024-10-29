import cv2
import numpy as np

def image_reader(image_name: str) -> np.ndarray:
    """
    Считывает изображение из файла
    :return: изображение в представлении в виде 
    двумерного массива
    """

    return cv2.imread(image_name)


def get_image_shape(img: np.ndarray) -> tuple:
    """
    Находит размеры изображения
    :return: размер изображения в виде кортежа
    """

    return img.shape[0], img.shape[1]