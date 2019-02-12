# Developers Note
As it stands this project is very outdated and can use some major changes and updates. I am planning a complete re-write in the not too distant future.

~~!UPDATE: As of the time of writing, the new and much more improved version will be ready in a week.~~ 

UPDATE II: It's been a little more than a week but i have a bad habit of underestimating the workload and the time i have available. The new version is a complete rewrite and it will come with numerous interesting features. And new C2 mechanisms. A release is imminent. I have moved on to debugging the new keylogger and working out some final issues. Look forward to a release soon.

Sorry for the delays, to be honest i usually tend to be working on several projects at a time, some private some public. Unfortunatelyu this divides my attention and i am left with less time to contribute to the Open Source community.

Bear with me while i work out the final details, thank you for your understanding.



### Keylogger
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
