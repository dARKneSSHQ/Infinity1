#Slice Bot (For dARKneSS By dARKneSS)

#-----------------------------------------------------------------------------------------------------------------------#

#Imports
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import discord, chalk
import asyncio

#-----------------------------------------------------------------------------------------------------------------------#

#Config
prefix = "///" 
game = "With Sams Cock" #Its for the "Now Playing" status in discord.

#-----------------------------------------------------------------------------------------------------------------------#

#Prefix
bot = commands.Bot(command_prefix=prefix)

#-----------------------------------------------------------------------------------------------------------------------#

#On Ready Status
@bot.event
async def on_ready():
    print ("Im Gay Baby-")
    print (bot.user.name)
    print ("Your a werido do commentary with me.")
    await bot.change_presence(game=discord.Game(name=game))

#-----------------------------------------------------------------------------------------------------------------------#

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0x7b00ff)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)


@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Here's what I could find.", color=0x7b00ff)
    embed.set_author(name="Will Ryan of DAGames")
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)



#-----------------------------------------------------------------------------------------------------------------------#

#Leave This at Bottem
bot.run("Memes.Insert Token Here")
#Slice Made by datBNation/Samuel-Flynn New