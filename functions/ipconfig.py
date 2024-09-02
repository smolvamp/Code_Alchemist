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
        with open("Ipconfigr.txt","w") as file2:
            subprocess.run(command, check=True,text=True,stdout=file2)
            file2.close()
    else:
        params = f'"{command}"'
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, f'"{sys.argv[0]}" {params}', None, 1)
        sys.exit()

command_to_run = 'ipconfig'

run_as_admin(command_to_run)
