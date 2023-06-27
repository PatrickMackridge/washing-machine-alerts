import ujson
import urequests
import config as c


def send_notif():

    headers = {
        "Access-Token": c.auth_token,
        "Content-Type": "application/json"
    }

    data = ujson.dumps({
        'type': 'note',
        'title': c.notif_title,
        'body': c.notif_body,
        'device_iden': c.device_iden
    })

    print("sending...")
    response = urequests.post(c.url, headers=headers, data=data)
    print("sent: " + str(response.status_code))
    response.close()
