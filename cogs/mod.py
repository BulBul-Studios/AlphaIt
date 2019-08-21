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
            await member.ban(reason=reason)
            await ctx.send(f'Banned {member.mention}')

    @commands.command()
    @has_permissions(kick_members=True, administrator=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        if ctx.message.author.server_permissions.kick:
            await member.kick(reason=reason)

    @commands.command()
    @has_permissions(ban_members=True, administrator=True)
    async def unban(self, ctx, *, member):
            banned_users = await ctx.guild.bans()
            member_name, member_discriminator = member.split('#')
            
            for ban_entry in banned_users:
                user = ban_entry.user
                
                if(user.name, user.discriminator) == (member_name, member_discriminator):
                    await ctx.guild.unban(user)
                    await ctx.send(f'Unbanned {user.mention}')

def setup(bot):
    bot.add_cog(mod(bot))
