import board
import neopixel

from discord.ext import commands
from time import sleep


def setup(bot):
    bot.add_cog(Lights(bot))


class Lights(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.strip_length = 450
        self.pixels = neopixel.NeoPixel(board.D18, self.strip_length, pixel_order=neopixel.RGB)

    async def clear(self, show=True):
        for i in range(self.strip_length):
            self.pixels[i] = (0, 0, 0)
        if show:
            self.pixels.show()

    @commands.command()
    async def lights(self, ctx):
        await self.clear()
        for i in range(self.strip_length):
            self.pixels[i] = (255, 255, 255)
            self.pixels.show()
            sleep(0.05)

