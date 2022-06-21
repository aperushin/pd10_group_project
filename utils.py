import requests
import random
from basic_word import BasicWord
from player import Player


def load_random_word(url: str = 'https://jsonkeeper.com/b/IWUE') -> BasicWord:
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


def check_user_answer(user_answer: str, player: Player, word_for_game: BasicWord) -> bool:
    """
    Проверяет ответ пользователя на соответствие критериям
    """
    if len(user_answer) < 3:
        print("слишком короткое слово")

    elif player.check_used_word(user_answer.lower()):
        print("уже использовано")

    elif not word_for_game.is_subword(user_answer.lower()):
        print("неверно")

    else:
        return True
