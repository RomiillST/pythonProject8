class User():
    def __init__(self, update):
        try:
            self.user_id = update.message.chat_id
            self.text = update.message.text
        except Exception:
            self.user_id = update.qallback_query.from_user.id

    def bervor(self):
        return self.user_id, self.text