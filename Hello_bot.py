# Jokebot v1
# Work with Python 3.6
import discord
from jokes import*

TOKEN = 'Your token here'
client = discord.Client()
channel = client.get_channel(#Your channel here)

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith("Tell me a joke"):
        await message.channel.send('I heard you! {0.name}'.format(message.author))
        await message.channel.send('I can tell... wholesome jokes for now.')
        await message.channel.send('Type Wholesome with a capital "w" to hear one.')

    if message.content.startswith("Wholesome"):
        await message.channel.send(wholesome())

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
