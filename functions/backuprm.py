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
            subprocess.run(command, check=True,text=True)
    else:
        params = f'"{command}"'
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, f'"{sys.argv[0]}" {params}', None, 1)
        sys.exit()

command_to_run = 'schtasks /delete /tn "Backupr_1"'
#special shit idk why but needed to run these kinds of tasks
if __name__ == "__main__":
 run_as_admin(command_to_run)