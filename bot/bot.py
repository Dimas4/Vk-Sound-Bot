import time

from initialize_backend.initialize import initialize


def start(token, backend, filename):
    bot = initialize(token, backend)

    while True:
        messages = bot.get_unread_messages()
        if messages["count"] >= 1:
            id, body = bot.get_message_and_id(messages)
            bot.convert_text_to_voice(body)
            uploaded_voice = bot.upload_file(filename, id)
            bot.send_message(id, attach=uploaded_voice)
        time.sleep(1)
