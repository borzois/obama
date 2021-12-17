import discord
from discord.ext import commands

class Misc(commands.Cog):
    def __init__(self, client, ip_manager):
        self.client = client
        self.ip_manager = ip_manager

    @commands.command()
    async def h(self, ctx):
        await ctx.send(self.ip_manager.get_ip())

    @commands.command()
    async def funnydog(self, ctx):
        await ctx.send("https://tenor.com/view/borzoi-snoopa-lord-foog-dog-funny-gif-20125052")