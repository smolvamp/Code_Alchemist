@echo off
REM Create the LabConfig key
reg add "HKEY_LOCAL_MACHINE\SYSTEM\Setup\LabConfig" /f

REM Add the BypassSecureBootCheck DWORD value
reg add "HKEY_LOCAL_MACHINE\SYSTEM\Setup\LabConfig" /v BypassSecureBootCheck /t REG_DWORD /d 1 /f


REM Add the BypassTPMCheck DWORD value
reg add "HKEY_LOCAL_MACHINE\SYSTEM\Setup\LabConfig" /v BypassTPMCheck /t REG_DWORD /d 1 /f


echo Registry keys and values have been added.
pause
