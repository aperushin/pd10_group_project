class Player:

    def __init__(self, name: str) -> None:
        self.name = name
        self.used_words = set()

    def count_used_words(self) -> int:
        """Считает количество использованных слов"""
        return len(self.used_words)

    def add_used_word(self, word: str) -> None:
        """Добавляет слово в список использованных слов"""
        self.used_words.add(word)

    def check_used_word(self, word: str) -> bool:
        """Проверяет наличие слова в списке использованных слов"""
        return word in self.used_words

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.name!r})'

    def __str__(self) -> str:
        return self.name
