import discord
from discord.ext import commands

TOKEN = 

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
- money kick <user> <reason>; warns a user (only works if you can kick members)
- money yt; my YouTube channel
- money twitch; my Twitch channel
- money bot_info; the bot information including invite link

WORKING ON: money mute <user> and money server_info```""")

@client.command(aliases=['youtube', 'YT', 'Youtube', 'Yt', 'yT', 'YouTube', 'YOUTUBE'])
async def yt(ctx):
    await ctx.send('Go check out: https://www.youtube.com/channel/UCtWQuDxHtgq_wY7AxuxM__w?')
@client.command(aliases=['TWITCH', 'Twitch', 'twiCH', 'TwiCH', 'Twichh', 'TWITCHH', 'twitchh'])
async def twitch(ctx):
    await ctx.send('Go check out: https://twitch.tv/hitthemoney')

@client.command(pass_context = True, aliases=['WARN', 'Warn',' warn', 'warN', 'WARNN', 'Warnn', 'warnn'])
@commands.has_permissions(kick_members = True)
async def warn(ctx, name, reason):
    await ctx.send("""You have been warned {}. 
Reason: {}""".format(name, reason))

@client.command(pass_context = True)
@commands.has_permissions(kick_members = True)
async def kick(ctx, name: discord.Member, *, reason = None):
    await name.kick(reason = reason)
    await ctx.send("""{} was kicked for {}""".format(name, reason))

@client.command(pass_context = True)
@commands.has_permissions(kick_members = True)
async def mute(ctx, name: discord.User, reason1):
    author = ctx.message.author
    await ctx.send("""{} was muted by {}. 
Reason: {}""".format(name, author, reason1))
    await ctx.send_message("""You were muted {}. 
Reason: {}""".format(name, reason1))
    #await client.add_roles(*"muted", reason = reason1, atomic = True)


@client.command()
async def bot_info(ctx):
    bot_info_embed = discord.Embed (
        color = discord.Color.gold(),
        title = "Bot Info"
    )
    bot_info_embed.set_thumbnail(url = "https://media.discordapp.net/attachments/667104711840628742/667105511602389007/money_logo.png")
    bot_info_embed.add_field(name = "Name", value = "moneyBot")
    bot_info_embed.add_field(name = "Version", value = "1.0.2")
    bot_info_embed.add_field(name = "Invite Link", value = "https://hitthemoney.github.io/moneyBot/")
    bot_info_embed.set_footer(text = "Command: money bot_info")

    await ctx.send(embed=bot_info_embed)

@client.command()
async def server_info(ctx):
    server_info_embed = discord.Embed (
        color = discord.Color.gold(),
        title = "Server Info",
    )
    server_info_embed.set_thumbnail(url = discord.Guild.icon_url)
    #server_info_embed.add_field(name = "Name", value = discord.Guild.name)
    server_info_embed.add_field(name = "Member Count", value = discord.Guild.member_count)
    server_info_embed.add_field(name = "Creation Date", value = discord.Guild.created_at)
    server_info_embed.set_footer(text = "Command: money server_info")

    await ctx.send(embed=server_info_embed)

#@client.command(pass_context = True)
#@commands.has_permissions(administrator = True)
#async def change_prefix(ctx, prefix1):
    #global client
    #client = commands.Bot(command_prefix = [prefix1])
    #await ctx.send('The server prefix has been changed to "{}"'.format(prefix1))
    #return client

client.run(TOKEN) 

#discord.Guild.icon_url