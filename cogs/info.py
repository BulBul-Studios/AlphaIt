import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import sys
import random 
import json
from discord.utils import get
from datetime import datetime

class info(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def roleinfo(self, ctx, role: discord.Role):
        embed = discord.Embed(color=role.color, timestamp=ctx.message.created_at)
        embed.set_author(name=f"Role Info - {role.name}")
        embed.set_footer(text=f"Requested by {ctx.author} ({ctx.author.id})", icon_url=ctx.author.avatar_url)
        embed.add_field(name=f"Name", value=role.name)
        embed.add_field(name=f"ID", value=role.id)
        embed.add_field(name=f"Mention", value=role.mention)
        embed.add_field(name=f"Hoisted?", value=role.hoist)
        embed.add_field(name=f"Position", value=role.position)
        embed.add_field(name="Created at", value=role.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        await ctx.send(embed=embed)

    @commands.command()
    async def serverinfo(self, ctx, guild: discord.Guild):
        guild = ctx.author.guild if not guild else guild
        embed = discord.Embed(color=discord.Color.green() timestamp=ctx.message.created_at)
        embed.set_thumbnail(url=guild.icon_url)
        embed.set_author(name=f"Server Info - {guild.name}")
        embed.set_footer(text=f"Requested by {ctx.author} ({ctx.author.id})", icon_url=ctx.author.avatar_url)
        embed.add_field(name=f"Name:", value=guild.name)
        embed.add_field(name=f"ID:", value=guild.id)
        embed.add_field(name=f"Region", value=guild.region)
        embed.add_field(name=f"AFK Timeout", value=guild.afk_timeout)
        embed.add_field(name=f"AFK Channel", value=guild.afk_channel)
        embed.add_field(name="Created at", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        await ctx.send(embed=embed)

    @commands.command()
    async def userinfo(self, ctx, user: discord.Member):
        guild = ctx.author.guild if not guild else guild
        embed = discord.Embed(color=discord.Color.green() timestamp=ctx.message.created_at)
        embed.set_thumbnail(url=guild.icon_url)
        embed.set_author(name=f"User Info - {user.name}")
        embed.set_footer(text=f"Requested by {ctx.author} ({ctx.author.id})", icon_url=ctx.author.avatar_url)
        embed.add_field(name=f"Name:", value=guild.name)
        embed.add_field(name=f"ID:", value=guild.id)
        embed.add_field(name="Created at", value=user.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(info(bot))