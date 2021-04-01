import subprocess


def run_bash_command(cmd):
    subprocess.Popen(["/bin/bash", "-c", cmd + "&> /dev/null"])


class LedInteraction:
    """
    Turn on/off LED depending on init params
    """
    ledTypes = ("scrollLock", "capsLock", "numLock")

    def __init__(self, led):
        """
        Constructor for class
        :param led: Determines which led will be turned on/off by class
        :type led: str: scrollLock, capsLock, numLock
        """

        if led not in self.ledTypes:
            raise ValueError("led must be one of: scrollLock, capsLock, numLock")
        else:
            self.__led_type = led

        self.__scrollLockChange = "sudo tee /sys/class/leds/input0\:\:scrolllock/brightness"
        self.__capsLockChange = "sudo tee /sys/class/leds/input0\:\:capslock/brightness"
        self.__numLockChange = "sudo tee /sys/class/leds/input0\:\:numlock/brightness"

        self.__led_on = "echo 1"
        self.__led_off = "echo 0"

    def led_on(self):
        """
        Turns LED on
        :return: None
        """
        if self.__led_type == "scrollLock":
            run_bash_command(self.__led_on + " | " + self.__scrollLockChange)
        elif self.__led_type == "capsLock":
            run_bash_command(self.__led_on + " | " + self.__capsLockChange)
        elif self.__led_type == "numLock":
            run_bash_command(self.__led_on + " | " + self.__numLockChange)
        else:
            raise ValueError("self.__led_type is not of expected type, please check that __init__ was successful")

    def led_off(self):
        """
        Turns LED off
        :return: None
        """
        if self.__led_type == "scrollLock":
            run_bash_command(self.__led_off + " | " + self.__scrollLockChange)
        elif self.__led_type == "capsLock":
            run_bash_command(self.__led_off + " | " + self.__capsLockChange)
        elif self.__led_type == "numLock":
            run_bash_command(self.__led_off + " | " + self.__numLockChange)
        else:
            raise ValueError("self.__led_type is not of expected type, please check that __init__ was successful")
