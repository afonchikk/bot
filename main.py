import requests
import datetime

class BotHandler:

    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def get_updates(self, offset=None, timeout=2):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_last_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = None

        return last_update

token = "550084421:AAEVq90RNA64BkELxXd9jqy-iVlQ2Z_yP20"

greet_bot = BotHandler(token)
greetings = ('hello', 'hi', 'greetings', 'sup')
now = datetime.datetime.now()


def main():
    new_offset = None
    today = now.day
    hour = now.hour


    while True:

        greet_bot.get_updates(new_offset)


        last_update = greet_bot.get_last_update()
        if last_update != None:
            last_update_id = last_update['update_id']
            last_chat_text = last_update['message']['text']
            last_chat_id = last_update['message']['chat']['id']
            last_chat_name = last_update['message']['chat']['first_name']


            greet_bot.send_message(last_chat_id, 'Hi, {}! Thank you for supporting CHAOEX community. We are here to answer whatever '
                                                 'questions you may have.'.format(last_chat_name))

            new_offset = last_update_id + 1




if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()