import discord
from discord.ext import commands
import json
bot = commands.Bot(command_prefix='m!', case_insensitive=True)

with open("./config.json", 'r') as configjsonfile:
    configData = json.load(configjsonfile)
    TOKEN = configData["DISCORD_TOKEN"]

@bot.event
async def on_ready():
    print('I am ready!')



