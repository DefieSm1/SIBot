
import discord  # needed for this whole thing to work in the first place
from discord.ext import commands  # like above
import os  # this if only needed for environ.get so the bot token stays private as an environmental variable
from asyncio import sleep  # self explanatory

bot = commands.Bot(command_prefix=commands.when_mentioned_or('///'))  # adds the prefix needed to recognize commands


@bot.event  # shows the bot's name & ID in the console
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------------')

bot.remove_command('help')  # removes the pre-installed command help


@bot.command()  # shows information & all commands for bot & replaces the deleted help command
async def help(ctx):
    await ctx.send("```I am a bot created by Defie#9180. The only thing I do is scare people.\n\n"
                   "Here are some of my commands (my prefix is '///'):\n"
                   "'///help'   - shows this exact message.\n"
                   "'///github' - gives a link to this projects Github page.\n"
                   "'///scare'  - joins a voice channel of choosing then 'scares' them.\n"
                   "Current version: 0.4```")


@bot.command()  # links to where you are now
async def github(ctx):
    await ctx.send("Here's the link to this projects Github page: https://github.com/DefieSm1/SIbot")


@bot.command()  # Joins a voice channel -> plays a sound file -> leaves
async def scare(ctx, channel: discord.VoiceChannel):
    if ctx.voice_client is not None:  # checks if bot is already in a voice channel
        return await ctx.voice_client.move_to(channel)  # moves to chosen channel

    vc = await channel.connect()  # connects to the chosen channel
    vc.play(discord.FFmpegPCMAudio('scare.mp3'), after=lambda e: print('done', e))  # plays scare.mp3

    await sleep(6)  # if you're using a custom MP3, change the number to the duration of it (in seconds)

    await vc.disconnect()  # disconnects from the voice channel

bot.run(os.environ.get('BOT_TOKEN'))  # if you're not using the os library, replace this with bot.run("YOUR_BOTS_TOKEN")
