# 3dmon

A simple Python script that monitors the print status of my Prusa i3 MK3 printer and reports it to Home Assistant.

Runs on a Raspberry Pi Zero W, powered by [TinyCore Linux](http://tinycorelinux.net). It's lightweight, boots in seconds and is sd-card-corruption-proof™️.

What it looks like in Home Assistant (paired up with an IP camera):
![](https://savjee.github.io/3dmon/screenshot.png)

Notification when the printer is done:
![](https://savjee.github.io/3dmon/screenshot-notification.jpg)

## Motivation. Why?
I wanted a simple way to monitor my 3D printer through Home Assistant. That way I could set up automations like: notify me when the printer is almost done.

Octoprint would be ideal but it doesn't run well on a Pi Zero. So instead I connected the printer's USB interface to the Pi and monitor its serial output with Python. Progress updates are captured and sent to Home Assistant through the REST API.

Why TinyCore? It boots up in seconds and runs entirely in RAM. I can power cycle my Pi all day and won't have sd card corruption. Yay!

## Setup

1. Download the latest version of Tiny Core Linux ( available at: http://tinycorelinux.net/downloads.html )
2. Copy the operating system to the SD card ( instructions at: https://www.raspberrypi.org/documentation/installation/installing-images/)
3. Insert your SD card and boot your device - you will need a keyboard and screen for this step
4. Complete basic install for Tiny Core Linux - available online or TinyCoreLinux-Setup.md
5. Connect to a network
6. To set the correct time, you need to modify the NTP server, using the following command:
```
sudo vi /etc/sysconfig/ntpserver
```
6. As Tiny Core Linux runs in RAM, all changes are lost unless the folders/files are added to a list, the following command will ensure the NTP server is kept:
```
echo /etc/sysconfig/ntpserver >> /opt/.filetool.lst
filetool.sh -b
```
7. Then reboot your device (sudo reboot) and when your device has rebooted, entering the following command should show you the correct time:
```
date
```
> If your time is not updating, run the following command to force an update:
```
sudo getTime.sh
```
8. Configure the current repository to install packages:
```
sudo vi /opt/tcemirror
```
> Change the only line in this file to: http://distro.ibiblio.org/tinycorelinux

9. Next you need to install python and the required modules:
```
tce-load -wi python3.8
tce-load -wi py3.8serial
tce-load -wi usb-serial-5.10.16-piCore
tce-load -wi firmware-rpi-wifi
tce-load -wi wifi
```
> **Hint** - you can use the following command to search for packages:
```
tce-ab
```
10. Install additional Python modules
```
pip3.8 install requests

```
<!-- FUTURE pip3.8 install paho-mqtt -->
11. Save your changes
```
echo /usr/local/lib/python3.8/site-packages/serial >> /opt/.filetool.lst
filetool.sh -b
```
12. **Optional** - Reboot device and open python to check all the modules are available:
```
python3

import serial
import requests
import json
```
<!-- FUTURE import paho.mqtt.client as mqtt -->

### Setup crontab on Tinycore
Add this to `/opt/bootlocal.sh` to start cron:

```
crond -L /dev/null 2>&1
```

Make sure that crontabs are persisted. Run: 

```
echo var/spool/cron >> /opt/.filetool.lst
```

Backup & reboot:
```
filetool.sh -b
sudo reboot
```

## License & contributions
[Licensed under MIT](LICENSE)

I'm not really good at Python (this is probably my first real project). Feel free to fix/improve my code ;)

One thing to keep in mind: this project is all about **monitoring** 3D printers. I won't accept pull requests for control logic. Just trying to keeps things simple & reliable.
