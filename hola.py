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

@bot.command()
async def ping(ctx):

    ly = discord.Embed(
        description = f'Your Ping Is {round(bot.latency*100)}ms',
        color = discord.Color.red()
    )
    await ctx.send(embed=ly)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def embed(ctx, * , msg):
    embed = discord.Embed(
        description=msg,
        color = discord.Color.blue()
    )
    await ctx.send(embed-embed)

@embed.error
async def embed_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        lem = discord.Embed(
            description=f"Please write what you wanna embed {ctx.author.name}",
            color = discord.Color.red()
        )
        await ctx.send(embed=lem)



bot.run(TOKEN)



