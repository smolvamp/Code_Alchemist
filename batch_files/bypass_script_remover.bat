@echo off
REM Delete the BypassTPMCheck DWORD value
reg delete "HKEY_LOCAL_MACHINE\SYSTEM\Setup\LabConfig" /v BypassTPMCheck /f

REM Delete the BypassSecureBootCheck DWORD value
reg delete "HKEY_LOCAL_MACHINE\SYSTEM\Setup\LabConfig" /v BypassSecureBootCheck /f

REM Delete the LabConfig key
reg delete "HKEY_LOCAL_MACHINE\SYSTEM\Setup\LabConfig" /f

echo Registry keys and values have been removed.
pause
