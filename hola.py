import discord
from discord.ext import commands
import json
import asyncio
import random
import time
from datetime import datetime
bot = commands.Bot(command_prefix='m!', case_insensitive=True)

with open("./config.json", 'r') as configjsonfile:
    configData = json.load(configjsonfile)
    TOKEN = configData["DISCORD_TOKEN"]

@bot.event
async def on_ready():
    print('I am ready!')
# hii command
@bot.command()
async def hi(ctx):
    # await ctx.send(f'Hello {ctx.author.name}')
    by = discord.Embed(
        description = f'Hello {ctx.author.name} How Are You',
        color = discord.Color.red()
    )
    await ctx.send(embed=by)
# ping command
@bot.command()
async def ping(ctx):

    ly = discord.Embed(
        description = f'Your Ping Is {round(bot.latency*100)}ms',
        color = discord.Color.red()
    )
    await ctx.send(embed=ly)

# embed command
@bot.command()
@commands.has_permissions(manage_messages=True)
async def embed(ctx, * , msg):
    embed = discord.Embed(
        description=msg,
        color = discord.Color.blue()
    )
    await ctx.send(embed=embed)

# error handler for embed command
@embed.error
async def embed_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        lem = discord.Embed(
            description=f"Please write what you wanna embed {ctx.author.name}",
            color = discord.Color.red()
        )
        await ctx.send(embed=lem)

# clear command
@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx,amount:int):
    await ctx.channel.purge(limit=amount+1)

# error handler for clear commands
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        # await ctx.send(f"{ctx.author.name} Please Specify The Number Of Messages To Clear")
        em = discord.Embed(
            description=f"{ctx.author.name}Please Specify the number of messages to clear",
            color = discord.Color.red()
        )
        await ctx.send(embed=em)

# kick command
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member:discord.Member , * , reason=None):

    await member.kick(reason=reason)
    await ctx.send(f'{member.name} was successfully kicked for {reason}')

# error handler for kick command
@kick.error
async def kick_error(ctx , error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('please mention a user to kick')

# ban command
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member , * , reason=None):

    await member.ban(reason=reason)
    await ctx.send(f'{member.name} was successfully banned for {reason}')

# errror handler for ban command
@ban.error
async def ban_error(ctx , error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('please mention a user to ban')

# unban command
@bot.command()
async def unban(ctx, * , members):
    banned_users = await ctx.guild.bans()
    member_name, member_descriminator = members.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if(user.name, user,member_descriminator) == (member_name, member_descriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'{members.name} was unbanned')

# error hanldler for unban command
@unban.error
async def unban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('please specify a user to unban')

@bot.command()
async def timer(ctx, seconds):
    try:
        secondint = int(seconds)
        if secondint > 300:
            await ctx.send('I dont think i can go over 5 mins')
            raise BaseException
        if secondint <= 0:
            await ctx.send("I dint think i can do negatives")
            raise BaseException

        message = await ctx.send(f'Timer: {seconds}')
        while True:
            secondint -= 1
            if secondint == 0:

                await message.edit(content="Ended")
                break

            await message.edit(content=f"Timer: {secondint}")
            await asyncio.sleep(1)
        await ctx.send(f"{ctx.author.mention}, your countdown has been ended")
    except ValueError:
        await ctx.send("You must enter a number")

bot.run(TOKEN)



