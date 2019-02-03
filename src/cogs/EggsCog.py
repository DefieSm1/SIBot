##########################################
# These are secret commands for the bot, #
# if you want to find them by yourself,  #
# do not view this file.                 #
##########################################

from discord.ext import commands


class EggsCog:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()  # credit to u/Poem_for_you_sprog for the poem
    async def poem(self, ctx):
        await ctx.send("They be hiding by the village,\n"
                       "In the sewage,\n"
                       "At the zoo -\n"
                       "And they burn and rob and pillage,\n"
                       "And they sack and plunder too!\n\n"
                       "They be secreted, concealing,\n"
                       "In a shadow,\n"
                       "By the shade -\n"
                       "Undiscovered, unrevealing,\n"
                       "Unencountered, unsurveyed!\n\n"
                       "They be on a mystic mission,\n"
                       "And they aim to misdirect -\n"
                       "It's the Spanish Inquisition!\n\n"
                       "They be where you least expect.\n")

    async def ``


def setup(bot):
    bot.add_cog(EggsCog(bot))
