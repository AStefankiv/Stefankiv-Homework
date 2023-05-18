## HW 1, 2

class Bot:
    def __init__(self, name):
        self.name = name

    def send_message(self, message):
        print(message)

    def say_name(self):
        return self.name


# HW 5 (type)
    Bot = type(
        "Bot", (),
        {"send_message": send_message,
         "say_name": say_name,
         "number": 1})

class TelegramBot(Bot):
    url = None
    chat_id = None

    def set_url(self, url):
        self.url = url

    def set_chat_id(self, chat_id):
        self.chat_id = chat_id

    def send_message(self, message):
        print(f"{self.name} bot says {message} to chat {self.chat_id} using {self.url}")


# HW 5 (type)
    TelegramBot = type('TelegramBot', (Bot,), {
        'url': None,
        'chat_id': None,
        'set_url': set_url,
        'set_chat_id': set_chat_id,
        'send_message': send_message
    })


some_bot = Bot('Marvin')
print(some_bot.say_name())

some_bot.send_message("Hello")

telegram_bot = TelegramBot("TG")
print(telegram_bot.say_name())

telegram_bot.send_message('Hello')

telegram_bot.set_chat_id(1)
telegram_bot.send_message('Hello')


## HW 3
class MyStr(str):
    def __str__(self):
        return self.upper()

my_str = MyStr('test')
print(my_str)

## HW 4
class User:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if isinstance(other, User):
            return self.name.lower() == other.name.lower()
        return False

first_user = User('OLEKSII')
second_user = User('Oleksii')
print(first_user == second_user)