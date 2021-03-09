import discord
from discord.ext import *
from discord.ext.commands import Bot
import asyncio
import time
import random

from discord.ext import commands, tasks

bot = commands.Bot

#I do not know how to do Object Oriented Programming so this is my best shot at a class full of commands
class commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #Commands
    
    #Purge command to delete messages
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount=1):
        if amount>10:
            await ctx.send('Too much to purge.', delete_after=3)
        if amount<=10:
            await ctx.channel.purge(limit=amount+1)
            await ctx.send(f'Purged {amount} messages.', delete_after=3)

    #Echos what the issuing person had said
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def say(self, ctx, *, message=" "):
        await ctx.send(message)

    @commands.command()
    async def bhb(self, ctx):
        await ctx.send('Yes, I am on.')

    @commands.command()
    async def help(self, ctx):
        author = ctx.message.author
        embed = discord.Embed(color = discord.Colour.blurple())
        embed.set_author(name="Here's the list for Bonk's commands!")
        embed.add_field(name = 'Normal Commands', value = '-----------------------', inline = False)
        embed.add_field(name = '.purge', value = 'Purges up to 10 messages or less if specified.\n Use as `.purge (amount of messages up to 10)`.', inline = False)
        embed.add_field(name = '.say', value = 'Repeats whatever you say.\n Beware, this can repeat anything and is locked to only those with the manage messages perm.\n Use as `.say (whatever message you want to repeat)`.', inline = False)
        embed.add_field(name = '.bhb', value = 'A command used to see if the bot is online.\n Use as `.bhb`.', inline = False)
        embed.add_field(name = '.help', value = 'This command! You just used it.\n Use as `.help`.', inline = False)
        embed.add_field(name = 'Reddit Commands', value = '----------------------', inline = False)
        embed.add_field(name = '.meme (also used as .m, .M, .MEME', value = 'Posts a random meme from Reddit!\n Use as `.meme`.', inline = False)
        embed.add_field(name = '.porn (also used as .p, .P, .PORN, .sex, .horny)', value = 'Posts a random porn pic from Reddit!\n Use as `.porn`.', inline = False)
        await author.send(embed=embed)
        await ctx.send('Check your DMs!')

def setup(bot):
    bot.add_cog(commands(bot))
