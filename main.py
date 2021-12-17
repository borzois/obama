import discord
from discord.ext import tasks, commands

from pathlib import Path

from utils.utils import Ip
from repository.repo import Repository

from cogs.manual_override import Manual
from cogs.misc import Misc
from cogs.vc import Voice

client = commands.Bot(command_prefix='.', description = "Obama")
ip_manager = Ip()
repo = Repository()

@client.event
async def on_ready():
    print('{0.user} has awakened'.format(client))

client.add_cog(Manual(client, repo.get_admins()))
client.add_cog(Misc(client, ip_manager))
client.add_cog(Voice(client))

client.run(repo.get_token())



