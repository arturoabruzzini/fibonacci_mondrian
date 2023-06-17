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

try:
    from secrets import WIFI_SSID, WIFI_PASSWORD
    wifi_available = True
except ImportError:
    print("Create secrets.py with your WiFi credentials to get time from NTP")
    wifi_available = False

# create the rtc object
rtc = machine.RTC()


def sync_time():
    # Connect to wifci and synchronize the RTC time from NTP
    if not wifi_available:
        get_time()
        return

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
            get_time()
        except OSError:
            pass

    wlan.disconnect()
    wlan.active(False)


# Get the current date and time
year, month, day, wd, hour, minute, second, _ = rtc.datetime()

DAYS_IN_MONTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def isdst():
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
    global year, month, day, wd, hour, minute, second

    year, month, day, wd, hour, minute, second, _ = rtc.datetime()
    # NTP synchronizes the time to UTC, this allows you to adjust the displayed time
    utc_offset = 1 if isdst() else 0
    return year, month, day, wd, (hour + utc_offset) % 24, minute, second
