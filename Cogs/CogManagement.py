from discord.ext import commands


def setup(bot):
    bot.add_cog(CogManagement(bot))


class CogManagement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def reload(self, ctx, cog_name):
        await ctx.send('Reloading ' + cog_name)
        self.bot.reload_extension('Cogs.' + cog_name)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unload(self, ctx, cog_name):
        if cog_name != 'CogManagement':
            await ctx.send('Unloading ' + cog_name)
            self.bot.unload_extension('Cogs.' + cog_name)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def load(self, ctx, cog_name):
        await ctx.send('Loading ' + cog_name)
        self.bot.load_extension('Cogs.' + cog_name)
