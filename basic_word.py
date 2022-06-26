class BasicWord:

    def __init__(self, word: str, subwords: list):
        self.word = word
        self.subwords = set(subwords)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.word!r}, {list(self.subwords)})"

    def __str__(self):
        return self.word

    def is_subword(self, subword: str) -> bool:
        """Проверяет наличие подслова в списке подслов"""
        return subword in self.subwords

    @property
    def subwords_quantity(self) -> int:
        """Возвращает количество подслов"""
        return len(self.subwords)
