import connect
import notification
import config as c


# Deal with vibration detection

wlan = connect.connect_to_wifi(c.ssid, c.password)

try:
    notification.send_notif()
except:
    connect.handle_connection_error(c.ssid, c.password, wlan)
