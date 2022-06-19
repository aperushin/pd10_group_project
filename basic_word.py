class BasicWord:

    def __init__(self, word: str, subwords: list):
        self.word = word
        self.subwords = set(subwords)

    def __repr__(self):
        return f"'{self.word}'.BasicWord"

    def is_subword(self, subword: str) -> bool:
        """
        Проверяет наличие подслова в списке подслов
        :param str subword:
        :return bool: True если найдено, False если нет
        """
        return subword in self.subwords

    def get_subwords_quantity(self) -> int:
        """
        Возвращает количество подслов
        :return int:
        """
        return len(self.subwords)
