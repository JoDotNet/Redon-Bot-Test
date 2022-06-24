import nextcord
from nextcord.ext import commands
from nextcord import Interaction


import os

intents = nextcord.intents.default()
intents.members = True

bot = commands.Bot(intents = intents)

@bot.event
async def on_start():
    print(f'Logged in as: {bot.user}')


@bot.slash_command(name = "help", description = "help me", guild_ids=[982973690478211072])
async def help(ctx: Interaction):
    await ctx.send("Hello!")

    

bot.run(os.environ['BOT_TOKEN'])