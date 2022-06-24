import nextcord
from nextcord.ext import commands
from nextcord import Interaction


class Basic(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot



    @nextcord.slash_command(name = "ping", description = "Testing hehe", guild_ids=[982973690478211072])
    async def ping(self, ctx: Interaction):
        await ctx.send("Helloz")



def setup(bot):
    bot.add_cog(Basic(bot))