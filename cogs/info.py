import os
import discord
from discord.ext import commands
import asyncio
import json
import aiohttp
import async_timeout
import requests
import json
import collections
from random import randint

class Trader:
    def __init__(self, bot):
        self.bot = bot
        datas = {
            'user': "{}".format(os.environ.get("clever_user")),
            'key': "{}".format(os.environ.get("cleverbot_key")),
            'nick': "{}".format(os.environ.get("cl_nicker"))
        }

        url = "{}".format(os.environ.get("cl_init"))
        r = requests.post(url, json = datas)

    @commands.command(aliases = ["help"])
    async def about(self,ctx):
        '''help menu'''
        about = """**__SQUEE__**\n\n**The AE Federation's official Mascot!**"""
        helpm = """Hi, I'm Squee!\nPlease don't be frightened by my appearance, I know I'm an ugly girl but I don't bite.\nI'm the mascot here and when I am not here, I am working over at Boog's tavern.\n\nThanks for joining us!"""

        em = discord.Embed(color = 0xffd500)
        em.set_thumbnail(url = self.bot.user.avatar_url)
        em.set_author(name = "About Squee:", icon_url = "https://image.ibb.co/hRaRx8/Squee.jpg")
        em.add_field(name = "Info:", value = about, inline = False)
        em.add_field(name = "Details:", value = helpm,inline = False)
        em.set_footer(text = "|Squee|",icon_url = self.bot.user.avatar_url)
        await ctx.send(embed = em)

    @commands.command()
    async def uee(self, ctx, *, args:str = None):
        if args == None:
            return
        await ctx.trigger_typing()
        args = args.replace(" ", "%20")
        try:
            data = {
                'user': "{}".format(os.environ.get("clever_user")),
                'key': "{}".format(os.environ.get("cleverbot_key")),
                'nick': "{}".format(os.environ.get("cl_nicker")),
                'text': args
                }
            url = "{}".format(os.environ.get("cl_querytalk"))
            r = requests.post(url, json = data)
            #print(r)
            reply = json.loads(r.content)
            #print(reply)
            reply = reply["response"]
            await ctx.send(reply)
        except Exception as e:
            print(e)


def setup(bot):
    bot.add_cog(Trader(bot))
