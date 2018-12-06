
import discord  # needed for this whole thing to work in the first place
from discord.ext import commands  # needed for commands
import os  # remove this line, it's only so my bot token stays private or keep it if you want to do the same

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
    await ctx.send("```I am a bot created by Defie#9180. The only thing i do is scare people.\n\n"
                   "Here are some of my commands (my prefix is '///'):\n"
                   "///'info'   - shows this exact message.\n"
                   "'///github' - gives a link to my Github.\n"
                   "'///scare'  - joins a voice channel of choosing then 'scares' them.```")


@bot.command()  # links to where you are now
async def github(ctx):
    await ctx.send("Here's the link to this projects Github page: https://github.com/DefieSm1")


@bot.command()  # Joins a voice channel -> plays a sound file -> leaves
async def scare(ctx, channel: discord.VoiceChannel):
    if ctx.voice_client is not None:  # checks if bot is already in a voice channel
        return await ctx.voice_client.move_to(channel)  # moves to chosen channel

    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio('scare.mp3'), after=lambda e: print('done', e))

    while True:  # an infinite loop because of how playing a sound works
        if not vc.is_playing():  # checks if the bot is playing a sound
            await vc.disconnect()  # if no, it disconnects form the voice channel

bot.run(os.environ('BOT_TOKEN'))  # if you're not using the os library, replace this with bot.run("YOUR_BOTS_TOKEN")
