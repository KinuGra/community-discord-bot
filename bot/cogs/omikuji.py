from discord.ext import commands
import discord

class Omikuji(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="omikuji", aliases=["おみくじ"])
    async def add_progress():
        """おみくじを引く"""
        fortunes = ["大吉", "吉"]
        result = random.choice(fortunes)

        await ctx.send(result)

# Cogをセットアップする関数
async def setup(bot):
    await bot.add_cog(Omikuji(bot))