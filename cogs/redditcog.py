import discord
import asyncio
import random
import praw

from discord.ext import commands, tasks

bot = commands.Bot

#PRAW setup
reddit = praw.Reddit(client_id='REDDITCLIENTID',
                     client_secret='REDDITAPPLICATIONSECRET',
                     user_agent='REDDITUSERAGENT')

#Variable to pick posts 1 through 30
random_post = random.randint(1, 25)

#The selections of subreddits to be picked from random through this variable
randomsub = [
reddit.subreddit('dankmemes').hot(),
reddit.subreddit('hmmm').hot(),
reddit.subreddit('HolUp').hot(),
reddit.subreddit('blursedimages').hot(),
reddit.subreddit('okbuddyretard').hot(),
reddit.subreddit('internet_funeral').hot(),
reddit.subreddit('surrealmemes').hot(),
reddit.subreddit('youngpeopleyoutube').hot()
]

class reddit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #Posts a random hot or top pic from a random subreddit
    @commands.command(aliases=['MEME', 'm', 'M'])
    async def meme(self, ctx):
        for i in range(random_post):
            submission = next(x for x in (random.choice(randomsub)) if not x.stickied)
        await ctx.send(submission.url)

def setup(bot):
    bot.add_cog(reddit(bot))