import pandas as pd
import cv2
import os
import matplotlib.pyplot as plt

def read_file(filename: str) -> pd.DataFrame:
    """
    Функция ждя чтения файла в датафрейм
    
    :param filename: имя файла
    :return: аргументы"""
    try:
        df = pd.read_csv(filename)
        df.columns = ["abs_path", "re_path"]
        return df
    
    except Exception as ex:
        print("Во время чстения файла произошла ошибка", ex.args)


def add_images_info(path: str) -> tuple:
    """
    Добавляет информацию об изображении.

    :param path: Путь к изображению.
    :return: Кортеж, содержащий высоту, ширину и глубину изображения.
    """
    img = cv2.imread(path)
    if img is not None:
        height, width, depth = img.shape
        return height, width, depth
    else:
        return None, None, None

def sort_values(df: pd.DataFrame) -> pd.DataFrame:
   """
   Сортирует DataFrame по столбцу "area".

   :param df: DataFrame, содержащий информацию об изображениях.
   :return: DataFrame, содержащий информацию об изображениях, отсортированный по столбцу "area".
   """
   return df.sort_values(by='area')


def describe_dataframe(df: pd.DataFrame) -> pd.DataFrame:
   """
   Возвращает статистическую информацию о DataFrame.

   :param df: DataFrame, содержащий информацию об изображениях.
   :return: DataFrame, содержащий статистическую информацию о DataFrame.
   """
   return df[['height', 'width', 'depth']].describe()


def filter_images_by_size(df: pd.DataFrame, max_width: int, max_height: int) -> pd.DataFrame:
   """
   Фильтрует DataFrame по размеру изображений.

   :param df: DataFrame, содержащий информацию об изображениях.
   :param max_width: Максимальная ширина изображения.
   :param max_height: Максимальная высота изображения.
   :return: DataFrame, содержащий информацию об изображениях, удовлетворяющих условиям фильтрации.
   """
   filtered_df = df[(df['height'] <= max_height) & (df['width'] <= max_width)]
   return filtered_df



def add_area_column(df: pd.DataFrame) -> pd.DataFrame:
   """
   Добавляет столбец "area" в DataFrame.

   :param df: DataFrame, содержащий информацию об изображениях.
   :return: DataFrame, содержащий информацию об изображениях с добавленным столбцом "area".
   """
   df["area"] = df["height"] * df["width"]
   return df



def build_histogram(df: pd.DataFrame) -> None:
   """
   Построение гистограммы распределения площадей изображений.

   :param df: DataFrame, содержащий информацию об изображениях.
   :return: None
   """
   plt.figure(figsize=(10, 6))
   plt.hist(df['area'], bins=20, color='skyblue', edgecolor='black')
   plt.title("Распределение площадей изображений")
   plt.xlabel("Площадь изображения (пиксели)")
   plt.ylabel("Количество изображений")
   plt.show()
