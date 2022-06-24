import nextcord
from nextcord.ext import commands
from nextcord import Interaction
#

import os

intents = nextcord.Intents.default()
intents.members = True

bot = commands.Bot(intents = intents)

@bot.event
async def on_ready():
    print(f'Logged in as: {bot.user}')


@bot.slash_command(name = "help", description = "help me", guild_ids=[982973690478211072])
async def help(ctx: Interaction):
    await ctx.send("Hello!")



initial_extentions = []

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        initial_extentions.append("cogs." + filename[:-3])

if __name__ == '__main__':
    for extention in initial_extentions:
        bot.load_extension(extention)
    

bot.run(os.environ['BOT_TOKEN'])