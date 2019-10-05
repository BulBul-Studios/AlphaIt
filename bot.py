import discord
from discord.ext import commands
import sys
import os

client = commands.Bot(command_prefix='a!')
token = sys.argv[1]
client.remove_command('help')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        
#Events:
@client.event
async def on_ready():
    activity = discord.Activity(name=f'{len(client.guilds)} servers with {len(set(client.get_all_members()))} members | a!help', type=discord.ActivityType.watching)
    await client.change_presence(activity=activity)
    print(f"Sweet, I have booted as {client.user.name} ({client.user.id})")
    
    
@client.event
async def on_message(message):
    if message.author.bot:
        return

    channel = client.get_channel(623360296974549012)
    await channel.send("<@212580493466664960> :eyes: you've been pinged yay")
    
    if ("69" in message.content.lower()) or ("420" in message.content.lower()):
        await message.channel.send("nice")

    
    await client.process_commands(message)

@commands.is_owner()
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f"Successfully loaded the cog `{extension}`")

@commands.is_owner()
@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f"Successfully unloaded the cog `{extension}`")
    
@commands.is_owner()
@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f"Successfully reloaded the cog `{extension}`")



client.run(token)
