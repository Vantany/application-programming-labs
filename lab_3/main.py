import argparse


def get_arguments() -> tuple:
    """
    Читает аргументы
    :return: аргументы
    """

    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("-i", type=str)
        parser.add_argument("-p", type=str)
        return parser.parse_args().i, parser.parse_args().p

    except:
        raise Exception("Incorrect argument format")

if __name__ == '__main__':
    image_name, save_path = get_arguments()
    