import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import sys
import random 
import json
from discord.utils import get
from datetime import datetime

class utilities(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Wew, I made it over the ~waves~. `{}ms` is my latency.".format(round(self.client.latency * 1000, 3)))

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(color=discord.Color.green())
        embed.set_author(name="Alphait Commands - pefix: a! ")
        embed.add_field(name="Utility Commands:", value="`a!ping` - **Sends the bot latency.** `a!help` - **Shows this message** `a!echo` - **repeats you** `a!invite` - gives an invite to invite Alphait!")
        embed.add_field(name="Moderation Commands:", value="`a!purge` - **Clears messages. (a!clear {number})** `a!ban` - **Bans a member (a!ban {user}** `a!kick` - **Kicks a member (a!kick {user})** `a!unban` - **Unbans a member (a!unban {user}**)")
        embed.add_field(name="Interaction Commands:", value="`a!dab` - **dab on 'em haters (a!dab {user}** `a!default` - **default on 'em haters (a!default {user}**")
        embed.add_field(name="Info Commands:", value="`a!userinfo` - **Shows info about a user. (a!userinfo {user)**")
        embed.add_field(name="Fun Commands:", value= "`a!8ball` - **a 8ball**, `a!coinflip` - flips a coin `a!rps` **it's rock paper scissors")
        await ctx.send(embed=embed)


    @client.command()
    async def invite(self, ctx):
        await ctx.send("Use this link to invite the bot! https://discordapp.com/oauth2/authorize?client_id=493973379515416577&permissions=8&scope=bot")

    @client.command()
    async def vote(self, ctx):
        await ctx.send("Vote Here! https://discordbots.org/bot/493973379515416577/vote")

    @client.command()
    async def avatar(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)
        embed = embed.set_author(name=f"Avatar - {member.name}")
        embed.set_image(url=member.avatar_url)
        embed.set_footer(text=f"Requested by {ctx.author} ({ctx.author.id})", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(utilities(bot))
