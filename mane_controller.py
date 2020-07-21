import subprocess,threading,os
import random


def run_list(setp_list):
    remove_cache()
    for setps in setp_list:
        for y,x in setps:
            tx = 131 + (x-1) * 74
            ty = 146 + (y-1) * 91
            #print ("%s -- %s %s" % (setps,tx,ty))
            #subprocess.call("adb shell input tap " + str(tx) + " " + str(ty) , shell=True)
            mane_make_echo(tx,ty)
    adb_send_run("mane_echo.sh")

def adb_send_run(filename):
    print("[*] Running script via adb ... ")
    subprocess.call("adb shell rm /sdcard/"+filename,shell=True)
    subprocess.call("adb push %s /sdcard/" %(filename),shell=True)
    subprocess.call("adb shell sh /sdcard/%s" %(filename),shell=True)

def remove_cache():
    if (os.path.exists("mane_echo.sh")):
        os.remove('mane_echo.sh')
    if (os.path.exists("mane_sendevent.sh")):
        os.remove('mane_sendevent.sh')
    if (os.path.exists("mane_dd.raw")):
        os.remove('mane_dd.raw')

def mane_make_echo(x,y):
    mane_sh = open('mane_echo.sh','a')

    mane_sh.writelines(r"echo -e -n '\x01\x02\x03\x04\x05\x06\x83\x00\x01\x00\x4A\x01\x01\x00\x00\x00' > /dev/input/event4"+'\n')
    
    sx = format(x,'x')
    sx = '0'*(4-len(sx)) + sx
    sx2 = sx[0:2]
    sx1 = sx[2:4]

    mane_sh.writelines(r"echo -e -n '\x01\x02\x03\x04\x05\x06\x83\x00\x03\x00\x35\x00\x%s\x%s\x00\x00' > /dev/input/event4" % (sx1,sx2)+'\n')
    
    sx = format(y,'x')
    sx = '0'*(4-len(sx)) + sx
    sx2 = sx[0:2]
    sx1 = sx[2:4]

    mane_sh.writelines(r"echo -e -n '\x01\x02\x03\x04\x05\x06\x83\x00\x03\x00\x36\x00\x%s\x%s\x00\x00' > /dev/input/event4" % (sx1,sx2)+'\n')
    mane_sh.writelines(r"echo -e -n '\x01\x02\x03\x04\x05\x06\x83\x00\x00\x00\x02\x00\x00\x00\x00\x00' > /dev/input/event4"+'\n')
    mane_sh.writelines(r"echo -e -n '\x01\x02\x03\x04\x05\x06\x83\x00\x00\x00\x00\x00\x00\x00\x00\x00' > /dev/input/event4"+'\n')
    mane_sh.writelines(r"echo -e -n '\x01\x02\x03\x04\x05\x06\x2D\x00\x00\x00\x02\x00\x00\x00\x00\x00' > /dev/input/event4"+'\n')
    mane_sh.writelines(r"echo -e -n '\x01\x02\x03\x04\x05\x06\x2D\x00\x00\x00\x00\x00\x00\x00\x00\x00' > /dev/input/event4"+'\n')
    mane_sh.writelines(r"echo -e -n '\x01\x02\x03\x04\x05\x06\xCD\x00\x01\x00\x4A\x01\x00\x00\x00\x00' > /dev/input/event4"+'\n')
    mane_sh.writelines(r"echo -e -n '\x01\x02\x03\x04\x05\x06\xCD\x00\x03\x00\x35\x00\x00\x00\x00\x00' > /dev/input/event4"+'\n')
    mane_sh.writelines(r"echo -e -n '\x01\x02\x03\x04\x05\x06\xCD\x00\x03\x00\x36\x00\x00\x00\x00\x00' > /dev/input/event4"+'\n')
    mane_sh.writelines(r"echo -e -n '\x01\x02\x03\x04\x05\x06\xCD\x00\x00\x00\x02\x00\x00\x00\x00\x00' > /dev/input/event4"+'\n')
    mane_sh.writelines(r"echo -e -n '\x01\x02\x03\x04\x05\x06\xCD\x00\x00\x00\x00\x00\x00\x00\x00\x00' > /dev/input/event4"+'\n')
    mane_sh.close()


def mane_make_sh_sendevent(x,y):
    mane_sh = open('mane_sendevent.sh','a+')
    mane_sh.writelines("sendevent /dev/input/event4 1 330 1"+'\n')
    mane_sh.writelines("sendevent /dev/input/event4 3 53 %s" % (x)+'\n')
    mane_sh.writelines("sendevent /dev/input/event4 3 54 %s" %(y) +'\n')
    mane_sh.writelines("sendevent /dev/input/event4 0 2 0"+'\n')
    mane_sh.writelines("sendevent /dev/input/event4 0 0 0"+'\n')
    mane_sh.writelines("sendevent /dev/input/event4 0 2 0"+'\n')
    mane_sh.writelines("sendevent /dev/input/event4 0 0 0"+'\n')
    mane_sh.writelines("sendevent /dev/input/event4 1 330 0"+'\n')
    mane_sh.writelines("sendevent /dev/input/event4 3 53 0"+'\n')
    mane_sh.writelines("sendevent /dev/input/event4 3 54 0"+'\n')
    mane_sh.writelines("sendevent /dev/input/event4 0 2 0"+'\n')
    mane_sh.writelines("sendevent /dev/input/event4 0 0 0"+'\n')
    mane_sh.close()

def mane_make_go(x,y):
    mane_go = open('mane_dd.raw','ab+')
    random_seed = random.randint(0,254)

    pre = [1,2,3,4,5,6,random_seed%250,0,1,0,int('4a',16),1,1,0,0,0]
    mane_go.write(bytearray(pre))

    sx = format(x,'x')
    sx = '0'*(4-len(sx)) + sx
    sx2 = sx[0:2]
    sx1 = sx[2:4]


    pre = [1,2,3,4,5,6,random_seed%250,0,      3,0,int('35',16),0,   int(sx1,16),int(sx2,16),  0,0] # x
    mane_go.write(bytearray(pre))

    sx = format(y,'x')
    sx = '0'*(4-len(sx)) + sx
    sx2 = sx[0:2]
    sx1 = sx[2:4]

    pre = [1,2,3,4,5,6,random_seed%250,0,      3,0,int('36',16),0,    int(sx1,16),int(sx2,16),   0,0] # y
    mane_go.write(bytearray(pre))

    pre = [1,2,3,4,5,6,random_seed%250,0,      0, 0, 2, 0, 0, 0, 0, 0 ] 
    mane_go.write(bytearray(pre))

    pre = [1,2,3,4,5,6,random_seed%250,0,      0, 0, 0, 0, 0, 0, 0, 0 ] 
    mane_go.write(bytearray(pre))

    random_seed = random.randint(0,254)

    pre = [1,2,3,4,5,6,random_seed%250,0,      0, 0, 2, 0, 0, 0, 0, 0 ] 
    mane_go.write(bytearray(pre))

    pre = [1,2,3,4,5,6,random_seed%250,0,      0, 0, 0, 0, 0, 0, 0, 0 ] 
    mane_go.write(bytearray(pre))

    random_seed = random.randint(0,254)

    pre = [1,2,3,4,5,6,random_seed%250,0,1,0,int('4a',16),1,0,0,0,0]
    mane_go.write(bytearray(pre))

    pre = [1,2,3,4,5,6,random_seed%250,0,      3,0,int('35',16),0,0,0,0,0]
    mane_go.write(bytearray(pre))

    pre = [1,2,3,4,5,6,random_seed%250,0,      3,0,int('36',16),0,0,0,0,0]
    mane_go.write(bytearray(pre))

    pre = [1,2,3,4,5,6,random_seed%250,0,      0, 0, 2, 0, 0, 0, 0, 0 ] 
    mane_go.write(bytearray(pre))

    pre = [1,2,3,4,5,6,random_seed%250,0,      0, 0, 0, 0, 0, 0, 0, 0 ] 
    mane_go.write(bytearray(pre))

    mane_go.close()
