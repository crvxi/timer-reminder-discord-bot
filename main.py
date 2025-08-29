from Properties import Properties
from TimerBot import TimerBot

# Initialize Discord Bot
properties = Properties()
bot = TimerBot(properties.SERVER_ID)
bot.run(properties.TOKEN)
