import discord
from discord.ext import commands

from pathlib import Path

class Voice(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.mod_path = Path(__file__).parent
        sound_folder = '../sounds/'
        self.sound_folder_path = (self.mod_path / sound_folder).resolve()

        self.gongul = (self.sound_folder_path / "gong.mp3").resolve()
        self.laugh = (self.sound_folder_path / "laugh.mp3").resolve()
        self.vineboom = (self.sound_folder_path / "vine.mp3").resolve()
        self.fart = (self.sound_folder_path / "fart.mp3").resolve()
        
        self.chan = None

    @commands.command()
    async def gong(self, ctx):
        user = ctx.message.author
        vc = user.voice.channel
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild) 

        if voice == None: 
            self.chan = await vc.connect()
        self.chan.play(discord.FFmpegOpusAudio(self.gongul))

    @commands.command()
    async def laugh(self, ctx):
        user = ctx.message.author
        vc = user.voice.channel
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild) 

        if voice == None: 
            self.chan = await vc.connect()
        self.chan.play(discord.FFmpegOpusAudio(self.laugh))

    @commands.command()
    async def vineboom(self, ctx):
        user = ctx.message.author
        vc = user.voice.channel
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild) 

        if voice == None: 
            self.chan = await vc.connect()
        self.chan.play(discord.FFmpegOpusAudio(self.vineboom))

    @commands.command()
    async def wetfart(self, ctx):
        user = ctx.message.author
        vc = user.voice.channel
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild) 

        if voice == None: 
            self.chan = await vc.connect()
        self.chan.play(discord.FFmpegOpusAudio(self.fart))

