# Android-auto-play-lianliankan
Using python to play lianliankan in android.

**No updates without big bug or important issues.**

## Install Environment

Install the basic controller in ubuntu.

* Python 3 and pip3
* Opencv
* Adb
* skimage.measure

```bash
sudo apt-get install python3 python3-pip
sudo pip3 install opencv-python
sudo apt-get install adb
sudo apt-get install python-skimage
```

## Android environment

An Android environment provides an **ADB interface**.

You can use 夜神 simulator, 雷电 simulator to run android 5+.

### APK Download

* [Google play](https://play.google.com/store/apps/details?id=com.tcw.ConnectFun&hl=en_US)
* [Apkpure](https://apkpure.com/mahjong-connect-fun/com.tcw.ConnectFun)

## Run it

1. Open you game and connect adb in ubuntu via adb command line.
2. Run adb shell in terminal if no error you can continue.
3. Choose Hard mode and Choose Animate mode in Game.
4. Run `python3 main.py` in terminal to auto play this Game.

## Screenshot

![](https://raw.githubusercontent.com/Mane-Network-Team/Android-auto-play-lianliankan/master/screenshot/1.png)