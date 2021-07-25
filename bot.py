# bot.py
import os
import discord
from datetime import datetime
from dotenv import load_dotenv
from discord.ext import commands
prefix = '.'
client = commands.Bot(command_prefix=prefix)

# Uses a .env to access it's discord token to prevent token stealing.
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Put a user ID as any of these variables to target it.
admin = 688115255301242919
ACCESS_list = [admin]

# Commands
@client.command(name="s")
async def say(message):
    if (message.author.id in ACCESS_list):
        text = message.message.content.replace(".s", "")
        await message.send(text)
        await message.message.delete()

# Jarvis
@client.event
async def on_message(message):
    msg = message.content.lower().replace(' ', '')
    if message.author == client.user:
        return
    if message.author.id in ACCESS_list:
        if msg == 'jarvis,scanthisguysballs':
            response = "His balls wack, sir."
            await message.channel.send(response)

# Run the client
client.run(TOKEN)
