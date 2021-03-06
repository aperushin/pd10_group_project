import requests
import random
from basic_word import BasicWord


def load_random_word(url: str) -> BasicWord:
    """
    Загружает с web-ресурса список словарей со словами и их подсловами

    Возвращает экземпляр класса со случайным словом из списка

    :param url: Web-cсылка на JSON-файл, имеющий структуру:
        [{"word":"слово","subwords":["подслово 1","подслово 2"]}]
    :return: Экземпляр класса BasicWord со случайным словом
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
    # Если ссылка не загрузилась, выводим ошибку и завершаем работу приложения
    except requests.exceptions.RequestException as err:
        raise SystemExit(err)

    # Выбираем случайный элемент из загруженного списка
    random_word = random.choice(response.json())
    return BasicWord(**random_word)
