# Create a dictionary of alphabets into symbols
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...',
    'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-',
    'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-',
    'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--',
    'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ', ': '--..--', '.': '.-.-.-',
    '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-'
}

# Write a function to encrypt the message into morse code
def text_to_morse(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
            cipher += MORSE_CODE_DICT[letter] + ' '

        else:
            cipher += ' '

    return cipher

# Morse code to text
def morse_to_text(message):
    message += ' '
    decipher = ''
    ciphered_text = ''
    for letter in message:
        if letter != ' ':
            i = 0
            ciphered_text += letter

        else:
            i += 1
            if i == 2:
                decipher += ' '
            else:
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(ciphered_text)]
                ciphered_text = ''

    return decipher


# Function to run the program
def main():
    message = input('Write a message you want to encrypt: \n')
    encrypted_message = text_to_morse(message.upper())
    print(encrypted_message)

    message = input('Insert the morse code you want to decrypt:\n')
    decrypted_message = morse_to_text(message)
    print(decrypted_message)


if __name__ == '__main__':
    main()

