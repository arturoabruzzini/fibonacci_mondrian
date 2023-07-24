# Create a secrets.py with your Wifi details to be able to get the time
# when the Interstate75W isn't connected to Thonny.
#
# secrets.py should contain:
# WIFI_SSID = "Your WiFi SSID"
# WIFI_PASSWORD = "Your WiFi password"

import time
import machine
import network
import ntptime

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
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        max_wait -= 1
        print('waiting for connection...')
        time.sleep(0.2)

    if max_wait > 0:
        print("Connected")

        try:
            ntptime.settime()
            print("Time set")
        except OSError:
            pass

    wlan.disconnect()
    wlan.active(False)


DAYS_IN_MONTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def isdst(month, day, wd):
    # Compute last sunday of march
    last_sunday_march = day - ((wd + 6) % 7) + 1
    if month == 3 and day < last_sunday_march:
        last_sunday_march -= 7
    while last_sunday_march + 7 <= DAYS_IN_MONTHS[month - 1]:
        last_sunday_march += 7

    # Compute last sunday of october
    last_sunday_october = day - ((wd + 6) % 7) + 1
    if month == 10 and day < last_sunday_october:
        last_sunday_october -= 7
    while last_sunday_october + 7 <= DAYS_IN_MONTHS[9]:
        last_sunday_october += 7

    # Check if we're in DST
    if month > 3 and month < 10:
        return True
    elif month == 3 and day >= last_sunday_march:
        return True
    elif month == 10 and day < last_sunday_october:
        return True
    else:
        return False


def get_time():
    year, month, day, wd, hour, minute, second, _ = rtc.datetime()
    # NTP synchronizes the time to UTC, this allows you to adjust the displayed time
    utc_offset = 1 if isdst(month, day, wd) else 0
    hour = (hour + utc_offset) % 24
    return hour, minute, second
