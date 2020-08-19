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
    
    #List of insults for users to insult themselves with bot
    @commands.command(aliases=['bugreport'])
    async def insultme(self, ctx):
        insults = [
            "{ctx.author} is my favorite person besides every other person I’ve ever met.",
            "I envy people who have never met {ctx.author}",
            "{ctx.author} is kinda like Rapunzel except instead of letting down their hair, they let down everyone in their life.",
            "{ctx.author} is impossible to underestimate.",
            "If {ctx.author} was an inanimate object, they'd be a participation trophy.",
            "Take my lowest priority and put {ctx.author} beneath it.",
            "Such a shame {ctx.author}'s mother didn’t swallow them.",
            "People like {ctx.author} are the reason God doesn’t talk to us anymore.",
            "If {ctx.author} was a potato they'd be a stupid potato.",
            "I’d call {ctx.author} a cunt, but they have neither the warmth or the depth.",
            "{ctx.author}'s birth certificate is an apology letter from the condom factory.",
            "{ctx.author}'s face is so oily that I’m surprised America hasn’t invaded yet.",
            "You’re the reason your mom swallows now.",
            "{ctx.author} could fuck up a wet dream.",
            "I want you to be the pallbearer at my funeral so you can let me down one last time.",
            "If you could suck your own dick then you would finally suck at everything.",
            "You’ll never be half the man your mother was.",
            "{ctx.author} smells like they wipe back to front.",
            "I could agree with you, but then we’d both be wrong.",
            "You are the human embodiment of an eight-dollar haircut.",
            "You’re about as important as a white crayon.",
            "You look like you have weiners in your butt.",
            "The only thing that will ever fuck you is life.",
            "You’re so inbred you’re a sandwich.",
            "Fuck your entire fuckin' life, bud.",
            "Give your balls a tug, ya tit fucker."
            "you fool. you absolute buffoon. you think you can challenge me in my own realm? you think you can rebel against my authority? you dare come into my house and upturn my dining chairs and spill coffee grounds in my Keurig? you thought you were safe in your chain mail armor behind that screen of yours. I will take these laminate wood floor boards and destroy you. I didn’t want war. but i didn’t start it."
            ]
        await ctx.send(random.choice(insults).format(ctx=ctx))

    #Purge command to delete messages
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount=1):
        if amount>10:
            toomuchpurge = await ctx.send('Too much to purge.', delete_after=3)
        if amount<=10:
            await ctx.channel.purge(limit=amount+1)
            await ctx.send(f'Purged {amount} messages.', delete_after=3)

def setup(bot):
    bot.add_cog(commands(bot))