import network
import time


def connect_to_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)

    # Wait for connect or fail
    max_wait = 10
    while max_wait > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        max_wait -= 1
        print('waiting for connection...')
        time.sleep(1)

    # Handle connection error
    if wlan.status() != 3:
        raise RuntimeError('network connection failed')
    else:
        print('connected')
        status = wlan.ifconfig()
        print('ip = ' + status[0])
    return wlan


def handle_connection_error(ssid, password, wlan):
    print("could not connect")
    if wlan.status() < 0 or wlan.status() >= 3:
        print("trying to reconnect...")
        wlan.disconnect()
        wlan.connect(ssid, password)
        if wlan.status() == 3:
            print('connected')
        else:
            print('failed')
