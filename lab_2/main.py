import argparse

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
    keyword, sp, ap = get_arguments()
    