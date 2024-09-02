import ctypes
import sys
import subprocess
import time
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin(command):
    if is_admin():
        with open("chkdsk.txt","a") as file2:
            while True:
                subprocess.run(command, check=True,text=True,stdout=file2)
                file2.write("/n---/n")
                file2.flush()
                time.sleep(1)            
    else:
        params = f'"{command}"'
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, f'"{sys.argv[0]}" {params}', None, 1)
        sys.exit()

command_to_run = 'chkdsk'

run_as_admin(command_to_run)
