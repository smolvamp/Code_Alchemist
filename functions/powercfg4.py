import ctypes
import sys
import subprocess
import os

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin(command):
    if is_admin():
        subprocess.run(command, check=True, text=True)
    else:
        params = f'"{command}"'
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, f'"{sys.argv[0]}" {params}', None, 1)
        sys.exit()

command_to_run = ['powercfg', '/batteryreport']
run_as_admin(command_to_run)

battery_report_path = os.path.join(os.getcwd(), 'battery-report.html')

if os.path.exists(battery_report_path):
    os.startfile(battery_report_path)
else:
    print("Battery report not found. Make sure the 'powercfg' command ran successfully.")
