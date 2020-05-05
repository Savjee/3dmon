#monitor.sh
#make sure a process is always running.

# Quit if the process is still running, no need to do anything!
if ps ax | grep -v grep | grep "main.py" > /dev/null
then
    echo "Still running...";
    exit
fi

# If there is no internet connection, stop and wait for next minute!
if ping -q -c 1 -W 1 google.com >/dev/null; then
  echo "The network is up"
else
  echo "The network is down. Trying to reconnect..."
  sudo wifi.sh -a
  exit 1
fi

nohup /home/tc/main.py 2>&1 > /tmp/3dmon.log
