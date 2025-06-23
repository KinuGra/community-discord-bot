from discord.ext import commands
import discord
import random

class Omikuji(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="omikuji", aliases=["おみくじ"])
    async def omikuji(self, ctx):
        """おみくじを引く"""
        fortunes = ["大吉", "中吉", "小吉", "吉", "凶",]
        result = random.choice(fortunes)

        await ctx.send(f"{ctx.author.mention}さんの運勢は{result}です！")

# Cogをセットアップする関数
async def setup(bot):
    await bot.add_cog(Omikuji(bot))