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

        self.current_effect = self.solid
        self.kwargs = {'r': 0, 'g': 0, 'b': 0}

        while True:
            new_frame = self.current_effect(**self.kwargs)
            print(new_frame)
            for i, pixel in enumerate(new_frame):
                self.pixels[i] = pixel
            self.pixels.show()

    @commands.command()
    async def lights(self, ctx, func_name, **kwargs):
        self.current_effect = getattr(self, func_name)
        self.kwargs = kwargs
        await ctx.send(func_name + ' | ' + str(kwargs))

    def solid(self, **kwargs):
        r = kwargs['r']
        g = kwargs['g']
        b = kwargs['b']
        yield [(r, g, b) for _ in range(self.strip_length)]
