#!/usr/bin/env python3
import pygame
import time


def text_to_morse(text):
    conversion_table = {
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        '.': '.-.-.-',
        ',': '--..--',
        '=': '-...-',
    }

    morse = 'Morse Code: '

    for letter in text:
        if letter == ' ':
            morse += ' '
        else:
            morse += conversion_table[letter.upper()]

    return morse
    
def play_morse_sound(text):

    pygame.mixer.init()

    for letter in text:
        if letter == ' ':
            time.sleep(2)
        else:
            pygame.mixer.music.load(f'sounds/{letter}_morse_code.ogg.mp3')
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

            time.sleep(1)


def main():
    still_running = True

    while still_running:
        plain_text = input("Enter text you want to convert to Morse Code:")
        print(text_to_morse(plain_text))
        print(f'Plain Text: {plain_text}')
        playsound_choice = input("Would you like to play the sound? [Y or N]")
        if playsound_choice.upper() == 'Y':
            play_morse_sound(plain_text)
        else:
            pass
        continue_choice = input("Would you like to convert another text to morse? [Y or N]")
        if continue_choice.upper() == 'Y':
            still_running = True
        else:
            still_running = False
        


if __name__ == "__main__":
    main()


