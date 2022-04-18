import discord
import dotenv
import logging
import sys

from discord.ext import (
    commands,
    tasks
)

dotenv.load_dotenv('.env')
logging.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler(sys.stdout)])

intents = discord.Intents.all()
status = discord.Game('🌳 Saving the Planet')
client = commands.Bot(command_prefix='.', help_command=None)


@client.event
async def on_ready():
    """
    Called when the client has successfully loaded.
    """
    await client.change_presence(activity=status)


@client.event
async def on_member_join(member: discord.Member):
    """
    Called whenever a member joins a server.
    """
    pass # ... TODO: Welcome messages