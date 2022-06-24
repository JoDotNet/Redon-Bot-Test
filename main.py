import nextcord
from nextcord.ext import commands
from nextcord import Interaction


import os

bot = commands.Bot()

@bot.event
async def on_start():
    print(f'Logged in as: {bot.user}')


@bot.slash_command(name = "help", description = "help me")
async def help(ctx: Interaction):
    await ctx.send("Hello!")

    
    
bot.run(os.environ['BOT_TOKEN'])