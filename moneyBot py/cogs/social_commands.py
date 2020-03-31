import discord
from discord.ext import commands

class social_commands(commands.Cog):
    def __init__(self, client):
        self.client = client

    print("Social commands are working.")

    @commands.command(aliases=['youtube', 'YT', 'Youtube', 'Yt', 'yT', 'YouTube', 'YOUTUBE'])
    async def yt(self, ctx):
        await ctx.send('Go check out: https://www.youtube.com/channel/UCtWQuDxHtgq_wY7AxuxM__w?')
    @commands.command(aliases=['TWITCH', 'Twitch', 'twiCH', 'TwiCH', 'Twichh', 'TWITCHH', 'twitchh'])
    async def twitch(self, ctx):
        await ctx.send('Go check out: https://twitch.tv/hitthemoney')
    @commands.command(aliases=['Website', 'WEBSITE', 'webste', 'Web', 'web', 'WEB', 'wwebsite'])
    async def website(self, ctx):
        await ctx.send('My official website is, https://hitthemoney.github.io/')

def setup(bot):
    bot.add_cog(social_commands(bot))