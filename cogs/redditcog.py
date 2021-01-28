import discord
import asyncio
import random
import praw

from discord.ext import commands, tasks
from praw.reddit import Submission

bot = commands.Bot

#Simply a cog dedicated to posting reddit memes through PRAW into a channel.

#PRAW setup
reddit = praw.Reddit(client_id='CLIENT ID',
                     client_secret='CLIENT SECRET',
                     user_agent='USER AGENT')

#Variable to pick posts 1 through 15
random_post = random.randint(1, 15)

#The selections of subreddits to be picked from random through this variable
randomnormalsub = [
reddit.subreddit('hmmm').hot(),
reddit.subreddit('HolUp').hot(),
reddit.subreddit('blursedimages').hot(),
reddit.subreddit('okbuddyretard').hot(),
reddit.subreddit('internet_funeral').hot(),
reddit.subreddit('surrealmemes').hot(),
reddit.subreddit('comedynecromancy').hot(),
reddit.subreddit('bonehurtingjuice').hot(),
reddit.subreddit('okbuddyretard').hot(),
reddit.subreddit('okbuddybaka').hot(),
reddit.subreddit('WackyTicTacs').hot(),
reddit.subreddit('wheredidthesodago').hot()
]

#Class to work the reddit meme command
class redditposts(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #Posts a random hot pic from a random subreddit
    @commands.command(aliases=['MEME', 'm', 'M'])
    @commands.cooldown(1, 1.5, commands.BucketType.user)
    async def meme(self, ctx):
        for i in range(random_post):
            normalsubmission = next(x for x in (random.choice(randomnormalsub)) if not x.stickied)
        await ctx.send(normalsubmission.url)

def setup(bot):
    bot.add_cog(redditposts(bot))
