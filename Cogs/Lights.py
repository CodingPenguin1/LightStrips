import board
import neopixel

import discord
from discord.ext import commands
from time import sleep


def setup(bot):
    bot.add_cog(Lights(bot))


class Lights(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.strip_length = 300
        self.pixels = neopixel.NeoPixel(board.D18, self.strip_length, pixel_order=neopixel.RGB)

    @commands.command()
    async def lights(self, ctx):
        for i in range(self.strip_length):
            self.pixels[i] = (255, 255, 255)
            self.pixels.show()
            sleep(0.1)
