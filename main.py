import connect
import vibes

# Deal with vibration detection

wlan = connect.connect_to_wifi()

try:
    vibes.run()
except:
    connect.handle_connection_error(wlan)
