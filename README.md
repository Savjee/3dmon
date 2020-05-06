# 3dmon

A simple Python script that monitors the print status of my Prusa i3 MK3 printer and reports it to Home Assistant.

Runs on a Raspberry Pi Zero W, powered by [TinyCore Linux](http://tinycorelinux.net). It's lightweight, boots in seconds and id sd-card-corruption-proof™️.

What it looks like in Home Assistant (paired up with an IP camera):
![](https://savjee.github.io/3dmon/screenshot.png)

Notification when the printer is done:
![](https://savjee.github.io/3dmon/screenshot-notification.jpg)

## Motivation. Why?
I wanted a simple way to monitor my 3D printer through Home Assistant. That way I could set up automations like: notify me when the printer is almost done.

Octoprint would be ideal but it doesn't run well on a Pi Zero. So instead I connected the printer's USB interface to the Pi and monitor its serial output with Python. Progress updates are captured and sent to Home Assistant through the REST API.

Why TinyCore? It boots up in seconds and runs entirely in RAM. I can power cycle my Pi all day and won't have sd card corruption. Yay!

## Setup
TODO...

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
````
filetool.sh -b
sudo reboot
```

## License & contributions
[Licensed under MIT](LICENSE)

I'm not really good at Python (this is probably my first real project). Feel free to fix/improve my code ;)

One thing to keep in mind: this project is all about **monitoring** 3D printers. I won't accept pull requests for control logic. Just trying to keeps things simple & reliable.
