import ctypes
import sys
import subprocess

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin(command):
    if is_admin():
        subprocess.run(command, check=True, text=True, shell=True)
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, f'"{sys.argv[0]}" "{command}"', None, 1)
        sys.exit()

command_to_run = 'schtasks /create /tn "Backupr_1" /tr "C:\\Users\\Harsh\\OneDrive\\Desktop\\Programming\\python\\backup.bat" /sc daily /st 02:00'

#special shit idk why but needed to run these kinds of tasks prevents some kind of infinite loop
if __name__ == "__main__":
    run_as_admin(command_to_run)
