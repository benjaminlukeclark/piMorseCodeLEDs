from LedInteraction import LedInteraction
from time import sleep


def space_logic():
    """
    Do nothing for 3 seconds (same time as dash, not an expert on morse so may be wrong)
    :return: None
    """
    sleep(3)


class MorseToLed:
    """
    Class that, when given a message in morse code and an LED interface, will communicate
    said message via the LED interface
    """

    def __init__(self, ledclass, message):
        """
        Constructor for class
        :param ledclass: interface to hardware
        :param message: string to communicate
        """
        if type(ledclass) is not LedInteraction:
            raise ValueError("Must pass LedInteraction class to init for correct interface to hardware")
        if type(message) is not str:
            raise ValueError("Must pass string to init for correct communication")
        self.__ledClass = ledclass
        self.__message = message

    def communicate_message(self):
        """
        Communicate our message using provided hardware interface
        :return:
        """
        for char in self.__message:
            if char == ".":
                self.__dot_logic()
            elif char == "-":
                self.__dash_logic()
            else:
                space_logic()

    def __dash_logic(self):
        """
        Dash stays on longer (3 seconds)
        :return: None
        """
        self.__ledClass.led_on()
        sleep(3)
        self.__ledClass.led_off()
        sleep(2)

    def __dot_logic(self):
        """
        Dash stays on shorter (1 seconds)
        :return: None
        """
        self.__ledClass.led_on()
        sleep(1)
        self.__ledClass.led_off()
        sleep(2)
