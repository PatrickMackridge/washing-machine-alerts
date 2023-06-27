import connect
import notification
import vibes

# Deal with vibration detection

wlan = connect.connect_to_wifi()

try:
    # vibes.run()
    notification.send_notif()
except:
    connect.handle_connection_error(wlan)
