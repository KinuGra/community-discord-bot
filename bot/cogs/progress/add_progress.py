from discord.ext import commands
import discord
from datetime import datetime

class Progress(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="add_progress", aliases=["ap"])
    async def add_progress(self, ctx, *, content: str):
        """進捗を記録するコマンド"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        author = ctx.author.name
        log = f"[{timestamp}] {author}: {content}\n"

        with open("progress_log.txt", "a", encoding="utf-8") as f:
            f.write(log)

        await ctx.send(f"進捗を記録しました : {content}")

# Cogをセットアップする関数
async def setup(bot):
    await bot.add_cog(Progress(bot))