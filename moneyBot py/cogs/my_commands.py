import discord
from discord.ext import commands
from datetime import datetime

class my_commands(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    @commands.is_owner()
    async def shutdown(self, ctx):
        messageAuthor = ctx.message.author
        now = datetime.now()
        currentTime = now.strftime("%H:%M:%S")
        print("moneyBot was shutdown by {} at {}".format(messageAuthor, currentTime))
        await ctx.send("**moneyBot is now shutting down**")
        await ctx.bot.logout()

def setup(bot):
    bot.add_cog(my_commands(bot))
