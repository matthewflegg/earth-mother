import discord
import dotenv
import os

from cogs.help import Help
from discord.ext import commands


def main():
    intents = discord.Intents.all()
    client = commands.Bot(command_prefix='.', help_command=Help(), intents=intents)
    client.load_extension('cogs.greetings')

    dotenv.load_dotenv('.env')
    token = os.getenv('TOKEN')
    client.run(token)


if __name__ == '__main__':
    main()