# pylint: disable=line-too-long


#########################################################################
# INFO:
# Un set es una colección que no posee órden, y por tanto, tampoco números de índex. Esto quiere decir que no podemos decidir el orden en el cual aparecerán sus # elementos. En Python, los sets se escriben entre llaves.
#########################################################################


"""Modulos a utilizar"""
import random
import string
from words_for_hangman import words


def get_valid_words(guess_words):
    """Selecciona de manera aleatoria una palabra de la lista de palabras"""
    word = random.choice(guess_words)
    # Devuelve la parabra TODA EN MAYUSCULA
    return word.upper()


def hangman():
    """Ahorcado"""
    # ----- Guarda la palabra que el usuario tiene que adivinar
    word = get_valid_words(words)
    # ----- Guarda las letras que componen la palabra que el usuario tiene que adivinar
    word_letters = set(word)
    # ----- Guarda todas las letras del abecedario en mayuscula ----- #
    alphabet = set(string.ascii_uppercase)
    # ----- Set vacio. Guarda las letras que el usuario ya utilizo
    used_letters = set()

    lives = 6

    while len(word_letters) > 0 and lives > 0:
        # ----- .join agrega a la cadena separado por el caracter que se le coloque adelante
        print(
            "You have",
            lives,
            "lives left and you have used these letters:",
            " ".join(used_letters),
        )

        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word: ", " ".join(word_list))

        # ----- Pidiendo al usuario que ingrese una letra
        user_letter = input("Guess a letter: ").upper()
        # ----- Si la letra que ingresa el usuario esta en 'alphabet', la agrega a la variable 'used_letters'
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            # ----- Si la letra que ingresa el usuario esta en la palabra, elimina esa letra de la variable que contiene las letras de la palabra a adivinar
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                # ----- Le quita una vida al usuario si la letra ingresada no se encuentra en la palabra
                lives = lives - 1
                print("Letter is not in word")
        # ----- Si la letra qwue ingresa el usuario ya fue utilizada
        elif user_letter in used_letters:
            print("You have already used that character. Please try again")
        else:
            # ----- El caracter ingresado no es valido (no se encuentra en variable 'alphabet')
            print("Invalid character. Please try again")

    if lives == 0:
        print("You died, sorry. The word was", word)
    else:
        print("Congrats! You guessed the word!", word, "!!")


hangman()
