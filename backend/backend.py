from .generate_vk_instance.generate_instance import generate_instance


class VkBot:
    def __init__(self, token):
        self.token = token
        self.vk = generate_instance(token)

    def get_unread_messages(self, offset=0, count=20):
        return self.vk.method("messages.getConversations", {"offset": offset, "count": count, "filter": "unread"})

    def send_message(self, id, message):
        self.vk.method("messages.send", {"peer_id": id, "message": message})

    @staticmethod
    def get_message_and_id(messages):
        return messages["items"][0]["last_message"]["from_id"], messages["items"][0]["last_message"]["text"]
