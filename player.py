from dataclasses import dataclass, field


@dataclass
class Player:

    name: str
    correct_answers: int = 0
    used_words: set[str] = field(init=False, default_factory=set)

    def count_used_words(self) -> int:
        """Считает количество использованных слов"""
        return len(self.used_words)

    def add_used_word(self, word: str) -> None:
        """Добавляет слово в список использованных слов"""
        self.used_words.add(word)

    def has_used_word(self, word: str) -> bool:
        """Проверяет наличие слова в списке использованных слов"""
        return word in self.used_words

    def __str__(self) -> str:
        return f'Игрок {self.name}'
