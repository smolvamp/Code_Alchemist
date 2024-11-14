@echo off
set source="source file we need user to fill some sh get that and put it here"
set destination="output where nigga same but output"

echo Backing up files from %source% to %destination%
xcopy %source% %destination% /e /i /y

echo Backup complete!
pause
