import discord
import dotenv
import logging
import pandas as pd
import sys
import random

from typing import List
from discord.ext import (
    commands,
    tasks
)

dotenv.load_dotenv('.env')
logging.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler(sys.stdout)])

intents = discord.Intents.all()
status = discord.Game('🌳 Saving the Planet')
client = commands.Bot(command_prefix='.', help_command=None)

facts: List[str] = pd.read_excel('files/facts.xlsx')["facts"].values.tolist()
previous_fact = ""


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
    valid_facts = [fact for fact in facts if fact != previous_fact]
    chosen_fact = random.choice(valid_facts)

    # channel = member.guild.system_channel
    # embed = discord.Embed()

    # pass # ... TODO: Welcome messages