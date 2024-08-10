# Create a secrets.py with your Wifi details to be able to get the time
# when the Interstate75W isn't connected to Thonny.
#
# secrets.py should contain:
# WIFI_SSID = "Your WiFi SSID"
# WIFI_PASSWORD = "Your WiFi password"

import time
import machine
import network
import urequests

from secrets import *

# create the rtc object
rtc = machine.RTC()

# Connect to wifi and synchronize the RTC time from NTP


def sync_time():
    # Start connection
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.config(pm=0xa11140)  # Turn WiFi power saving off for some slow APs
    wlan.connect(WIFI_SSID, WIFI_PASSWORD)

    # Wait for connect success or failure
    max_wait = 100
    while max_wait > 0:
        print('waiting for connection...', wlan.status())
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        max_wait -= 1
        time.sleep(0.2)

    if max_wait > 0:
        print("Connected")
        
        r = urequests.get("https://timeapi.io/api/Time/current/coordinate?latitude=50.8&longitude=-0.1")
        # open the json data
        j = r.json()
        r.close()
        
        #rtc.datetime((j["seconds"], j["minute"], j["hour"], 1, j["day"], j["month"], j["year"]))
        rtc.datetime((j["year"], j["month"], j["day"], 0, j["hour"], j["minute"], j["seconds"], 0))

    wlan.disconnect()
    wlan.active(False)

def get_time():
    year, month, day, wd, hour, minute, second, _ = rtc.datetime()
    return hour, minute, second

