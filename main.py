from player import Player
from utils import load_random_word, check_user_answer


def main():
    word_for_game = load_random_word()

    player_1 = Player(input("Введите имя игрока:\n"))
    print(f"Привет {player_1}\n"
          f"Составьте {word_for_game.get_subwords_quantity()} слов из слова '{word_for_game}'\n"
          f"Слова должны быть не короче 3 букв\n"
          f"Чтобы закончить игру, угадайте все слова или напишите 'stop'\n"
          f"Поехали, ваше первое слово?")

    while player_1.count_used_words() != word_for_game.get_subwords_quantity():

        user_answer = input()

        if user_answer in ("stop", "стоп"):
            break

        if check_user_answer(user_answer, player_1, word_for_game):
            print("отлично, принимается!")
            player_1.add_used_word(user_answer.lower())

    print(f"Игра завершена, вы угадали {player_1.count_used_words()} слов!")


if __name__ == '__main__':
    main()
