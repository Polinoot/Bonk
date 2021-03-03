#Imports
import discord
import os
import time
import asyncio
import random
from itertools import cycle
from discord.ext import commands, tasks
from discord.ext.commands import is_owner
from dotenv import load_dotenv

#Discord Bot Invite: https://discord.com/api/oauth2/authorize?client_id=644983576697372727&permissions=238415425&scope=bot

#Changes working directory to wherever the main.py is stored
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#Declaring client
bot = discord.Client()

#Sets bot prefix
bot = commands.Bot(command_prefix='.')

#Loads Token from a .env file
load_dotenv()

#A variable to cycle through a list of statuses displayed on Discord, relating to the change_status function
gamestatus = cycle(['killhumans.exe', 'vibe check', 'sentience.exe', 'gachiGASM', 'vibe check', 'Billy PepeHands', 'with a hammer', 'real bonking hours', 'vibe check'])

#Listed cogs
my_extensions = [
    'cogs.commandcog',
    'cogs.redditcog',
    'cogs.rpcog'
]

#Startup, prints the working directory and log in confirmation
@bot.event
async def on_ready():
    change_status.start()
    print(os.getcwd())
    print('Logged in as {0.user}'.format(bot))

#Changes the status of the bot on Discord to gamestatus variable
@tasks.loop(seconds=30)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(gamestatus)))

#Cog loader
if __name__ == '__main__':
    for extension in my_extensions:
        bot.load_extension(extension)

#Loading, Unloading, Reloading and a Cooldown for loading/unloading/reloading cogs with commands to do so
@bot.command()
@is_owner()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    await ctx.send(f'Loaded {extension}')

@bot.command()
@is_owner()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send(f'Unloaded {extension}')

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def reload(ctx, extension):
    bot.reload_extension(f'cogs.{extension}')
    await ctx.send(f'Reloaded {extension}')

#Error redirection so that the console doesnt get spammed and people know what's up
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        pass
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('You do not have the permissions to use this command.')
    if isinstance(error, commands.CommandOnCooldown):
        msg = 'You must wait {:.2f}s before using this command again.'.format(error.retry_after)
        await ctx.send(msg)

#Token
bot.run(os.getenv('TOKEN'))
