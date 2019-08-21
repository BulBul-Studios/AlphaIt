import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import sys
import random 
import json
from discord.utils import get
from datetime import datetime

class Events(commands.Cog):
    
    def __init__(self, bot):
        self.client = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        servers = len(self.client.guilds)
        members = len(set(self.client.get_all_members()))
        activity = discord.Activity(name=f'{servers} servers with {members} members | a!help', type=discord.ActivityType.watching)
        channel = self.client.get_channel(612027042061615135)
        embed = discord.Embed(color=discord.Color.dark_green())
        embed.add_field(name="Joined a Server!", value=f"<:upvote:607776642189754368> AlphaIt just joined ***{guild.name}***. Now we are on ***{servers}*** servers.")
        await self.channel.send(embed=embed)
        await self.client.change_presence(activity=activity)
        
    @commands.Cog.listener()
    async def on_guild_leave(self, guild):
        servers = len(self.client.guilds)
        members = len(set(self.client.get_all_members()))
        activity = discord.Activity(name=f'{servers} servers with {members} members | a!help', type=discord.ActivityType.watching)
        channel = self.client.get_channel(612027042061615135)
        embed = discord.Embed(color=discord.Color.dark_red())
        embed.add_field(name="Lefted a Server!", value=f"<:downvote:607777806922809366> AlphaIt just lefted ***{guild.name}***. Now we are on ***{servers}*** servers.")
        await channel.send(embed=embed)
        await self.client.change_presence(activity=activity)

def setup(bot):
    bot.add_cog(Events(bot))