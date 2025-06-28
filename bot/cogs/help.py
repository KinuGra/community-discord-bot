from discord.ext import commands
import discord
from mysql.connector import Error
from db.queries import insert_progress

class Progress(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help")
    async def add_progress(self, ctx):
        """/help 使い方の一覧を表示"""

# Cogをセットアップする関数
async def setup(bot):
    await bot.add_cog(Progress(bot))