from config import LOG_GROUP_ID
from NekoUserBot import bot, neko

if __name__ == "__main__":
    neko.start()
    bot.run()
    with bot:
        bot.send_message(f"{LOG_GROUP_ID}", "Nyaa Neko Ready Boi!")
