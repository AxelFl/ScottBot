from discord.ext.commands import Bot
import random
import SecretKey
import asyncio
import discord
import time

# Start the bot object
my_bot = Bot(command_prefix="S")

# All the things to say
jokes = ["Would you like sum fries with that?", "Tickle my bum and call me Samantha.",
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

# List used to not repeat the same things again
# Makes the choice function less random
last_used = []


# When the bot is ready
@my_bot.event
async def on_ready():
	# discord.opus.load_opus()
	print("Client logged in")


# For every message that the bot sees
@my_bot.event
async def on_message(message):
	# Add a 1 in 10 chance to activate the text to speech functionality on discord
	# This is to not annoy the chat all too often with tts messages
	# This feature is only used in the scott command and promo
	if random.randint(1, 10) == 1:
		tts = True
	else:
		tts = False

	# Send Scott's promo on the command "scottpromo"
	if "scottpromo" in message.content.lower():
		return await my_bot.send_message(message.channel, content="https://www.behance.net/scottleiker, "
		                                                          "https://soundcloud.com/scottleiker, "
		                                                          "https://www.instagram.com/scottleiker pls follow",
		                                 tts=tts)

	# Activate the message sending if "scott" is in the message
	if "scott" in message.content.lower():
		global jokes
		global last_used

		while True:
			# Pick a random word
			word = random.choice(jokes)
			# Repick a word if it was the latest used word
			# Else just pick another word
			if word not in last_used:
				# Reclassify the latest used and send the message
				# If it is a short list just append the word
				# Else remove the first one and add a new one
				if len(last_used) > 5:
					last_used.pop(0)
					last_used.append(word)
				else:
					last_used.append(word)
				return await my_bot.send_message(message.channel, content=word, tts=tts)

	# Stupid sorry message
	if "sorry" in message.content.lower():
		return await my_bot.send_message(message.channel, content="You better be")

	# Simple coin flip
	if "flip" in message.content.lower():
		# 50/50 random choice
		if random.randint(1, 2) == 1:
			return await my_bot.send_message(message.channel, content="Heads")
		else:
			return await my_bot.send_message(message.channel, content="Tails")

	if "test" in message.content.lower():
		in_voice = message.author.voice.voice_channel
		if in_voice is not None:
			VoiceClient = await my_bot.join_voice_channel(message.author.voice.voice_channel)
			player = await VoiceClient.create_ytdl_player("https://www.youtube.com/watch?v=aRsWk4JZa5k")
			player.start()
			await asyncio.sleep(player.duration)
			return await VoiceClient.disconnect()

		else:
			print("nah fam")

	# if "STOP" in message.content:
	# 	try:
	# 		await VoiceClient.disconnect()
	# 	except UnboundLocalError:
	# 		return await my_bot.send_message(message.channel, content="I'm not connected")


# External function to hide my discord bot's token
my_bot.run(SecretKey.givekey())
