import discord
import datetime
import itertools
import pandas as pd
from discord.ext import commands


class Greetings(commands.Cog):
    """
    ⚙️ Contains commands that set/remove the welcome channel.
    """
    def __init__(self, client: commands.Bot):
        """
        Creates an instance of Greetings, the main cog that manages the bot.
        """
        facts = pd.read_excel('files/facts.xlsx')

        self.client = client
        self.channel = None
        self.facts = itertools.cycle(facts.iloc[:, 0].to_list())

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    @commands.guild_only()
    async def setchannel(self, ctx: commands.Context):
        """
        ⚙️ Sets the current channel as the channel to send welcome messages in.
        """
        self.channel = ctx.channel
        embed = discord.Embed(title="⚙️ Done. I will now send welcome messages in this channel.")
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    @commands.guild_only()
    async def removechannel(self, ctx: commands.Context):
        """
        ⚙️ Stops sending welcome messages in this channel.
        """
        self.channel = None
        embed = discord.Embed(title="⚙️ Done. I will no longer send welcome messages in this channel.")
        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        """
        Sends a welcome message to new users who join a server.
        """
        if not self.channel:
            return

        embed = discord.Embed(
            title=f"👋🏻 Welcome, {member.display_name}!",
            description=next(self.facts),
            timestamp=datetime.datetime.utcnow()
        )

        await self.channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error: Exception):
        """
        Handles errors when commands in this cog are invoked.
        """
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('You don\'t have permission to use this command.')
        if isinstance(error, commands.NoPrivateMessage):
            pass
        else:
            return

def setup(client: commands.Bot):
    """
    Registers the cog with the Discord client.
    """
    client.add_cog(Greetings(client))