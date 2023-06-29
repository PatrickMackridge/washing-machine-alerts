from machine import Pin
import notification
import time


def is_finished(vibrate):
    for i in range(300):
        if vibrate.value() == 0:
            return False
        else:
            time.sleep(1)
    return True


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
                time.sleep(1)
            else:
                finished = is_finished(vibrate)
                if finished:
                    print('Washing Done!')
                    notification.send_notif()
                    running = False
    return
