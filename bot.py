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
            response = "Their balls wack, sir."
            await message.channel.send(response)
        if 'jarvis,scantheballsof' in msg:
            msg = msg.replace('jarvis,scantheballsof', '')
            msg = int(msg.strip('<>!@'))
            print(msg)
            time.sleep(0.5)
            response = "Yes sir, commencing ball scan..."
            await message.channel.send(response)
            time.sleep(3)
            if msg == 688115255301242919:
                response = "Leafesque's balls are massive. They read as `2%` wack, sir."
            elif msg == 517122589718741022:
                response = "23rd President's balls are `23%` wack, sir."
            elif msg == 221756292862050314:
                response = "Afanguy's balls are `0%` wack, sir."
            elif msg == 546400083311067137:
                response = "Seha's balls are enormous, sir. Readings say `12%` wack."
            elif msg == 593223812980670493:
                response = "Bug's balls are seemingly irrelevant to the context, sir."
            elif msg == 436985877806317586:
                response = "Callisuni's balls are from space, referred to as spaceballs. Readings say `30%` wack."
            elif msg == 346393655432445954:
                response = "Redditor balls, sir."
            elif msg == 347198887309869078:
                response = "His balls wack, sir. Readings say `57%` wack."
            elif msg == 703732414119411792:
                response = "Turkish balls, sir."
            elif msg == 868744451244302346:
                response = "My database contains all possible balls in the universe, making them the most wack balls, sir."
            elif msg == 318151890405687296:
                response = "Furry balls, sir. `103%` wack, readings show."
            elif msg == 242220086713122816:
                response = "His balls are deep, sir. Readings show `37%` wack."
            elif msg == 443527170392850434:
                response = "Helix balls, sir."
            elif msg == 645668447967117332:
                response = "His balls wack, sir. They seem to like men."
            elif msg == 665882081343307794:
                response = "Apologies sir, his balls are too tiny to scan."
            elif msg == 306966483911704586:
                response = "Loli in username, sir."
            elif msg == 454735636956577803:
                response = "Balls slightly wack, sir. Readings show `17%`."
            elif msg == 538479146679140362:
                response = "Greek balls, sir. `67%` wack."
            elif msg == 441052235967889430:
                response = "Funny balls, sir. Very wack."
            elif msg == 402026123086528518:
                response = "His balls are holy, sir."
            elif msg == 244517712032825344:
                response = "Readings show `27%` wack, sir. That number seems to multiply past 8PM."
            elif msg == 453227223693131777:
                response = "Racist balls, sir."
            elif msg == 288481819173584898:
                response = "Inconsistent balls, sir. Readings say very wack."
            elif msg == 624738893543243786:
                response = "Worldbuilder balls, sir. `39%` wack."
            elif msg == 538182631074955294:
                response = "Rubber balls, sir. `13%` wack."
            elif msg == 703543391530647664:
                response = "Locus balls, sir."
            elif msg == 169564270277820417:
                response = "His balls have Thaumcraft taint, sir. Readings say `47%` wack."
            elif msg == 607408346668204032:
                response = "Their ball hair seems to be attributed to someone named 'Gabe', sir."

            await message.channel.send(response)


    if msg == 'https://tenor.com/view/jarvis-gif-21248397':
        time.sleep(1)
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
