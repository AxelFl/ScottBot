from discord.ext.commands import Bot
import SecretKey
import asyncio

# Start the bot object
my_bot = Bot(command_prefix="S")

# Delay in voice usage for a better experience
delay = 0.5


# When the bot is ready
@my_bot.event
async def on_ready():
	print("Client logged in")


# For every message that the bot sees
@my_bot.event
async def on_message(message):

	if "carey" in message.content.lower():
		in_voice = message.author.voice.voice_channel
		if in_voice is not None:
			voice_client = await my_bot.join_voice_channel(message.author.voice.voice_channel)
			try:
				while 1:
					player = await voice_client.create_ytdl_player("https://www.youtube.com/watch?v=yXQViqx6GMY")
					player.start()
					await asyncio.sleep(player.duration + delay)
			except:
				return await voice_client.disconnect()

	if "STOPP" in message.content:  # Used to remove Scott from a channel if he is not leaving
		in_voice = message.author.voice.voice_channel  # Channel Author is in, NONE type if not connected
		if in_voice is not None:  # If the Author is in a voice channel
			# Create the voice client
			voice_client = await my_bot.join_voice_channel(message.author.voice.voice_channel)
		return await voice_client.disconnect()  # Leave the channel

# External function to hide my discord bot's token
my_bot.run(SecretKey.givekey())
