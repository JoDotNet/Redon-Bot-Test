import nextcord
from nextcord.ext import commands

import os

bot = commands.Bot()

@bot.event
async def on_start():
    print(f'Logged in as: {bot.user}')


    
bot.run(os.environ['BOT_TOKEN'])