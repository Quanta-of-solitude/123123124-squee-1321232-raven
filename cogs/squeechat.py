import os
import discord
import json
from discord.ext import commands
import asyncio
import requests


class squeechat(commands.Cog):

    def __init__(self,bot):

        self.bot = bot
        self.client = discord.Client()
        datas = {
            'user': "{}".format(os.environ.get("clever_user")),
            'key': "{}".format(os.environ.get("cleverbot_key")),
            'nick': "{}".format(os.environ.get("cl_nicker"))
        }

        url = "{}".format(os.environ.get("cl_init"))
        r = requests.post(url, json = datas)

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
            await ctx.send("`Internal chatbot error, sorry\n\n      -Noble`")
            print(e)

def setup(bot):
	bot.add_cog(squeechat(bot))
