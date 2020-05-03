import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import sys
import random 
import json
from discord.utils import get
from datetime import datetime

class mod(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['purge'])
    @has_permissions(manage_messages=True)
    async def clear(self, ctx,  amount=0):
        member = ctx.author
        await ctx.channel.purge(limit=amount+1)
        await ctx.send(f"Deleted {amount} messages requested by {member} ({member.id})")

    @commands.command()
    @has_permissions(ban_members=True, administrator=True)
    async def ban(self, ctx, member : discord.Member, *, reason="The Ban Hammer Has Spoken"):
            if not member:
                await ctx.send("Make sure to specify a user!")
                return
            await member.ban(reason=reason)
            await ctx.send(f'Banned {member.mention}')

def setup(bot):
    bot.add_cog(mod(bot))
