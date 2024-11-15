import pandas as pd
import cv2
import os
import matplotlib.pyplot as plt

def read_file(filename: str) -> pd.DataFrame:

    try:
        df = pd.read_csv(filename)
        df.columns = ["abs_path", "re_path"]
        return df
    
    except Exception as ex:
        print("Во время чстения файла произошла ошибка", ex.args)


def add_images_info(path: str) -> tuple:
    img = cv2.imread(path)
    if img is not None:
        height, width, depth = img.shape
        return height, width, depth
    else:
        return None, None, None
    
def filter_images_by_size(df: pd.DataFrame, max_width, max_height: int)-> pd.DataFrame:
    filtered_df = df[(df['height'] <= max_height) & (df['width'] <= max_width)]
    return filtered_df


def add_area_column(df: pd.DataFrame) -> pd.DataFrame:
    df["area"] = df["height"] * df["width"]
    return df


def build_histogram(df: pd.DataFrame) -> None:
    plt.figure(figsize=(10, 6))
    plt.hist(df['area'], bins=20, color='skyblue', edgecolor='black')
    plt.title("Распределение площадей изображений")
    plt.xlabel("Площадь изображения (пиксели)")
    plt.ylabel("Количество изображений")
    plt.show()