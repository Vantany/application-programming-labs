import cv2
import numpy as np
import matplotlib.pyplot as plt

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


def image_invert(img: np.ndarray) -> np.ndarray:
    """
    Инвертирует пиксели в изображении
    :param img: изображение"""
    
    return 255 - img

def show_images(*args, **kwargs) -> None:
    """
    Отображает изображение на жкран с помощью
    библиотеки matplotlib
    в *args находятся изображения
    в **kwargs заголовки для изображений"""

    titles = kwargs.get('titles', None)
    num_images = len(args)

    plt.figure(figsize=(15, 5))

    for i, img in enumerate(args):
        plt.subplot(1, num_images, i + 1)
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)) 
        if titles and i < len(titles):
            plt.title(titles[i]) 

    plt.show()

def save_image(save_path: str, img: np.ndarray) -> None:
    """
    Сохраняет изображение
    :param save_dir: Путь по которому сохранится файл
    :param img: Сохраняемое изображение
    """
    cv2.imwrite(save_path, img)