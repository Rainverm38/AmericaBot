# AmericaBot by Rainverm38
# More info can be found on the GitHub here: https://github.com/Rainverm38/AmericaBot

import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import datetime as DT                       # Imports datetime as DT so instead of typing 'datetime.datetime.now()' you type 'DT.datetime.now()' it saves time and looks less dumb than 'datetime.datetime.now()'
#import time                                # Doesn't appear to be working here, must be imported before the command that requires it is run.

# Checks time that bot was started
startTime = DT.datetime.now()

# Prefix to be entered before commmands. Ex. !test
bot = commands.Bot(command_prefix='!')      # In this case the prefix is '!' so before typing a command you type '!' and then 'test'
bot.remove_command('help')                  # Removes the default help command

# Notify in console when bot is loaded and sets bot currently playing status
@bot.event
async def on_ready():
    endTime = DT.datetime.now()
    await bot.change_presence(game=discord.Game(name=''))   # Sets the bot's presence
    print('--------------------------')
    timeToLoad = endTime - startTime
    currentDT = DT.datetime.now()               # Gets current time
    print('Time to load:', timeToLoad)          # Prints the time to load
    print('Current Time:', currentDT)           # Prints current time in console
    print('Done Loading!')                      # Prints 'Done Loading!' in console
    print('--------------------------')

# Adds a help command that sends a message to the user rather than spamming the chat channel
@bot.command(pass_context=True)
async def help(ctx):
    currentDT = DT.datetime.now()
    author = ctx.message.author
    embed = discord.Embed(
        color = discord.Color.gold()
    )
    embed.set_author(name='Help')
    embed.add_field(name='!help', value='Lists off commands, the accent color is gold to symbolize America\'s infinite wealth and glory.', inline=False)
    embed.add_field(name='!info', value='Tells you about the bot', inline=False)
    await bot.send_message(author, embed=embed)
    print('--------------------------')
    print('Current Time:', currentDT)
    print('Help has been run')
    print('--------------------------')

# 'Info' command
@bot.command(pass_context=True)
async def info(ctx):
    currentDT = DT.datetime.now()
    print(' ')
    await bot.say('Rainverm38 realized that there probably weren\'t any bots dedicated for the greatest country on Earth. He decided to fix that problem.') 
    print('--------------------------')
    print('Current Time:', currentDT)
    print('info has been run')
    print('--------------------------')

bot.run('TOKEN HERE')         # User defined bot token