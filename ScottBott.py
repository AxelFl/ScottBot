import discord
from discord.ext.commands import Bot
import random
import SecretKey


my_bot = Bot(command_prefix="S")

random_shit = ["Would you like sum fries with that?", "Tickle my bum and call me Samantha.",
               "SUCCULENT CHINESE MEEEEEAL", "DON'T TOUCH MY PENIS!", "End my saffron.", ".ass",
               "What do you call crystal clear urine? 1080pee.",
               "What's the best thing about dating a homeless girl? You can drop her off anywhere.",
               "So this guy with a premature ejaculation problem comes out of nowhere.",
               "What's Forrest Gump's computer password? 1forrest1",
               "How does NASA organize their company parties? They planet",
               "What kind of shoes do ninjas wear? Sneakers", "Why can’t a bike stand on its own? It's two tired",
               "What’s the best part about living in Switzerland? Not sure, but the flag is a big plus",
               "Atheism is a non-prophet organization.",
               "What did the doctor say to the man who caught a bladder infection? Urine trouble",
               "PMS should just be called ovary-acting.",
               "Dwarfs and midgets have very little in common.", "How do you make Holy water? Boil the hell out of it.",
               "What's the hardest part about shooting up a school? The erection"]

last_used = ""


@my_bot.event
async def on_ready():
    print("Client logged in")


@my_bot.event
async def on_message(message):
    if random.randint(1, 10) == 1:
        tts = True
    else:
        tts = False

    if "scottpromo" in message.content.lower():
        return await my_bot.send_message(message.channel, content="https://www.behance.net/scottleiker, https://soundcloud.com/scottleiker, https://www.instagram.com/scottleiker pls follow")

    if "scott" in message.content.lower():
        global random_shit
        global last_used

        while True:
            word = random.choice(random_shit)
            if word == last_used:
                pass
            else:
                last_used = word
                return await my_bot.send_message(message.channel, content=word, tts=tts)

    if "sorry" in message.content.lower():
        return await my_bot.send_message(message.channel, content="You better be")

    if "flip" in message.content.lower():
        if random.randint(1, 2) == 1:
            return await my_bot.send_message(message.channel, content="Heads")
        else:
            return await my_bot.send_message(message.channel, content="Tails")

my_bot.run(SecretKey.givekey())
