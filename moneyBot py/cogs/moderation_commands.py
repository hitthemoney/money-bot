import discord
from discord.ext import commands

class moderation_commands(commands.Cog):
    def __init__(self, client):
        self.client = client

    print("Moderation commands are working.")

    @commands.command(pass_context = True, aliases=['WARN', 'Warn',' warn', 'warN', 'WARNN', 'Warnn', 'warnn'])
    @commands.has_permissions(kick_members = True)
    async def warn(self, ctx, name: discord.Member, *, reason = None):
        messageAuthor = ctx.message.author
        moneyBot = await self.client.fetch_user(679160569965576192)        
        if name == messageAuthor:
            await ctx.send("""**{} you can not warn yourself :man_facepalming:**""".format(messageAuthor))
        elif name == moneyBot:
            await ctx.send("""**{} you can not warn me :man_facepalming:**""".format(messageAuthor))
        else:
            await ctx.send("""**You have been warned {}. 
Reason: {}**""".format(name, reason))
            guild = self.client.get_guild(ctx.guild.id)
            channel = await name.create_dm()
            await channel.send("""**You were warned from {}
Reason: {}**""".format(guild, reason))

    @commands.command(pass_context = True, aliases=['Kick','KICK','KICKK','Kickk','kickk'])
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, name: discord.Member, *, reason = None):
        messageAuthor = ctx.message.author
        moneyBot = await self.client.fetch_user(679160569965576192)
        if name == messageAuthor:
            await ctx.send("""**{} you can not kick yourself :man_facepalming:**""".format(messageAuthor))
        elif name == moneyBot:
            await ctx.send("""**{} you can not kick me :man_facepalming:**""".format(messageAuthor))
        else:
            await name.kick(reason = reason)
            await ctx.send("""**{} was kicked
Reason: {}**""".format(name, reason))
            guild = self.client.get_guild(ctx.guild.id)
            channel = await name.create_dm()
            await channel.send("""**You were kicked from {}
Reason: {}**""".format(guild, reason))

    @commands.command(pass_context = True, aliases=['Ban','BAN','Bann','bann','BANN'])
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, name: discord.Member, *, reason = None):
        messageAuthor = ctx.message.author
        moneyBot = await self.client.fetch_user(679160569965576192)
        if name == messageAuthor:
            await ctx.send("""**{} you can not ban yourself :man_facepalming:**""".format(messageAuthor))
        elif name == moneyBot:
            await ctx.send("""**{} you can not ban me :man_facepalming:**""".format(messageAuthor))
        else:
            await name.ban(reason = reason)
            await ctx.send("""**{} was banned
Reason: {}**""".format(name, reason))
            guild = self.client.get_guild(ctx.guild.id)
            channel = await name.create_dm()
            await channel.send("""**You were banned from {}
Reason: {}**""".format(guild, reason))

    @commands.command(pass_context = True, aliases=['Unban','UNBAN','Unbann','unbann','UNBANN'])
    @commands.has_permissions(ban_members = True)
    async def unban(self, ctx, id: int, invite: bool):
        name = await self.client.fetch_user(id)
        await ctx.guild.unban(name)
        await ctx.send("""**{} was unbanned**""".format(name))
        if invite == True:
            messageAuthor = ctx.message.author
            link = await ctx.channel.create_invite(max_age = None)
            guild = self.client.get_guild(ctx.guild.id)
            channel = await name.create_dm()
            await channel.send("""**You were unbanned from {}
{} would like to invite you back {}**""".format(guild, messageAuthor, link))
        else:
            guild = self.client.get_guild(ctx.guild.id)
            channel = await name.create_dm()
            await channel.send("""**You were unbanned from {}**""".format(guild))

    @commands.command(pass_context=True, aliases=['MUTE', 'Mute', 'mutee'])
    @commands.has_permissions(kick_members = True)
    async def mute(self, ctx, name: discord.Member, *, reason):
        messageAuthor = ctx.message.author
        moneyBot = await self.client.fetch_user(679160569965576192)
        if name == messageAuthor:
            await ctx.send("""**{} you can not mute yourself :man_facepalming:**""".format(messageAuthor))
        elif name == moneyBot:
            await ctx.send("""**{} you can not mute me :man_facepalming:**""".format(messageAuthor))
        else:
            test = discord.utils.get(name.guild.roles, name="muted")
            await discord.Member.add_roles(name, test)
            await ctx.send("""**{} was muted
Reason: {}**""".format(name, reason))
            guild = self.client.get_guild(ctx.guild.id)
            channel = await name.create_dm()
            await channel.send("""**You were muted from {}
Reason: {}**""".format(guild, reason))

    @commands.command(pass_context=True, aliases=['UNMUTE', 'Unmute', 'unmutee'])
    @commands.has_permissions(kick_members = True)
    async def unmute(self, ctx, name: discord.Member):
        test = discord.utils.get(name.guild.roles, name="muted")
        await discord.Member.remove_roles(name, test)
        await ctx.send("""**{} was unmuted**""".format(name))
        guild = self.client.get_guild(ctx.guild.id)
        channel = await name.create_dm()
        await channel.send("""**You were unmuted from {}**""".format(guild))

def setup(bot):
    bot.add_cog(moderation_commands(bot))