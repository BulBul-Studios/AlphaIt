import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import sys
import random 
import json
from discord.utils import get
from datetime import datetime

class intercations(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    async def dab(self, ctx, user: discord.User):
        embed = discord.Embed(color=discord.Color.orange())
        embed.set_author(name=f"Alphait subtly, yet epically dabs on {user}")
        embed.set_image(url="https://media.giphy.com/media/A4R8sdUG7G9TG/giphy.gif")
        await ctx.send(embed=embed)

    @commands.command()
    async def default(self, ctx, user: discord.User):
        embed = discord.Embed(color=discord.Color.orange())
        embed.set_author(name=f"{ctx.author} epically defaults on {user}")
        embed.set_image(url="https://media.tenor.com/images/4f71b921b09bfb195c0295116aa4e8dc/tenor.gif")
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(intercations(client))