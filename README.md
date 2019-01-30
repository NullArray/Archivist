# Note
As it stands this project is outdated and can use major changed and updates. I am planning a complete re-write in the not too distant future.


## Keylogger
A python keylogger that sends its logs to gmail and attempts to add a registry entry for persistence. You'll need to allow less secure apps from the options in gmail to receive your logs.

Furthermore you will need the pyHook and pythoncom modules for this to work. I've included a requirements file for convenience as well.

## Usage

To use the keylogger simply change the values of the following variables:

```
USER
PASS
TO
```

To your specifications, and compile the script to exe with pyinstaller for distribution. Please use the --noconsole and --onefile flags when compiling.

This is an adaptation of the original authored by ajinabraham https://github.com/ajinabraham
