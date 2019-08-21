import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import sys
import random 
import json
from discord.utils import get
from datetime import datetime
import os


client = commands.Bot(command_prefix='a!')
token = sys.argv[1]
client.remove_command('help')
ball = ["As I see it, yes", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don’t count on it", "It is certain", "It is decidedly so", "Most likely", "My reply is no", "My sources say no", "Outlook good", "Outlook not so good", "Reply hazy try again", "Signs point to yes", "Very doubtful", "Without a doubt","Yes","Yes, definitely," "You may rely on it"]

#Events:
@client.event
async def on_ready(aliases=['8ball']):
    servers = len(client.guilds)
    members = len(set(client.get_all_members()))
    activity = discord.Activity(name=f'{servers} servers with {members} members | a!help', type=discord.ActivityType.watching)
    await client.change_presence(activity=activity)
    print(f"Sweet, I have booted as {client.user.name} ({client.user.id})")

@commands.is_owner()
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@commands.is_owner()
@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(token)
