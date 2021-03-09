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
