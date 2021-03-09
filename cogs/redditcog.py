import discord
import asyncio
import random
import os
import praw
from dotenv import load_dotenv

from discord.ext import commands, tasks
from praw.reddit import Submission

bot = commands.Bot

load_dotenv()

#PRAW setup
redditclientid = (os.getenv('REDDITCLIENTID'))
clientsecret = (os.getenv('REDDITCLIENTSECRET'))
useragent = (os.getenv('REDDITUSERAGENT'))

reddit = praw.Reddit(client_id = redditclientid,
                     client_secret = clientsecret,
                     user_agent = useragent,
                     check_for_async=False)

#Variable to pick posts 1 through 25
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

class redditposts(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #Posts a random hot() pic from a random subreddit
    @commands.command(aliases=['MEME', 'm', 'M'])
    @commands.cooldown(1, 1.5, commands.BucketType.user)
    async def meme(self, ctx):
        for i in range(random_post):
            normalsubmission = next(x for x in (random.choice(randomnormalsub)) if not x.stickied)
        await ctx.send(normalsubmission.url)

def setup(bot):
    bot.add_cog(redditposts(bot))
