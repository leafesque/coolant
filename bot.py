# bot.py
import os
import discord
import random
import time
from datetime import datetime
from dotenv import load_dotenv
from discord.ext import commands
prefix = '.'
client = commands.Bot(command_prefix=prefix)
status_movies = ["Iron Man", "Iron Man 2", "Iron Man 3", "Finding Nemo 11", "Spaceballs", "1992 space movie", "family guy", "a pornography starring your mother.", "you sleep!", "you always!", "danny devito make pasta", "cock rating 1!", "cock rating 2!", "cock rating 2 reloaded!", "cock rating 3!", "cock rating 4!", "cock rating 5!", "cock rating 6!", "cock rating 7!", "cock rating 8!", "cock rating 9!", "cock rating 10!", "cock rating 99!", "balls rating!", "balls rating 2!", "for bopa; death on sight", "yormit make shit brownies", "seha make great brownies", "seha make pizza", "for the pizza", "for omori gifs; death on sight", "for mittence; do the funny voice", "the alloy discord server"]

# Uses a .env to access it's discord token to prevent token stealing.
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Put a user ID as any of these variables to target it.
admin = 688115255301242919
ACCESS_list = [admin]

# Log Print
async def log_print(text):
    print(text)
    with open('log.txt', 'a') as log_file:
        log_file.write(text + "\n")

# Ready
@client.event
async def on_ready():
    await log_print('[' + datetime.now().strftime("%x %X") + ']' + ' ' + f'{client.user} has connected to Discord!')
    
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=random.choice(status_movies)))

# Jarvis
@client.event
async def on_message(message):
    msg = message.content.lower().replace(' ', '')
    if message.author == client.user:
        return
    if message.author.id in ACCESS_list:
        if msg == 'jarvis,scanthisguysballs':
            time.sleep(0.5)
            response = "Yes sir, commencing ball scan..."
            await message.channel.send(response)
            time.sleep(2)
            response = "His balls wack, sir."
            await message.channel.send(response)
    if msg == 'https://tenor.com/view/jarvis-gif-21248397':
        time.sleep(0.5)
        response = "https://tenor.com/view/jarvis-gif-21248407"
        await message.channel.send(response)
    await client.process_commands(message)

# Commands
@client.command(name="s")
async def say(message):
    if (message.author.id in ACCESS_list):
        text = message.message.content.replace(".s", "")
        await message.send(text)
        await message.message.delete()
        await log_print('[' + datetime.now().strftime("%x %X") + ']' + ' Said \"' + text + '\"!')

@client.command(name="cst")
async def change_status(message):
    if (message.author.id in ACCESS_list):
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=random.choice(status_movies)))
        await message.message.delete()
        await log_print('[' + datetime.now().strftime("%x %X") + ']' + ' Recycled status message!')

@client.command(name='op')
async def op(message, text):
    if (message.author.id == admin):
        strippedtext = int(text.strip('<>!@'))
        ACCESS_list.append(strippedtext)
        await message.message.delete()
        strippedtext = str(strippedtext)
        await log_print('[' + datetime.now().strftime("%x %X") + ']' + ' Gave \"' + strippedtext + '\" permissions!')

@client.command(name='deop')
async def deop(message, text):
    if (message.author.id == admin):
        strippedtext = int(text.strip('<>!@'))
        ACCESS_list.remove(strippedtext)
        await message.message.delete()
        strippedtext = str(strippedtext)
        await log_print('[' + datetime.now().strftime("%x %X") + ']' + ' Took away \"' + strippedtext + '\"\'s permissions!')


# Run the client
client.run(TOKEN)
