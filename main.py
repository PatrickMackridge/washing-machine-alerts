import connect
import notification


# Deal with vibration detection

wlan = connect.connect_to_wifi()

try:
    notification.send_notif()
except:
    connect.handle_connection_error(wlan)
