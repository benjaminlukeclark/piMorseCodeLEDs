class MorseCode:
    """
    Class to encrypt messages as morse code
    """
    def __init__(self):
        self.__lookUpDict = {
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
            '1': '.----',
            '2': '..---',
            '3': '...--',
            '4': '....-',
            '5': '.....',
            '6': '-....',
            '7': '--...',
            '8': '---..',
            '9': '----.',
            '0': '-----',
            ', ': '--..--',
            '.': '.-.-.-',
            '?': '..--..',
            '/': '-..-.',
            '-': '-....-',
            '(': '-.--.',
            ')': '-.--.-'
        }

    def encrypt(self, message):
        """
        Encrypts a string as morse code
        :param message: String to encrypt
        :type message: Str
        :return: message as morse code
        """
        if type(message) is not str:
            raise ValueError("MorseCode encrypt method requires string input")
        return_message = ''
        for char in message:
            if char != " ":
                return_message += self.__lookUpDict[char.upper()]
            else:
                return_message += ' '
        return return_message

