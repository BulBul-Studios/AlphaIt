import discord
from discord.ext import commands
import sys
import os
import json

def get_prefix(client, message):
    with open('prefixes.json','r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]


client = commands.Bot(command_prefix = get_prefix)
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
async def on_guild_join(guild):
    with open('prefixes.json','r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = 'a!'

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.event
async def on_guild_remove(guild):
    with open('prefixes.json','r') as f:
        prefixes = json.load(f)
    
    prefixes.pop(str(guild.id))

    with open('prefixes.joson', 'w') as f:
        json.dump(prefixes, f, indent = 4)
        
'''@client.command()
async def prefix(ctx, prefix):
    @has_permissions(administrator=True)
    with open('prefixes.json','r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix
    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)
    await ctx.send(f"Prefixed changed to {prefix}")'''


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
