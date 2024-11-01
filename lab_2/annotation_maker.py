import csv
import os

def annotation_maker(save_path: str, annotation_path: str) -> None:
    """
    Функция создает файл с абсолютными и относительными ссылками
    на изображения
    :param save_path: путь к папке с данными
    :param annotation_path: название файла с аннотациями

    :return: None
    """

    paths = []
    dir = os.getcwd()

    for name in os.listdir(save_path):
        
        absolute_path = os.path.abspath(os.path.join(save_path, name))
        relative_path = str(absolute_path).replace(dir, "")[1:]
        paths.append([absolute_path,relative_path])

    try:
        with open(annotation_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(paths)
    except:
        raise Exception("Cant oppen file")