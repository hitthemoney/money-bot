import discord
from discord.ext import commands


class help_commands(commands.Cog):
    def __init__(self, client):
        self.client = client

    print("Help commands are working.")

    @commands.command(aliases=['HELPP', 'HELP', 'Help', 'Helpp', 'helpp', 'help.', 'HELP.', 'Help.'])
    async def help(self, ctx):
        await ctx.send("""```fix
Commands:
- money help; brings you to this page
- money warn <user> <reason>; warns a user (only works if you can kick members)
- money kick <user> <reason>; kicks a user (only works if you can kick members)
- money ban <user> <reason>; bans a user (only works if you can ban members)
- money unban <user id> <bool (True reinvites the member and False does not)>; unbans a user (only works if you can ban members)
- money mute <user> <reason>; makes a user unable to chat (only works if you can kick members, and have setup a role called "muted" (case sensitive))
- money unmute <user> <reason>; unmutes a muted user (only works if you can kick members, and have the "muted" role)
- money yt; my YouTube channel
- money twitch; my Twitch channel
- money website; my website
- money bot-info; the bot information including invite link
- money server-info; the server info (Note this command is currently broken)

WORKING ON: fixing money server_info```""")

def setup(bot):
    bot.add_cog(help_commands(bot))