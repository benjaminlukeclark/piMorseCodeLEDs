from MorseCode import MorseCode
from LedInteraction import LedInteraction
from MorseToLed import MorseToLed
import sys


def print_header():
    print("----------------------------------------------------------------------------------------------------")
    print("Python script for Raspberry Pi to communicate strings via keyboard LEDs")
    print("")
    print("By Sudoblark (https://github.com/sudoblark)")
    print("")


def print_footer():
    print("")
    print("----------------------------------------------------------------------------------------------------")


def print_error():
    print_header()
    print("---------------------- ERROR ---------------------------------")
    print("Script either passed incorrectly formatted, or number, of args")
    print("Re-run with --help for assistance")
    print("---------------------- ERROR ---------------------------------")
    print_footer()
    exit(1)


# If incorrect number of args passed then exit
# --led LED --message MESSAGE means 4 args are permissible, 1st arg is always script name
if len(sys.argv) > 5:
    print_error()
else:
    # Setup args to set with default values so we can check if correctly passed at end
    ledChoice = None
    message = None

    # First arg is always script name
    arguments = len(sys.argv) - 1
    position = 1
    while arguments >= position:
        # Print help and close
        if sys.argv[position] == "--help":
            print_header()
            print("Strings are first translated to morse code then communication in dot-dash notation via a chosen LED")
            print("")
            print("Accepted args:")
            print("--help shows this message")
            print("")
            print("--led %ARG% sets led to use, admissible input is: scrollLock, capsLock, numLock")
            print("")
            print("--message %ARG% determines message to encode and sent")
            print("")
            print("Example")
            print("python3 main.py --led capsLock --message SOS")
            print("python3 main.py --led capsLock --message 'Hello World'")
            print_footer()
            exit(1)
        elif sys.argv[position] == "--led":
            ledChoice = sys.argv[position + 1]
            position = position + 2
        elif sys.argv[position] == "--message":
            message = sys.argv[position + 1]
            position = position + 2
        else:
            print_error()

# Triple check input is correct
if (message is None) or (ledChoice is None):
    print_error()
else:
    print_header()
    print("Message: " + message + "   |   LED: " + ledChoice)

# Encrypt our text into morse code
MorseClass = MorseCode()
EncryptedText = MorseClass.encrypt(message)

# Setup interface to hardware
LedInterface = LedInteraction(ledChoice)

# Communicate message
Translator = MorseToLed(LedInterface, EncryptedText)
Translator.communicate_message()

print_footer()
