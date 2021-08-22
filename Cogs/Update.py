import os

import discord
from discord.ext import commands
import subprocess


def setup(bot):
    bot.add_cog(Updates(bot))


class Updates(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def update(self, ctx):
        await ctx.send('Pulling changes')
        os.system('git pull')

        await ctx.send('Reloading cogs')
        for file in os.listdir('Cogs'):
            if not file.startswith('__') and file.endswith('.py'):
                try:
                    self.bot.reload_extension(f'Cogs.{file[:-3]}')
                except commands.errors.NoEntryPointError:
                    pass

        await ctx.send('Done')

    @commands.command()
    async def ip(self, ctx):
        output = subprocess.run(('/usr/bin/ifconfig'), shell=True, capture_output=True, text=True).stdout.split('\n')
        for line in output:
            if 'inet ' in line:
                ip = line[:line.find(' netmask')].replace('inet', ' ').strip()
                if ip != '127.0.0.1':
                    await ctx.send(ip)
                    return