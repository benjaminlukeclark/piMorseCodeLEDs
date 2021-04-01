from LedInteraction import LedInteraction
from time import sleep

print("test start")
LedClass = LedInteraction("capsLock")
LedClass.led_on()
sleep(5)
LedClass.led_off()
print("test end")