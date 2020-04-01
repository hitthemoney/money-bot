import discord
from discord.ext import commands

TOKEN = ''
prefix1 = 'money '
client = commands.Bot(command_prefix = [prefix1])
client.remove_command('help')

@client.event
async def on_ready():
    print('Bot is ready.')

#runs all of the files
client.load_extension('cogs.moderation_commands')
client.load_extension('cogs.info_commands')
client.load_extension('cogs.help_commands')
client.load_extension('cogs.social_commands')
client.load_extension('cogs.my_commands')
#April Fools Commands
client.remove_command('warn')
client.load_extension('cogs.april_fools_commands')

client.run(TOKEN) 