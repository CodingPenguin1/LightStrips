#!/usr/bin/env python3
import os

import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
import subprocess

intents = discord.Intents(messages=True, guilds=True, members=True)
bot = commands.Bot(command_prefix='!', intents=intents)
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


@bot.event
async def on_ready():
    ip_status.start()

    # Load all cogs
    for file in os.listdir('Cogs'):
        if not file.startswith('__') and file.endswith('.py'):
            try:
                bot.load_extension('Cogs.' + file[:-3])
            except commands.errors.NoEntryPointError:
                pass


@tasks.loop(seconds=60)
async def ip_status():
    #output = subprocess.run(('/usr/bin/ifconfig'), shell=True).stdout.split('\n')
    output = subprocess.run(('/sbin/ifconfig'), shell=True, stdout=subprocess.PIPE)
    #output = subprocess.run(('/sbin/ifconfig'), shell=True).stdout.split('\n')
    print(output.stdout.decode('utf-8'))
    for line in output:
        if 'inet ' in line:
            ip = line[:line.find(' netmask')].replace('inet', ' ').strip()
            if ip != '127.0.0.1':
                await bot.change_presence(activity=discord.Game(ip))
                return


if __name__ == '__main__':
    # Run bot from key given by command line argument
    bot.run(TOKEN)
