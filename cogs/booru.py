from pybooru import Danbooru
import discord
from discord.ext import commands
import io
import aiohttp


class Booru(commands.Cog):
    def __init__(self, client, booru_tool):
        self.client = client
        self.booru = booru_tool

    @commands.command()
    async def gayporn(self, ctx):
        image = self.booru.get_random("yaoi")
        #await ctx.send(file=discord.File(image))
        async with aiohttp.ClientSession() as session:
            async with session.get(image) as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'gay.png'))