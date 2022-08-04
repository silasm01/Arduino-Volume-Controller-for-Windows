# Arduino-Volume-Controller

## How to set up AVM.
1. Download [arduino-sketch.ino](https://github.com/silasm01/Arduino-Volume-Controller/blob/main/arduino/arduino-sketch/arduino-sketch.ino).
2. Edit [arduino-sketch.ino](https://github.com/silasm01/Arduino-Volume-Controller/blob/main/arduino/arduino-sketch/arduino-sketch.ino) to add or remove analog pins from ``potInputs[]`` to match your pin setup.
3. Upload [arduino-sketch.ino](https://github.com/silasm01/Arduino-Volume-Controller/blob/main/arduino/arduino-sketch/arduino-sketch.ino) to your Arduino.
4. Download both files from [python](https://github.com/silasm01/Arduino-Volume-Controller/tree/main/python) directory and edit [settings.yaml](https://github.com/silasm01/Arduino-Volume-Controller/blob/main/python/settings.yaml) to fit your setup.
#### Optional: Run on startup.
> This currently only cover Windows.
1. Copy the [main.pyw](https://github.com/silasm01/Arduino-Volume-Controller/blob/main/python/main.pyw) file path.
2. Press ``Win + r`` and type ``shell:startup`` to open startup folder.
3. Create a shortcut using the [main.pyw](https://github.com/silasm01/Arduino-Volume-Controller/blob/main/python/main.pyw) file path and done.
