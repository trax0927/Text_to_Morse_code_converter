# TODO 1: get morse code for alphabets and numbers in a dictionary
morse_code = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',
    'F': '..-.',  'G': '--.',   'H': '....',  'I': '..',    'J': '.---',
    'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',  'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
    '/': '-..-.',  '(': '-.--.',  ')': '-.--.-', '&': '.-...', ':': '---...',
    ';': '-.-.-.', '=': '-...-',  '+': '.-.-.',  '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'  # Space as separator
}

# TODO 2: prompt the user for user text

end = False
while not end:

    Texts = input('Enter a Text you want to convert to morse code: ').upper()
    if Texts == '':
        print('input a text')
    else:
        Texts = list(Texts)

    # TODO 3: converting the text to morse code without function
    if Texts:
        print('morse code:')
        for Text in Texts:
            try:
                print(f'{morse_code[Text]}', end=" ")
            except KeyError:
                print(f'\n "{Text}" is not a morse code alphabet, try again!', end='')
        print('\n')
        # prompt user to continue conversion
    if_continue = input('do you want to write another text (yes/no): ')
    if if_continue == 'no':
        print('\n # ----------------- #')
        end = True

