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
        await ctx.send(":ping_pong: Wew, I made it over the ~waves~. `{}ms` is my heartbeat (latency) :heart:.".format(round(self.client.latency * 1000, 3)))

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(color=discord.Color.green())
        embed.set_author(name="Alphait V2.5.6 Commands - prefix: a!")
        embed.add_field(name="_Utilities and infomation Commands:_", value="Useful things.")
        embed.add_field(name="a!help", value="Sends this message.")
        embed.add_field(name="a!ping", value="Send the latency of the bot.")
        embed.add_field(name="a!invite", value="Sends a link to invite the bot.")
        embed.add_field(name="a!vote", value="Sends a link to vote for the bot on a bot listing site.")
        embed.add_field(name="a!userinfo", value="Sends infomation about the specified user.")
        embed.add_field(name="a!serverinfo", value="Sends infomation about the server.")
        embed.add_field(name="a!roleinfo", value="Sends infomation about the specified role.")
        await ctx.send(embed=embed)
        embed = discord.Embed(color=discord.Color.green())
        embed.set_author(name="Alphait V2.5.6 Commands")
        embed.add_field(name="_Moderation Commands:_", value="Commands that you can use for moderation")
        embed.add_field(name="a!purge (a!clear)",value="Clears the specified amount of messages")
        embed.add_field(name="a!ban", value="Bans the specified user.")
        embed.add_field(name="a!unban", value="Unbans the specified user.")
        embed.add_field(name="a!kick", value="Kicks the specified user.")
        await ctx.send(embed=embed)
        embed = discord.Embed(color=discord.Color.green())
        embed.set_author(name="Alphait V2.5.6 Commands")
        embed.add_field(name="_Fun and Intercation Commands:_", value="Lists the fun and intercation commands of the bot.")
        embed.add_field(name="a!dab", value="You dab on the specified user.")
        embed.add_field(name="a!default", value="You default dance of the specified user.")
        embed.add_field(name="a!8ball", value="a magic 8ball.")
        embed.add_field(name="a!coinflip", value="Flips a coin.")
        embed.add_field(name="a!rps", value="it's rock paper scissors.")
        await ctx.send(embed=embed)
        
    @commands.command()
    async def invite(self, ctx):
        await ctx.send("Use this link to invite the bot! https://discordapp.com/oauth2/authorize?client_id=493973379515416577&permissions=8&scope=bot")

    @commands.command()
    async def vote(self, ctx):
        await ctx.send("Vote Here! https://discordbots.org/bot/493973379515416577/vote")

def setup(bot):
    bot.add_cog(utilities(bot))
