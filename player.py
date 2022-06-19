class Player:

    def __init__(self, name):
        self.name = name
        self.used_words = set()

    def count_used_word(self):
        """получение количества использованных
        слов (возвращает int);
        :param
        :return int() """

        return len(self.used_words)

    def add_used_word(self, word):
        """добавление слова в использованные
        слова (ничего не возвращает);
        :param
        :return None"""

        self.used_words.add(self.word)

    def check_used_word(self, word):
        """проверка использования данного
        слова до этого (возвращает bool).
        :param
        :return bool """

        return word in self.used_words

    def __repr__(self):
        return f'Player {self.name}'

    def __str__(self):
        return self.name

