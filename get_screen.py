import subprocess,os

def take_screen():
    print("[*] Taking screenshot ...")
    out = subprocess.getoutput("adb shell screencap -p | sed 's/\r$//' > screen.png")
    if (out.find("error")!=-1):
        print("[*] Adb error :")
        print(out)
        exit()

    if (os.path.getsize('screen.png')<10):
        print("[*] Error on screen.png size.")
        exit()
    print("[+] Take a screenshot")

