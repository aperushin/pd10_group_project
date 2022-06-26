class Player:

    def __init__(self, name: str):
        self.name = name
        self.used_words = set()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name!r})"

    def __str__(self):
        return self.name

    @property
    def guessed_words(self) -> int:
        """Возвращает количества угаданных слов"""
        return len(self.used_words)

    def add_used_word(self, word: str):
        """добавление слова в использованные"""
        self.used_words.add(word)

    def check_used_word(self, word):
        """
        проверка использования данного
        """
        return word in self.used_words
