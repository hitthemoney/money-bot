import discord
from discord.ext import commands
import time

class april_fools_commands(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    print("April fools commands are working.")

    @commands.command(pass_context = True, aliases=['WARN', 'Warn',' warn', 'warN', 'WARNN', 'Warnn', 'warnn'])
    @commands.has_permissions(kick_members = True)
    async def warn(self, ctx, name: discord.Member, *, reason = None):
        messageAuthor = ctx.message.author
        moneyBot = await self.client.fetch_user(679160569965576192)        
        if name == messageAuthor:
            await ctx.send("""**{} you can not ban yourself :man_facepalming:**""".format(messageAuthor))
        elif name == moneyBot:
            await ctx.send("""**{} you can not ban me :man_facepalming:**""".format(messageAuthor))
        else:
            done = False
            await ctx.send("""**You will be banned in 10 seconds {}. 
Reason: {}**""".format(name, reason))
            guild = self.client.get_guild(ctx.guild.id)
            channel = await name.create_dm()
            await channel.send("""**You will be banned from {} in 10 seconds
Reason: {}**""".format(guild, reason))
            now = time.time()
            future = now + 10
            while done == False:
                if time.time() == future:
                    await ctx.send("""**{} was banned. 
Reason: {}**""".format(name, reason))
                    guild = self.client.get_guild(ctx.guild.id)
                    channel = await name.create_dm()
                    await channel.send("""**You were banned from {}
Reason: {}**""".format(guild, reason))
                    done = True

def setup(bot):
    bot.add_cog(april_fools_commands(bot))