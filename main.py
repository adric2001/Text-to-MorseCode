#!/usr/bin/env python3
from pydub import AudioSegment
from pydub.playback import play


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
        morse += conversion_table[letter.upper()]

    return morse
    
def play_morse_sound(text):
    A = AudioSegment.from_wav("sounds/m n\")




def main():
    plain_text = input("Enter text you want to convert to Morse Code:")
    print(text_to_morse(plain_text))
    print(f'Plain Text: {plain_text}')
    playsound_choice = input("Would you like to play the sound? [Y or N]")
    if playsound_choice.upper() == 'Y':




if __name__ == "__main__":
    main()


