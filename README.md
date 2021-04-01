# piMorseCodeLEDs
Made to translate strings to morse code, then communicate these via LEDs on a keyboard (provided it's hooked up to a raspberry pi)

Made whilst studying [TM129](http://www.open.ac.uk/courses/modules/tm129) for no other reason than I thought it'd be neat to do and help me a little with some lower-level conceptual understanding.

```bash
----------------------------------------------------------------------------------------------------
pi@raspberry:~ $ sudo python3 /media/sf_TM129/Github/piMorseCodeLEDs/piMorseCodeLEDs/main.py --help
----------------------------------------------------------------------------------------------------
Python script for Raspberry Pi to communicate strings via keyboard LEDs

By Sudoblark (https://github.com/sudoblark)

Strings are first translated to morse code then communication in dot-dash notation via a chosen LED

Accepted args:
--help shows this message

--led %ARG% sets led to use, admissible input is: scrollLock, capsLock, numLock

--message %ARG% determines message to encode and sent

Example
python3 main.py --led capsLock --message SOS
python3 main.py --led capsLock --message 'Hello World'

----------------------------------------------------------------------------------------------------
pi@raspberry:~ $ 
```

# install
1. Clone to a Raspberry Pi
```bash
git clone https://github.com/sudoblark/piMorseCodeLEDs
```
2. Run help if you're stuck
```bash
python3 /media/sf_TM129/Github/piMorseCodeLEDs/piMorseCodeLEDs/main.py --help
```

3. Run script in sudo to do some morse code translation
_Note_: Requires sudo to access the i/o items
```bash
pi@raspberry:~ $ sudo python3 /media/sf_TM129/Github/piMorseCodeLEDs/piMorseCodeLEDs/main.py --led capsLock --message 'Hello World'
----------------------------------------------------------------------------------------------------
Python script for Raspberry Pi to communicate strings via keyboard LEDs

By Sudoblark (https://github.com/sudoblark)

Message: Hello World   |   LED: capsLock

----------------------------------------------------------------------------------------------------
```
