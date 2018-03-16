from discord.ext.commands import Bot
import random
import SecretKey
import asyncio
import discord
import time

# Start the bot object
my_bot = Bot(command_prefix="S")

# When the bot is ready
@my_bot.event
async def on_ready():
	# discord.opus.load_opus()
	print("Client logged in")


# For every message that the bot sees
@my_bot.event
async def on_message(message):

	if "@everyone" in message.content.lower():
		return await my_bot.send_file(message.channel, "can_u_dont.jpg")


# External function to hide my discord bot's token
my_bot.run(SecretKey.givekey())
