import discord
from discord.ext import commands


class Say(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    async def is_owner(ctx):
        return ctx.author.id == 280271578850263040


    @commands.command()
    @commands.check(is_owner)
    async def sendText(self, ctx,channelid:str = None,text:str=None):
        try:
            if channelid==None or text == None:
                await ctx.send("`Provide ID!`")
                return
            else:
                k=self.bot.get_channel(id = int(channelid))
                print(k)
                await k.send("{}".format(text))
        except Exception as e:
            print(e)







def setup(bot):
    bot.add_cog(Say(bot))
