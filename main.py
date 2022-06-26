from player import Player
from utils import load_random_word, get_ending


def main():
    word_for_game = load_random_word()

    player = Player(input("Введите имя игрока:\n"))
    print(f"Привет {player}\n"
          f"Составьте {word_for_game.subwords_quantity} слов из слова '{word_for_game}'\n"
          f"Слова должны быть не короче 3 букв\n"
          f"Чтобы закончить игру, угадайте все слова или напишите 'stop'\n"
          f"Поехали, ваше первое слово?")

    while player.guessed_words != word_for_game.subwords_quantity:

        user_answer = input()

        if user_answer in ("stop", "стоп"):
            break

        elif len(user_answer) < 3:
            print("Слишком короткое слово")

        elif player.check_used_word(user_answer.lower()):
            print("Это слово уже отгадано")

        elif not word_for_game.is_subword(user_answer.lower()):
            print("Неверно")

        else:
            player.add_used_word(user_answer.lower())
            print(f"Отлично, принимается!\n"
                  f"Вы угадали {player.guessed_words} слов{get_ending(player.guessed_words)} "
                  f"из {word_for_game.subwords_quantity}")

    print(f"\nИгра завершена, вы угадали {player.guessed_words} слов{get_ending(player.guessed_words)} "
          f"из {word_for_game.subwords_quantity}!")


if __name__ == '__main__':
    main()
