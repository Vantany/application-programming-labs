import argparse

from img_downloader import img_downloader
from annotation_maker import annotation_maker
from iterator import ImgIterator

def get_arguments() -> tuple:
    """
    Функция для получения аргуметов
    из командной строки
    
    :return: аргументы"""

    parser = argparse.ArgumentParser()

    try:
        parser.add_argument('keyword', type=str)
        parser.add_argument('-sp', type=str)
        parser.add_argument('-ap', type=str)
    except:
        raise Exception('Неверный формат аргументов')
    
    return parser.parse_args().keyword, parser.parse_args().sp, \
            parser.parse_args().ap

 
if __name__ == "__main__":
    keyword, save_path, annotation_path = get_arguments()
    try:
        img_downloader(keyword=keyword, save_path=save_path)
        annotation_maker(save_path=save_path, annotation_path=annotation_path)

        iterator = ImgIterator(annotation_path=annotation_path)
        for img in iterator:
            print(img)
            
    except:
        raise Exception("Something went wrong")
