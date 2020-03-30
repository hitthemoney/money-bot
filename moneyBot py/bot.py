import discord
from discord.ext import commands
import msgpack

TOKEN = ''

prefix1 = 'money '

client = commands.Bot(command_prefix = [prefix1])

memberJoin = False

client.remove_command('help')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_member_join(member):
    global memberJoin
    global memberJoinName
    memberJoin = True
    memberJoinName = member

@client.command(aliases=['HELPP', 'HELP', 'Help', 'Helpp', 'helpp', 'help.', 'HELP.', 'Help.'])
async def help(ctx):
    await ctx.send("""```fix
Commands:
- money help; brings you to this page
- money warn <user> <reason>; warns a user (only works if you can kick members)
- money kick <user> <reason>; kicks a user (only works if you can kick members)
- money ban <user> <reason>; bans a user (only works if you can ban members)
- money unban <user id> <bool (True reinvites the member and False does not)>; unbans a user (only works if you can ban members)
- money mute <user> <reason>; makes a user unable to chat (only works if you can kick members, and have setup a role called "muted" (case sensitive))
- money unmute <user> <reason>; unmutes a muted user (only works if you can kick members, and have the "muted" role)
- money invite <id>; invites a user
- money yt; my YouTube channel
- money twitch; my Twitch channel
- money website; my website
- money bot_info; the bot information including invite link
- money server_info; the server info (Note this command is currently broken)

WORKING ON: fixing money server_info```""")

@client.command(aliases=['youtube', 'YT', 'Youtube', 'Yt', 'yT', 'YouTube', 'YOUTUBE'])
async def yt(ctx):
    await ctx.send('Go check out: https://www.youtube.com/channel/UCtWQuDxHtgq_wY7AxuxM__w?')
@client.command(aliases=['TWITCH', 'Twitch', 'twiCH', 'TwiCH', 'Twichh', 'TWITCHH', 'twitchh'])
async def twitch(ctx):
    await ctx.send('Go check out: https://twitch.tv/hitthemoney')
@client.command(aliases=['Website', 'WEBSITE', 'webste', 'Web', 'web', 'WEB', 'wwebsite'])
async def website(ctx):
    await ctx.send('My official website is, https://hitthemoney.github.io/')

@client.command(pass_context = True, aliases=['WARN', 'Warn',' warn', 'warN', 'WARNN', 'Warnn', 'warnn'])
@commands.has_permissions(kick_members = True)
async def warn(ctx, name: discord.Member, reason):
    await ctx.send("""**You have been warned {}. 
Reason: {}**""".format(name, reason))
    guild = client.get_guild(ctx.guild.id)
    channel = await name.create_dm()
    await channel.send("""**You were warned from {}
Reason: {}**""".format(guild, reason))

@client.command(pass_context = True, aliases=['Kick','KICK','KICKK','Kickk','kickk'])
@commands.has_permissions(kick_members = True)
async def kick(ctx, name: discord.Member, *, reason = None):
    await name.kick(reason = reason)
    await ctx.send("""**{} was kicked
Reason: {}**""".format(name, reason))
    guild = client.get_guild(ctx.guild.id)
    channel = await name.create_dm()
    await channel.send("""**You were kicked from {}
Reason: {}**""".format(guild, reason))

@client.command(pass_context = True, aliases=['Ban','BAN','Bann','bann','BANN'])
@commands.has_permissions(ban_members = True)
async def ban(ctx, name: discord.Member, *, reason = None):
    await name.ban(reason = reason)
    await ctx.send("""**{} was banned
Reason: {}**""".format(name, reason))
    guild = client.get_guild(ctx.guild.id)
    channel = await name.create_dm()
    await channel.send("""**You were banned from {}
Reason: {}**""".format(guild, reason))

@client.command(pass_context = True, aliases=['Unban','UNBAN','Unbann','unbann','UNBANN'])
@commands.has_permissions(ban_members = True)
async def unban(ctx, id: int, invite: bool):
    name = await client.fetch_user(id)
    await ctx.guild.unban(name)
    await ctx.send("""**{} was unbanned**""".format(name))
    if invite == True:
        messsageAuthor = ctx.message.author
        link = await ctx.channel.create_invite(max_age = None)
        guild = client.get_guild(ctx.guild.id)
        channel = await name.create_dm()
        await channel.send("""**You were unbanned from {}
{} would like to invite you back {}**""".format(guild, messsageAuthor, link))
    else:
        guild = client.get_guild(ctx.guild.id)
        channel = await name.create_dm()
        await channel.send("""**You were unbanned from {}**""".format(guild))

@client.command(pass_context=True, aliases=['MUTE', 'Mute', 'mutee'])
@commands.has_permissions(kick_members = True)
async def mute(ctx, name: discord.Member, reason):
    test = discord.utils.get(name.guild.roles, name="muted")
    await discord.Member.add_roles(name, test)
    await ctx.send("""**{} was muted
Reason: {}**""".format(name, reason))
    guild = client.get_guild(ctx.guild.id)
    channel = await name.create_dm()
    await channel.send("""**You were muted from {}
Reason: {}**""".format(guild, reason))

@client.command(pass_context=True, aliases=['UNMUTE', 'Unmute', 'unmutee'])
@commands.has_permissions(kick_members = True)
async def unmute(ctx, name: discord.Member):
    test = discord.utils.get(name.guild.roles, name="muted")
    await discord.Member.remove_roles(name, test)
    await ctx.send("""**{} was unmuted**""".format(name))
    guild = client.get_guild(ctx.guild.id)
    channel = await name.create_dm()
    await channel.send("""**You were unmuted from {}**""".format(guild))

@client.command(aliases=['Invite','INVITE','INVITEE','Invitee','invitee'])
async def invite(ctx, id: int):
    messsageAuthor = ctx.message.author
    name = await client.fetch_user(id)
    await ctx.send("""**{} sucessfully invited {}**""".format(messsageAuthor, name))
    link = await ctx.channel.create_invite(max_age = None)
    guild = client.get_guild(ctx.guild.id)
    channel = await name.create_dm()
    await channel.send("""**{} would like to invite you to {}**
{}""".format(messsageAuthor, guild, link))

@client.command()
async def bot_info(ctx):
    bot_info_embed = discord.Embed (
        color = discord.Color.gold(),
        title = "Bot Info"
    )
    bot_info_embed.set_thumbnail(url = "https://media.discordapp.net/attachments/667104711840628742/667105511602389007/money_logo.png")
    bot_info_embed.add_field(name = "Name", value = "moneyBot")
    bot_info_embed.add_field(name = "Version", value = "1.0.2")
    bot_info_embed.add_field(name = "Invite Link", value = "https://hitthemoney.github.io/money-bot/")
    bot_info_embed.set_footer(text = "Command: money bot_info")

    await ctx.send(embed=bot_info_embed)

@client.command()
async def server_info(ctx):
    server_info_embed = discord.Embed (
        color = discord.Color.gold(),
        title = "Server Info",
    )
    guildName = client.get_guild(ctx.guild.id)
    #server_info_embed.set_thumbnail(url = discord.Guild.icon_url) 
    server_info_embed.add_field(name = "Name", value = guildName)
    server_info_embed.add_field(name = "Member Count", value = 'Currently Broken' ) #discord.Guild.member_count
    server_info_embed.add_field(name = "Creation Date", value = 'Currently Broken' ) #discord.Guild.created_at
    server_info_embed.set_footer(text = "Command: money server_info")

    await ctx.send(embed=server_info_embed)

client.run(TOKEN) 
