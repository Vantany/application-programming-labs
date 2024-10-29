import os

from icrawler.builtin import GoogleImageCrawler


def img_downloader(keyword: str , save_path: str) -> None:
    """
    Функция для загрузки изображений по ключевому слову
    :param keyword: ключевое слово для поиска
    :param save_path: путь к папке для сохранениия

    :return: None
    """

    if os.path.exists(save_path): # для отладки
        return

    try:
        google_crawler = GoogleImageCrawler(storage={'root_dir': save_path})
        google_crawler.crawl(keyword=keyword, max_num=75)
    except:
        raise Exception("Downloading went wrong")