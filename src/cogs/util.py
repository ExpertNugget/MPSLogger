import discord
from discord.ext import commands


class util(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(util(bot))
