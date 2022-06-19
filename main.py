from constants import WORD_JSON, MIN_LENGTH, STOP_WORDS
from player import Player
from utils import load_random_word


def main():
    word = load_random_word(WORD_JSON)
    subwords_count = word.subwords_count
    player = Player(input('Введите имя игрока\n'))

    print(f'Привет, {player.name}!')
    print(f'Составьте {subwords_count} слов из слова {word.word}')
    print(f'Слова должны быть не короче {MIN_LENGTH} букв')
    print(f'Чтобы закончить игру, угадайте все слова или напишите "{STOP_WORDS[0]}"')
    print('Поехали, ваше первое слово?')

    while player.correct_answers < subwords_count:
        user_answer = input().strip().lower()

        if user_answer in STOP_WORDS:
            break
        if len(user_answer) < MIN_LENGTH:
            print('Слишком короткое слово')
            continue
        if player.has_used_word(user_answer):
            print('Уже использовано')
            continue

        player.add_used_word(user_answer)
        if word.is_subword(user_answer):
            player.correct_answers += 1
            print(
                f'Верно! Угадано {player.correct_answers}'
                f'слов из {subwords_count}'
            )
        else:
            print('Неверно')

    print(f'Игра завершена, вы угадали {player.correct_answers} слов!')


if __name__ == '__main__':
    main()
