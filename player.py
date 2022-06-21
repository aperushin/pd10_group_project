class Player:

    def __init__(self, name: str):
        self.name = name
        self.used_words = set()

    def count_used_words(self) -> int:
        """
        получение количества использованных
        """
        return len(self.used_words)

    def add_used_word(self, word: str):
        """
        добавление слова в использованные
        """
        self.used_words.add(word)

    def check_used_word(self, word):
        """
        проверка использования данного
        """

        return word in self.used_words

    def __repr__(self):
        return f"Player {self.name}"

    def __str__(self):
        return self.name
