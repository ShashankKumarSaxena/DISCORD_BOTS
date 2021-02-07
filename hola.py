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

@bot.command()
async def hi(ctx):
    # await ctx.send(f'Hello {ctx.author.name}')
    by = discord.Embed(
        description = f'Hello {ctx.author.name} How Are You',
        color = discord.Color.red()
    )
    await ctx.send(embed=by)


bot.run(TOKEN)



