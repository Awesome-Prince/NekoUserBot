from config import LOG_GROUP_ID
from NekoUserBot import neko, bot
import NekoUserBot.plugins


if __name__ == "__main__":
   neko.start()
   tbot.run()
   bot.run()
   with bot:
            bot.send_message(f"{LOG_GROUP_ID}", "Nyaa Neko Ready Boi!")

