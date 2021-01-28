import discord
import asyncio
import random
import praw

from discord.ext import commands, tasks
from praw.reddit import Submission

bot = commands.Bot

#This entire cog is dedicated to the same function as redditcog.py, however, selects only from a list of porn subs to post images in an nsfw channel
#I have attempted to combine this into the redditcog.py but miserably fails at every attempt
#Plus its easier to reload the cogs individually in case something goes wrong

#PRAW setup
reddit = praw.Reddit(client_id='CLIENT ID',
                     client_secret='CLIENT SECRET',
                     user_agent='USER AGENT')

#Variable to pick posts 1 through 25
random_post = random.randint(1, 15)

#List of porn subs
randompornsub = [
reddit.subreddit('rule34').hot(),
reddit.subreddit('suicidegirls').hot(),
reddit.subreddit('AsianHotties').hot(),
reddit.subreddit('thighdeology').hot(),
reddit.subreddit('BustyPetite').hot(),
reddit.subreddit('hentai').hot(),
reddit.subreddit('NSFW_GIF').hot(),
reddit.subreddit('bigtiddygothgf').hot(),
reddit.subreddit('besthqporngifs').hot(),
reddit.subreddit('AnimeMILFS').hot(),
reddit.subreddit('2Booty').hot(),
reddit.subreddit('gothsluts').hot(),
reddit.subreddit('SnowWhites').hot(),
reddit.subreddit('pawg').hot(),
reddit.subreddit('TittyDrop').hot(),
reddit.subreddit('BiggerThanYouThought').hot(),
reddit.subreddit('AsiansGoneWild').hot(),
reddit.subreddit('AsianHotties').hot(),
reddit.subreddit('AsianHottiesGIFS').hot(),
reddit.subreddit('AsianPorn').hot()
]

#Class to work the reddit porn command
class rp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #Posts a random hot pic from a random porn subreddit
    @commands.command(aliases=['p', 'P', 'PORN', 'sex', 'horny'])
    @commands.cooldown(1, 1.5, commands.BucketType.user)
    @commands.is_nsfw()
    async def porn(self, ctx):
        for i in range(random_post):
            pornsubmission = next(x for x in (random.choice(randompornsub)) if not x.stickied)
        await ctx.send(pornsubmission.url)

def setup(bot):
    bot.add_cog(rp(bot))