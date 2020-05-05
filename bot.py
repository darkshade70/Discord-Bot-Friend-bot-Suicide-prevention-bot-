import discord  # Importing all necessary libraries and modules
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import os
import asyncio
from itertools import cycle
import time
import random
import dialogflow
from google.api_core.exceptions import InvalidArgument

# Dialog flow setup

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'private_key.json'

DIALOGFLOW_PROJECT_ID = 'newagent-vualpy'
DIALOGFLOW_LANGUAGE_CODE = 'en'
SESSION_ID = 'me'

session_client = dialogflow.SessionsClient()
session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)

messages = 0  # Setting messages varialbe to 0
joined = 0  # Setting joined variable to 0
enabled = False
# id = 666695108535779416                      #Server id. Important for counting k-users command.


statusMsg = ['Let the dawn protect you',  # List of custom status messages
             'I will be by your side <3',
             'To succeed means to accept failure',
             'Your limitation--It is only your imagination',
             'Always dream big',
             'Even the heaviest doors can be opened',
             'There is a potato chip ony my shoulder',
             'Nep-Nep-Nep-Nep-Nep',
             'Lettuce, be friends',
             'Are you made of Copper and Tellurium? Cause I think your CuTe :sunglasses:',
             'If you were a flower, Id pick you',
             'One, two, three, four...uhh what comes after again?',
             'Its not like I want to be friends or anything... >_<',
             "It's not about finishing first, it's about finishing together",
             "Hand in hand we'll win the fight!"]

jokes = ["Whats the best thing about Switzerland?\nI dont know but the flag is a big plus. Ba Dum tschh"
         ":rofl::laughing:",
         "I just invented a new word. It's called plagiarism. :rofl::laughing:",
         "Did you hear about the mathematician who is afraid of negative number?\n"
         "He'll stop at nothing to avoid them. :rofl::laughing:",
         "Why do we tell actors to break a leg?\n"
         "Because every play has a CAST. :rofl::laughing:",
         "Have you heard about the restaurant called karma?\n"
         "There's no menu, you get what you deserve. :rofl::laughing:",
         "A woman in labour suddenly shouted, shouldn't, wouldn't, couldn't, didn't, can't\n"
         "The doctor said don't worry, those are just contractions. :rofl::laughing:",
         "You don't need a parachute to go sky diving\n"
         "You need a parachute to go skydiving twice. :rofl::laughing:",
         "Parallel lines have so much in common. To bad they'll never meet. :rofl::laughing:"]

greetings = ["Let's have a nice chat ^-^",
             'You wanted to talk? Me too!',
             "Welcome, I see you want to talk :)",
             "Chat command enabled, friend cap is on. Giving my full attention c:",
             "Chit Chat time :smile:"]

scores = []

client = commands.Bot(command_prefix='k-')  # Setting the bot prefix to k-
client.remove_command('help')


@client.event  # When bot is online print bot is ready in console
async def on_ready():
    """When bot is ready or online print bot is ready in console"""
    print('Bot is Ready')


async def change_status():
    """Chnages the bot status and cycles through unique statuses periodically"""
    await client.wait_until_ready()
    Status = cycle(statusMsg)

    while True:
        await asyncio.sleep(6)
        newStatus = next(Status)
        await client.change_presence \
            (activity=discord.Activity(type=discord.ActivityType.watching, name="ᗩᑎᎥᗰᗴ | " + newStatus))


@client.event  # First event
async def update_stats():
    """Logs server information os people joined and messages sent periodically"""
    await client.wait_until_ready()
    global messages, joined

    while not client.is_closed():
        try:
            with(open("stats.txt", "a")) as f:
                f.write(f'|Server Stats| Time: {int(time.time())}, Number Of Messages Sent: {messages},'
                        f' Number Of Members Joined: {joined}\n')

                messages = 0
                joined = 0
                await asyncio.sleep(15)

        except Exception as j:
            print(j)
            await asyncio.sleep(15)


@client.event
async def on_member_join(member):
    """When new member joins send a unique welcome message (DM) Also counts for new members that joined"""
    greetings = ['Hello there!',
                 'Greetings there ^-^',
                 'Its nice to meet you!',
                 'Lets get along and have a fun time :)',
                 'A new friend to make :D']

    global joined
    joined += 1
    await member.send(f'{random.choice(greetings)}{member.mention}\n')

    greeting = open("intro.txt")
    greetings = greeting.read()
    greeting.close()
    await member.send(greetings)


@client.event
async def on_message(message):
    """This is for custom commands. So far includes user count command and prints logged information about serer"""
    if message.author == client.user:
        return
    if message.author.bot: return

    global messages
    global enabled
    messages += 1
    ID = client.get_guild(666695108535779416)
    # chatbot command
    if enabled:
        if message.content == 'k-end':
            enabled = False
            await message.channel.send(f"Cya, until next time, have a nice day ^-^")
        else:
            text_to_be_analyzed = message.content
            text_input = dialogflow.types.TextInput(text=text_to_be_analyzed, language_code=DIALOGFLOW_LANGUAGE_CODE)
            query_input = dialogflow.types.QueryInput(text=text_input)
            try:
                response = session_client.detect_intent(session=session, query_input=query_input)
            except InvalidArgument:
                raise

            """
            print("Query text:", response.query_result.query_text)
            print("Detected intent:", response.query_result.intent.display_name)
            print("Detected intent confidence:", response.query_result.intent_detection_confidence)
            """
            await message.channel.send(response.query_result.fulfillment_text)  # Sends bot response

    if message.content == 'k-users':  # Counts the number of users in specific server
        await message.channel.send(f'# of Members: {ID.member_count} beautiful people ^-^')

    elif message.content == 'k-stats':
        stat = open("stats.txt")
        stats = stat.read()[0:1868]
        stat.close()
        await message.channel.send(f"Printing the past 20 documented lines")
        await message.channel.send(f'Here are the server stats:')
        await message.channel.send(stats)

    elif message.content == 'k-joke':
        await message.channel.send(f"Here is a funny joke ^-^\n{random.choice(jokes)}")

    elif message.content == 'k-info':
        info = open('devInfo.txt')
        allInfo = info.read()
        info.close()
        await message.channel.send(allInfo)

    elif message.content == 'k-chat':
        enabled = True
        await message.channel.send(f"{random.choice(greetings)}")

    elif message.content.split()[0] == "k-rate":
        if message.content.split()[1].isdigit():
            rating = int(message.content.split()[1])
            if 1 <= rating <= 100:
                with open("ratings.txt", "a") as r:
                    r.write(f'\n{rating}')
                await message.channel.send(f'Thank you for you input ^-^')
            else:
                await message.channel.send(f'Please input a number from 1-100')
        else:
            await message.channel.send(f'Please make sure it is a number from 1-100')\

    elif message.content == 'k-help':
        botCommandInfo = open('allBotCommands.txt')
        commandInfo = botCommandInfo.read()
        botCommandInfo.close()
        await message.channel.send(f"{commandInfo}")

    elif message.content.split()[0] == 'k-feedback':
        if message.content.split('k'):
            feedback = message.content
            with open("feedback.txt", "a") as f:
                f.write(f'{feedback}\n')
        await message.channel.send(f'Thank you for your feedback! ^-^')

    elif message.content == 'k-rating':
        with open('ratings.txt', 'r') as r:
            scores = list(map(int, r.read().split('\n')))
            averageRating = int(sum(scores) / len(scores))
            await message.channel.send(f"The average user rating for Kiona is {averageRating}%")
            for i in range(1, len(scores)):
                startValue = scores[i]
                position = i
                while position > 0 and scores[position - 1] > startValue:
                    scores[position] = scores[position - 1]
                    position = position - 1
                    scores[position] = startValue
            median = int(len(scores) / 2)
            print(scores[median])
            await message.channel.send(f"The median number is {scores[median]}")

    elif message.content == 'k-test':
        await message.channel.send(f"Testing")

    elif message.content.split()[0] == "k-search":
        if message.content.split()[1].isdigit():
            with open('ratings.txt', 'r') as r:
                scores = list(map(int, r.read().split('\n')))
                found = False
                inp = int(message.content.split()[1])
                for x in scores:
                    if x == int(inp):
                        found = True
                        break
                if found:
                    await message.channel.send(f'Match found. Some one gave Kiona a {inp}% rating')
                if not found:
                    await message.channel.send(f'no match found. No one gave Kiona a {inp}% rating yet')

    await client.process_commands(message)


# Allows us to upload and load files from cogs
@client.command()
@has_permissions(manage_server=True)
async def load(ctx, extension):
    """Allows for loading of files in the cogs folder without having to restart the bot"""

    client.load_extension(f'cogs.{extension}')


@client.command()
@has_permissions(manage_server=True)
async def unload(ctx, extension):
    """Allows for unloading of files in the cogs folder without having to restart the bot"""

    client.load_extension(f'cogs{extension}')


for filename in os.listdir('./cogs'):  # This goes through the cogs folder and loads the files
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


@load.error
async def kick_error(error, ctx):
    if isinstance(error, MissingPermissions):
        await ctx.send(f'Sorry, you do not have permissions')


client.loop.create_task(change_status())
client.loop.create_task(update_stats())
client.run('bot token')
