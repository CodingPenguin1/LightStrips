import random

import discord
from discord.ext import commands
from utils import *


def setup(bot):
    bot.add_cog(StudentCommands(bot))


class StudentCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def poll(self, ctx, question, *options: str):
        # Delete sender's message
        await ctx.channel.purge(limit=1)

        # Need between 2 and 10 options for a poll
        if not (1 < len(options) <= 10):
            await ctx.send('Enter between 2 and 10 answers')
            return

        # Define reactions
        if len(options) == 2 and options[0] == 'yes' and options[1] == 'no':
            reactions = ['✅', '❌']
        else:
            reactions = ['1⃣', '2⃣', '3⃣', '4⃣', '5⃣', '6⃣', '7⃣', '8⃣', '9⃣', '🔟']

        description = []
        for i, option in enumerate(options):
            description += '\n {} {}'.format(reactions[i], option)
        embed = discord.Embed(title=question, description=''.join(description))

        react_message = await ctx.send(embed=embed)
        for reaction in reactions[:len(options)]:
            await react_message.add_reaction(reaction)

        # Logging
        await log(self.bot, f'{ctx.author} started a poll in #{ctx.channel}:')
        await log(self.bot, question, False)
        for option in options:
            await log(self.bot, f'{option}', False)

    @commands.command()
    async def ping(self, ctx):
        latency = round(self.bot.latency * 1000)
        await ctx.send(f'{latency} ms')
        await log(self.bot, f'{ctx.author} pinged from #{ctx.channel}, response took {latency} ms')
