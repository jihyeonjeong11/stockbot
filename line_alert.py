import requests

#메세지를 보냅니다.
def SendMessage(msg):
    try:

        TARGET_URL = 'https://notify-api.line.me/api/notify'
        TOKEN = 'Q7zAJsl4R5gEldD9ndSuxrhhuk7yMeopFHiJ4eqWn8T' #여러분의 값으로 변경

        response = requests.post(
            TARGET_URL,
            headers={
                'Authorization': 'Bearer ' + TOKEN
            },
            data={
                'message': msg
            }
        )

    except Exception as ex:
        print(ex)