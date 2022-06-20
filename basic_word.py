class BasicWord:

    def __init__(self, word: str, subwords: list | set) -> None:
        self.word = word
        self.subwords = set(subwords)

    def is_subword(self, subword: str) -> bool:
        """
        Проверяет наличие подслова в списке подслов
        :param str subword: Подслово для проверки
        :return bool: True если найдено, False если нет
        """
        return subword in self.subwords

    def get_min_length(self):
        """Находит минимальную длину подслова из списка подслов"""
        return min([len(x) for x in self.subwords])

    @property
    def subwords_count(self) -> int:
        """Возвращает количество подслов"""
        return len(self.subwords)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.word!r}, {self.subwords!r})'

    def __str__(self) -> str:
        return f'Слово "{self.word}"'
