import argparse
import pandas as pd
from data_actions import *

def get_arguments() -> tuple:
    """
    Функция для получения аргуметов
    из командной строки
    
    :return: аргументы"""

    parser = argparse.ArgumentParser()

    try:
        parser.add_argument('-ap', "--annotation_path", required=True, type=str, help = "Путь к файлу с аннотацией")
    except Exception as e:
        print('Неверный формат аргументов')
    
    parsered_data = parser.parse_args()

    return parsered_data.annotation_path


if __name__ == "__main__":

    annotation_path = get_arguments()

    df = read_file(annotation_path)

    df[["height", "width", "depth"]] = df["abs_path"].apply(lambda path: pd.Series(add_images_info(path)))
    
    stat = describe_dataframe(df)
    
    filtered_df = filter_images_by_size(df, 1000, 1300)

    df = add_area_column(df)

    df = sort_values(df)

    build_histogram(df)