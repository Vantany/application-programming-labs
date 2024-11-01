import cv2
import numpy as np
import matplotlib.pyplot as plt

def image_reader(image_name: str) -> np.ndarray:
    """
    Считывает изображение из файла
    :return: изображение в представлении в виде 
    двумерного массива
    """
    try:
        img = cv2.imread(image_name)

        if img is None:
            raise Exception('Не удалось прочитать изображение')
        return img

    except Exception as e:
        print(*e.args)


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

def show_images(img, inverted_img: np.ndarray) -> None:
    """
    Отображает изображение на жкран с помощью
    библиотеки matplotlib
    :param img: исходное изображение
    :param inverted_img: инвертированное изображение
    """

    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.title('Исходное изображение')
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.title('Инвертированное изображение')
    plt.imshow(cv2.cvtColor(inverted_img, cv2.COLOR_BGR2RGB)) 
    plt.axis('off')

    plt.show()

def save_image(save_path: str, img: np.ndarray) -> None:
    """
    Сохраняет изображение
    :param save_dir: Путь по которому сохранится файл
    :param img: Сохраняемое изображение
    """
    
    try:   
        if not cv2.imwrite(save_path, img):
            raise Exception('Не удалось сохранить изображение')
        
    except Exception as e:
        print(*e.args)