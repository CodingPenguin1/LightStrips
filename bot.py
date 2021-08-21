#!/usr/bin/env python3
import os

import discord
from discord.ext import commands
from discord_components import DiscordComponents
from dotenv import load_dotenv

intents = discord.Intents(messages=True, guilds=True, members=True)
client = commands.Bot(command_prefix='!', intents=intents)
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


@client.event
async def on_ready():
    # Set up Discord Components
    DiscordComponents(client)

    # Load all cogs
    for file in os.listdir('Cogs'):
        if not file.startswith('__') and file.endswith('.py'):
            try:
                client.load_extension(f'Cogs.{file[:-3]}')
            except commands.errors.NoEntryPointError:
                pass


if __name__ == '__main__':
    # Run bot from key given by command line argument
    client.run(TOKEN)
