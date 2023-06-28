from machine import Pin
import notification
import time


def run():
    running = False
    finished = False
    vibrate = Pin(16, Pin.IN, Pin.PULL_DOWN)
    while not finished:
        if vibrate.value() == 0:
            print("Washing Started!")
            running = True
        while running:
            if vibrate.value() == 0:
                print("washing...")
                time.sleep(1)
            else:
                time.sleep(300)
                if vibrate.value() == 1:
                    print("Washing Done!")
                    running = False
                    notification.send_notif()
                    finished = True
                    break
    if finished:
        return
