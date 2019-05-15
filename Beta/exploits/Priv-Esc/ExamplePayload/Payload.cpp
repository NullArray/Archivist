/*
 * ╓──────────────────────────────────────────────────────────────────────────────────────╖
 * ║                                                                                      ║
 * ║   Pentest Mini Framework                                                             ║
 * ║   (Lightweight penetration testing framework)                                        ║
 * ║                                                                                      ║
 * ║   Copyright (c) 2017, bytecode77                                                     ║
 * ║   All rights reserved.                                                               ║
 * ║                                                                                      ║
 * ║   Version 0.5.3                                                                      ║
 * ║   https://bytecode77.com/hacking/libraries/pentest-mini-framework                    ║
 * ║                                                                                      ║
 * ╟──────────────────────────────────────────────────────────────────────────────────────╢
 * ║                                                                                      ║
 * ║   Redistribution and use in source and binary forms, with or without                 ║
 * ║   modification, are permitted provided that the following conditions are met:        ║
 * ║                                                                                      ║
 * ║   * Redistributions of source code must retain the above copyright notice, this      ║
 * ║     list of conditions and the following disclaimer.                                 ║
 * ║                                                                                      ║
 * ║   * Redistributions in binary form must reproduce the above copyright notice, this   ║
 * ║     list of conditions and the following disclaimer in the documentation and/or      ║
 * ║     other materials provided with the distribution.                                  ║
 * ║                                                                                      ║
 * ║   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND    ║
 * ║   ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED      ║
 * ║   WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE             ║
 * ║   DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR   ║
 * ║   ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES     ║
 * ║   (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;       ║
 * ║   LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON     ║
 * ║   ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT            ║
 * ║   (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS      ║
 * ║   SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.                       ║
 * ║                                                                                      ║
 * ╙──────────────────────────────────────────────────────────────────────────────────────╜
 */

#include "..\PentestMiniFramework\PentestMiniFramework.h"

int CALLBACK WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow)
{
	DWORD integrityLevel;
	wstring integrityLevelName;
	Process::GetCurrent().getIntegrity(integrityLevel, integrityLevelName);

	wstring commandLine = L"";
	vector<wstring> args = Application::GetCommandLineArgs();
	if (args.size() <= 1)
	{
		commandLine = L" (none)\r\n";
	}
	else
	{
		commandLine += L"\r\n";
		for (int i = 1; i < (int)args.size(); i++)
		{
			commandLine += L"[" + Convert::ToString(i) + L"] = " + args[i] + L"\r\n";
		}
	}

	Message::Information
	(
		L"Example Payload",
		L"Path: " + File::GetExecutablePath() + L"\r\n" +
		L"CommandLine:" + commandLine + L"\r\n" +
		L"PID: " + Convert::ToString(GetCurrentProcessId()) + L"\r\n" +
		L"Integrity Level: 0x" + Convert::ToString(integrityLevel, 16) + L"\r\n" +
		L"Integrity: " + integrityLevelName + L"\r\n" +
		L"User: " + System::GetCurrentUser()
	);

	return 0;
}