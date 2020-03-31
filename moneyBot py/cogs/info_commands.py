import discord
from discord.ext import commands

class info_commands(commands.Cog):
    def __init__(self, client):
        self.client = client

    print("Info commands are working.")

    @commands.command(aliases=['BOT-INFO', 'bot-info', 'Bot-Info'])
    async def _bot_info(self, ctx):
        botinfo_embed = discord.Embed (
            color = discord.Color.gold(),
            title = "Bot Info"
        )
        botinfo_embed.set_thumbnail(url = "https://media.discordapp.net/attachments/667104711840628742/667105511602389007/money_logo.png")
        botinfo_embed.add_field(name = "Name", value = "moneyBot")
        botinfo_embed.add_field(name = "Version", value = "1.0.2")
        botinfo_embed.add_field(name = "Invite Link", value = "https://hitthemoney.github.io/money-bot/")
        botinfo_embed.set_footer(text = "Command: money bot_info")

        await ctx.send(embed=botinfo_embed)

    @commands.command(aliases=['SERVER-INFO', 'server-info', 'Server-Info'])
    async def server_info(self, ctx):
        server_info_embed = discord.Embed (
            color = discord.Color.gold(),
            title = "Server Info",
        )
        guildName = self.client.get_guild(ctx.guild.id)
        #server_info_embed.set_thumbnail(url = discord.Guild.icon_url) 
        server_info_embed.add_field(name = "Name", value = guildName)
        server_info_embed.add_field(name = "Member Count", value = 'Currently Broken' ) #discord.Guild.member_count
        server_info_embed.add_field(name = "Creation Date", value = 'Currently Broken' ) #discord.Guild.created_at
        server_info_embed.set_footer(text = "Command: money server_info")

        await ctx.send(embed=server_info_embed)

def setup(bot):
    bot.add_cog(info_commands(bot))