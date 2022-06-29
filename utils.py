import requests
import random
from basic_word import BasicWord


def load_random_word(url: str) -> BasicWord | None:
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
        # При проблемах с загрузкой данных или интернет соединением - возвращаем None
    except requests.exceptions.RequestException:
        return None

        # Выбираем случайный элемент из загруженного списка
    random_word = random.choice(response.json())
    return BasicWord(**random_word)


def get_ending(number: int) -> str:  # thanks Николай Мартин
    """
    Возвращает окончание слова, согласующееся с числительным

    Версия для слова "слово"
    """
    n_abs = abs(number)
    mod = n_abs % 10
    if (10 < (n_abs % 100) < 15) or mod > 4 or mod == 0:
        return ''
    if mod == 1:
        return 'о'
    if 2 <= mod <= 4:
        return 'а'
