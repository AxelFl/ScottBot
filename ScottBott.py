import discord
from discord.ext.commands import Bot
import random
import SecretKey


my_bot = Bot(command_prefix="S")

random_shit = ["Would you like sum fries with that?", "Tickle my bum and call me Samantha.",
               "SUCCULENT CHINESE MEEEEEAL", "DON'T TOUCH MY PENIS!", "End my saffron.", ".ass"]

last_used = ""


@my_bot.event
async def on_ready():
    print("Client logged in")


@my_bot.event
async def on_message(message):
    if "scott" in message.content.lower():
        global random_shit
        global last_used

        while True:
            word = random.choice(random_shit)
            if word == last_used:
                pass
            else:
                last_used = word
                return await my_bot.send_message(message.channel, content=word, tts=True)

    if "sorry" in message.content.lower():
        return await my_bot.send_message(message.channel, content="You better be")


my_bot.run(SecretKey.givekey())
