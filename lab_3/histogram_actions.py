import cv2, numpy as np
import matplotlib.pyplot as plt

def draw_histogram(img: np.ndarray, enable_grid = False) -> None:
    
    plt.figure(figsize=(10, 5))

    for ind, col in enumerate(('b', 'g', 'r')):
        histogram = cv2.calcHist([img], [ind], None, [256], [0, 256])
        plt.plot(histogram, color=col)

    plt.title('Гистограмма изображения')
    plt.xlabel('Интенсивность пикселей')
    plt.ylabel('Частота')
    plt.xlim([0, 256])
    plt.legend(['Синий канал', 'Зеленый канал', 'Красный канал'])

    if enable_grid:
        plt.grid()

    plt.show()