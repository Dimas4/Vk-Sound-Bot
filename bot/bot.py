import time

from initialize_backend.initialize import initialize


def start(token, backend):
    bot = initialize(token, backend)

    while True:
        messages = bot.get_unread_messages()
        if messages["count"] >= 1:
            id, body = bot.get_message_and_id(messages)
            if body.lower() == "привет":
                bot.send_message(id, "Привет")
        time.sleep(1)
