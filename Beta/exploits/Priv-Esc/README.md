# Performance Monitor Volatile Environment LPE

| Exploit Information |                                   |
|:------------------- |:--------------------------------- |
| Publish Date        | 28.06.2017                        |
| Patched             | Windows 10 RS3 (16299)            |
| Target              | Microsoft Windows                 |
| exploit-db          | N/A                               |
| CVE                 | N/A                               |
| Versions            | Windows 7-10, x86/x64 independent |

## Description

perfmon.exe (Performance Monitor) is an auto-elevated binary that executes
mmc.exe with the path to "perfmon.msc" as commandline argument. It is there to
auto-elevate only Performance Monitor, but the Management Console itself does
not auto-elevate.

Now, let's take a look at the disassembly of the data section:

![](https://bytecode77.com/images/sites/hacking/exploits/uac-bypass/performance-monitor-privilege-escalation/disassembly.png)

This indicates, that mmc.exe will be executed from a path that contains an
environment variable (%systemroot%), thus making it vulnerable to environment
variable injection.

How to change `%systemroot%`?

Simple: Through Volatile Environment.

Define your own %systemroot% in `HKEY_CURRENT_USER\Volatile Environment`
and perfmon.exe will look for mmc.exe there instead. This makes the exploit
particularly interesting as no DLL is required, at all. No injection, no
hijacking, we can just name our payload "mmc.exe" and it will be executed with
high IL.

After executing perfmon.exe, our bogus "mmc.exe" is executed, which makes it
also completely independend from:

* x86 or x64 bit target
* Native or managed code - both can be used
* Basically, any other files - we might as well copy the current executable to "mmc.exe" and re-use it this way!

In this example, Payload.exe will be started, which is an exemplary payload file
displaying a MessageBox.

## Expected Result

When everything worked correctly, Payload.exe should be executed, displaying
basic information including integrity level.

Executing either one of the x64 or x86 binaries on a 64-bit operating system
will work. This means, the x86 binary will work everywhere, while the x64 built
executable will only work on a 64-bit operating system.

These two screenshots show both x86 and x64 binaries executed on a 64-bit
operating system. As you see, the x86 binary causes a second commandline
argument to get passed to "mmc.exe".

![](https://bytecode77.com/images/sites/hacking/exploits/uac-bypass/performance-monitor-privilege-escalation/result/001_x86.png)
![](https://bytecode77.com/images/sites/hacking/exploits/uac-bypass/performance-monitor-privilege-escalation/result/002_x64.png)

## Downloads

Compiled binaries with example payload:

[![](https://bytecode77.com/images/shared/fileicons/zip.png) PerformanceMonitorVolatileEnvironmentLPE rev1 Binaries.zip](https://bytecode77.com/downloads/hacking/exploits/uac-bypass/PerformanceMonitorVolatileEnvironmentLPE%20rev1%20Binaries.zip)

## Project Page

[![](https://bytecode77.com/images/shared/favicon16.png) bytecode77.com/hacking/exploits/uac-bypass/performance-monitor-privilege-escalation](https://bytecode77.com/hacking/exploits/uac-bypass/performance-monitor-privilege-escalation)