from MorseCode import MorseCode
from LedInteraction import LedInteraction
from MorseToLed import MorseToLed
from time import sleep


# Encrypt our text into morse code
test_message = "SoS"
MorseClass = MorseCode()
print("Test message: " + test_message)
EncryptedText = MorseClass.encrypt(test_message)

# Setup interface to hardware
LedInterface = LedInteraction("capsLock")

# Communicate message
Translator = MorseToLed(LedInterface, EncryptedText)
Translator.communicate_message()