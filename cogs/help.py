import discord
from discord.ext import commands


class Help(commands.MinimalHelpCommand):
    """
    Implements a basic help command for the bot.
    """
    async def send_pages(self):
        """
        Sends a paginated help command.
        """
        destination = self.get_destination()
        e = discord.Embed(description='')

        for page in self.paginator.pages:
            e.description += page

        await destination.send(embed=e)