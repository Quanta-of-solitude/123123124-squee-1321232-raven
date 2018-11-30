import os
import discord
from discord.ext import commands
import asyncio
import requests
from bs4 import BeautifulSoup


class squeechat:

    def __init__(self,bot):

        self.bot = bot

    def get_response(self, text):
        try:
            text = text.replace(' ', '+')
            r = requests.get("{}".format(os.environ.get("botlib"))+"{}".format(text)+"&application={}&offensive=false".format(os.environ.get("appidlb")))

            soup = BeautifulSoup(r.content, 'lxml')
            f_data = soup.find("message")
            response = f_data.text
            return response
        except Exception as e:
            print(e)

    @commands.command()
    async def hi(self, ctx, *, args:str = None):
        if args == None:
            return
        await ctx.trigger_typing()
        text = args
        args = args.replace(' ', '+')
        print(args)
        try:
            lst = ["who are you?", "who are you", "what is your name", "what is your name?", "whatr is ur name?", "what is ur name"]

            if text in lst:
                response = "I am squee! :D"
            else:
                response = self.get_response(args)

            await ctx.send(response)
        except Exception as e:
            print(e)

def setup(bot):
	bot.add_cog(squeechat(bot))
